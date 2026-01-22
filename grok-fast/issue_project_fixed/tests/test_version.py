"""Test version attribute availability and correctness"""
import pytest
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_version_attribute_exists():
    """Test that __version__ attribute exists"""
    import fake_useragent
    assert hasattr(fake_useragent, '__version__')


def test_version_constant_exists():
    """Test that VERSION constant exists (backward compatibility)"""
    import fake_useragent
    assert hasattr(fake_useragent, 'VERSION')


def test_version_values_match():
    """Test that __version__ and VERSION have the same value"""
    import fake_useragent
    assert fake_useragent.__version__ == fake_useragent.VERSION


def test_version_format():
    """Test that version follows semantic versioning format"""
    import fake_useragent
    version = fake_useragent.__version__
    # Basic semver check: x.y.z format
    parts = version.split('.')
    assert len(parts) >= 2
    assert all(part.isdigit() for part in parts)