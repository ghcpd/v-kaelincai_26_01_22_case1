"""Version attribute tests (PEP 396 + backward compatibility)"""
import os
import sys
import re

# Ensure tests import the local package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fake_useragent


def test_has_version_attributes():
    assert hasattr(fake_useragent, '__version__'), "__version__ must be exposed (PEP 396)"
    assert hasattr(fake_useragent, 'VERSION'), "legacy VERSION must still be present"


def test_versions_are_equal_and_valid_semver():
    v1 = fake_useragent.__version__
    v2 = fake_useragent.VERSION
    assert v1 == v2

    # Basic semantic-version-like check (allowing suffixes)
    assert re.match(r'^\d+\.\d+\.\d+(?:[.-][A-Za-z0-9]+)?$', v1), f"bad version format: {v1}"
