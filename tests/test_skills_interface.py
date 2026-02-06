from pathlib import Path

"""Tests for the skills interface and documentation.

These tests validate that the high-level contracts for skills are present
in the specs and README files, without depending on concrete implementations.
"""
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILLS_README = PROJECT_ROOT / "skills" / "README.md"
FUNCTIONAL_SPECS = PROJECT_ROOT / "specs" / "functional.md"
TECHNICAL_SPECS = PROJECT_ROOT / "specs" / "technical.md"


def _read(path: Path) -> str:
    """Read a file as UTF-8 text."""

    return path.read_text(encoding="utf-8")


def test_skills_readme_lists_three_skills() -> None:
    """The skills README should document at least three core skills."""

    content = _read(SKILLS_README)
    assert "skill-trend-scout" in content
    assert "skill-wallet-manager" in content
    assert "skill-media-orchestrator" in content


def test_functional_specs_describe_skill_interfaces() -> None:
    """Functional specification should describe high-level skill interfaces."""

    content = _read(FUNCTIONAL_SPECS)
    assert "Trend Scout Skill" in content
    assert "Wallet Manager Skill" in content
    assert "Media Orchestrator Skill" in content


def test_technical_specs_define_wallet_manager_contract() -> None:
    """Technical specification must define the WalletManager contract."""

    content = _read(TECHNICAL_SPECS)
    assert "Wallet Manager Skill Contract" in content
    assert "WalletManager" in content
    assert "execute_transaction" in content

