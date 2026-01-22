"""Backward-compatibility tests (ensure old code keeps working)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fake_useragent


def test_imports_and_legacy_usage_remain_compatible():
    # Simulate old-style usage
    legacy = fake_useragent.VERSION
    modern = fake_useragent.__version__
    assert legacy == modern

    # Import the constant directly (old code might do this)
    from fake_useragent import VERSION as V
    assert V == fake_useragent.__version__

    # settings still expose the canonical value
    from fake_useragent import settings
    assert settings.__version__ == fake_useragent.__version__
