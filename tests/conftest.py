from __future__ import annotations

import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

"""
Pytest configuration for the Project Chimera codebase.

This file ensures that the project root (which contains the `skills` package
and application modules) is available on `sys.path` for all tests.
"""
