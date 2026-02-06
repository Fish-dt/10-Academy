from pathlib import Path

"""Tests for the trend-fetching / scouting specification.

These tests assert that the research and skills documentation correctly
describe the `skill-trend-scout` behavior.
"""
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILLS_README = PROJECT_ROOT / "skills" / "README.md"
ARCHITECTURE_RESEARCH = PROJECT_ROOT / "research" / "architecture_strategy.md"


def _read(path: Path) -> str:
    """Read a file as UTF-8 text."""

    return path.read_text(encoding="utf-8")


def test_skills_readme_defines_trend_scout() -> None:
    """The skills catalog must define the `skill-trend-scout` entry."""

    content = _read(SKILLS_README)
    assert "skill-trend-scout" in content
    assert "viral topics" in content or "trends" in content
    assert "Viral Potential" in content


def test_research_mentions_mcp_and_trends() -> None:
    """Architecture research should reference MCP and agent networking."""

    content = _read(ARCHITECTURE_RESEARCH)
    assert "Model Context Protocol" in content or "MCP" in content
    assert "OpenClaw" in content or "agent" in content

