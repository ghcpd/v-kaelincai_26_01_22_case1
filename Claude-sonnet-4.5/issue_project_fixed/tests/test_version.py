"""Version Attribute Tests

Tests to verify that both __version__ and VERSION attributes are properly exposed
and follow PEP 396 standards.
"""
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import fake_useragent


def test_version_attribute_exists():
    """Test that __version__ attribute exists"""
    assert hasattr(fake_useragent, '__version__'), \
        "Module should have __version__ attribute (PEP 396)"


def test_version_constant_exists():
    """Test that VERSION constant exists (backward compatibility)"""
    assert hasattr(fake_useragent, 'VERSION'), \
        "Module should have VERSION constant for backward compatibility"


def test_version_values_are_equal():
    """Test that __version__ and VERSION have the same value"""
    assert fake_useragent.__version__ == fake_useragent.VERSION, \
        "__version__ and VERSION should have the same value"


def test_version_format():
    """Test that version number follows semantic versioning format"""
    version = fake_useragent.__version__
    assert isinstance(version, str), "Version should be a string"
    
    # Check basic format (X.Y.Z)
    parts = version.split('.')
    assert len(parts) >= 2, "Version should have at least major.minor format"
    
    # Check that major and minor are numeric
    assert parts[0].isdigit(), "Major version should be numeric"
    assert parts[1].isdigit(), "Minor version should be numeric"


def test_version_is_string():
    """Test that version is a string type"""
    assert isinstance(fake_useragent.__version__, str), \
        "__version__ should be a string"
    assert isinstance(fake_useragent.VERSION, str), \
        "VERSION should be a string"


def test_version_value():
    """Test that version has expected value"""
    assert fake_useragent.__version__ == '0.1.6', \
        "Version should be 0.1.6"


def test_version_immutability():
    """Test that version references point to the same object"""
    # Both should reference the same value
    assert fake_useragent.__version__ is fake_useragent.VERSION or \
           fake_useragent.__version__ == fake_useragent.VERSION, \
        "Both version attributes should be equivalent"


if __name__ == '__main__':
    print("Running Version Attribute Tests...")
    print("=" * 60)
    
    tests = [
        test_version_attribute_exists,
        test_version_constant_exists,
        test_version_values_are_equal,
        test_version_format,
        test_version_is_string,
        test_version_value,
        test_version_immutability,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error - {e}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All version tests passed!")
    else:
        sys.exit(1)
