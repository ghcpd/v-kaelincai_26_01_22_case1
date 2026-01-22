"""Test backward compatibility - ensure old code still works"""
import pytest
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_old_version_access_pattern():
    """Test that old code using VERSION still works"""
    import fake_useragent

    # Simulate old code that used VERSION
    version = fake_useragent.VERSION
    assert version == '0.1.6'


def test_old_import_pattern():
    """Test that old import patterns still work"""
    import fake_useragent

    # Old code might do this
    ua = fake_useragent.UserAgent()
    chrome = ua.chrome
    firefox = ua.firefox
    random = ua.random

    assert all(isinstance(x, str) for x in [chrome, firefox, random])


def test_no_breaking_changes():
    """Test that no existing functionality was broken"""
    import fake_useragent

    # All these should work as before
    assert hasattr(fake_useragent, 'UserAgent')
    assert hasattr(fake_useragent, 'VERSION')

    ua = fake_useragent.UserAgent()
    assert hasattr(ua, 'chrome')
    assert hasattr(ua, 'firefox')
    assert hasattr(ua, 'random')


def test_new_and_old_version_access():
    """Test that both new and old version access methods work"""
    import fake_useragent

    # New way (PEP 396 compliant)
    new_version = fake_useragent.__version__

    # Old way (backward compatible)
    old_version = fake_useragent.VERSION

    assert new_version == old_version
    assert new_version == '0.1.6'