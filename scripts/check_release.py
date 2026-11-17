#!/usr/bin/env python3
"""Consistency checks for the nlyu-pm repository. No dependencies.

Run from anywhere: python3 scripts/check_release.py
Exits 1 and lists every problem if the version, the skill list, or the
per-skill host files have drifted apart.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "nlyu-pm"
problems = []


def fail(msg):
    problems.append(msg)


def read(path):
    return path.read_text(encoding="utf-8")


def load(path):
    try:
        return json.loads(read(path))
    except (OSError, ValueError) as exc:
        fail(f"{path.relative_to(ROOT)}: cannot read as JSON ({exc})")
        return {}


# --- 1. One version everywhere -------------------------------------------
claude_market = load(ROOT / ".claude-plugin" / "marketplace.json")
codex_market = load(ROOT / ".agents" / "plugins" / "marketplace.json")
claude_plugin = load(PLUGIN / ".claude-plugin" / "plugin.json")
codex_plugin = load(PLUGIN / "plugin.json")
readme = read(ROOT / "README.md")
changelog = read(ROOT / "CHANGELOG.md")

banner = re.search(r"^║\s+v(\d+\.\d+\.\d+) ·", readme, re.M)
top_entry = re.search(r"^## (\d+\.\d+\.\d+)", changelog, re.M)
versions = {
    ".claude-plugin/marketplace.json metadata.version": claude_market.get("metadata", {}).get("version"),
    ".claude-plugin/marketplace.json plugins[0].version": (claude_market.get("plugins") or [{}])[0].get("version"),
    "plugins/nlyu-pm/.claude-plugin/plugin.json version": claude_plugin.get("version"),
    "plugins/nlyu-pm/plugin.json version": codex_plugin.get("version"),
    "README.md banner": banner.group(1) if banner else None,
    "CHANGELOG.md top entry": top_entry.group(1) if top_entry else None,
}
if len(set(versions.values())) != 1 or None in versions.values():
    fail("versions disagree:\n" + "\n".join(f"      {v}  {k}" for k, v in versions.items()))

# --- 2. Marketplaces point at the plugin ----------------------------------
for name, market in ((".claude-plugin", claude_market), (".agents/plugins", codex_market)):
    for entry in market.get("plugins", []):
        src = entry.get("source")
        path = src.get("path") if isinstance(src, dict) else src
        if not path or not (ROOT / path).is_dir():
            fail(f"{name}/marketplace.json: plugin source {path!r} is not a folder")

# --- 3. Every skill carries what both hosts need --------------------------
skills = sorted(p.name for p in (PLUGIN / "skills").iterdir() if p.is_dir())
shared_rules = read(PLUGIN / "resources" / "shared-rules.md")
host_section = shared_rules[shared_rules.find("## 11."):]

for skill in skills:
    folder = PLUGIN / "skills" / skill
    rel = folder.relative_to(ROOT)
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        fail(f"{rel}: no SKILL.md")
        continue
    text = read(skill_md)
    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    front = front.group(1) if front else ""
    if not re.search(rf"^name: {re.escape(skill)}$", front, re.M):
        fail(f"{rel}/SKILL.md: frontmatter name is not '{skill}'")
    if not re.search(r"^disable-model-invocation: true$", front, re.M):
        fail(f"{rel}/SKILL.md: missing 'disable-model-invocation: true' (Claude Code manual-only)")
    if "**Plugin root.**" not in text or "${CLAUDE_PLUGIN_ROOT}" not in text:
        fail(f"{rel}/SKILL.md: missing the 'Plugin root' paragraph that resolves <plugin-root>")
    if text.count("${CLAUDE_PLUGIN_ROOT}") > 1:
        fail(f"{rel}/SKILL.md: uses ${{CLAUDE_PLUGIN_ROOT}} outside the 'Plugin root' paragraph; write <plugin-root>")
    policy = folder / "agents" / "openai.yaml"
    if not policy.is_file() or not re.search(r"^\s+allow_implicit_invocation:\s*false\b", read(policy), re.M):
        fail(f"{rel}/agents/openai.yaml: missing or lacks 'allow_implicit_invocation: false' (Codex manual-only)")
    if f"`/nlyu-pm:{skill}`" not in host_section or f"`${skill}`" not in host_section:
        fail(f"shared-rules.md section 11: host table does not list /nlyu-pm:{skill} and ${skill}")
    if not (ROOT / "docs" / "skills" / f"{skill}.md").is_file():
        fail(f"docs/skills/{skill}.md: no page for this skill")
    if f"docs/skills/{skill}.md" not in readme:
        fail(f"README.md: no link to docs/skills/{skill}.md")

count = re.search(r"^║\s+(\d+) skills ·", readme, re.M)
if not count or int(count.group(1)) != len(skills):
    fail(f"README.md banner skill count is {count.group(1) if count else 'missing'}, but there are {len(skills)} skills")

# --- 4. Resources never use the Claude-only variable ----------------------
for path in sorted((PLUGIN / "resources").rglob("*.md")):
    uses = read(path).count("${CLAUDE_PLUGIN_ROOT}")
    allowed = 1 if path.name == "shared-rules.md" else 0  # the note about older session files
    if uses > allowed:
        fail(f"{path.relative_to(ROOT)}: uses ${{CLAUDE_PLUGIN_ROOT}}; write <plugin-root>")

# --- 5. Codex starter prompts name real skills ----------------------------
interface = codex_plugin.get("extensions", {}).get("com.openai", {}).get("interface", {})
for prompt in interface.get("defaultPrompt", []):
    for name in re.findall(r"\$([a-z][a-z-]*)", prompt):
        if name not in skills:
            fail(f"plugins/nlyu-pm/plugin.json: starter prompt names ${name}, which is not a skill")
for key in ("composerIcon", "logo"):
    icon = interface.get(key)
    if icon and not (PLUGIN / icon).is_file():
        fail(f"plugins/nlyu-pm/plugin.json: {key} {icon!r} does not exist")

if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
print(f"OK: version {versions['README.md banner']}, {len(skills)} skills ({', '.join(skills)})")
