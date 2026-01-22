"""Backward Compatibility Tests

Tests to ensure that code written for the old version still works with the fix.
"""
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import fake_useragent


def test_old_code_using_version_constant():
    """Test that old code using VERSION still works"""
    # This is how old code accessed the version
    version = fake_useragent.VERSION
    assert version == '0.1.6', "VERSION constant should still work"


def test_old_code_user_agent_import():
    """Test that old import patterns still work"""
    # Old code might have imported like this
    from fake_useragent import UserAgent
    
    ua = UserAgent()
    assert ua is not None, "Direct UserAgent import should still work"


def test_old_code_basic_usage():
    """Test that old basic usage pattern still works"""
    # Typical old code pattern
    from fake_useragent import UserAgent
    
    ua = UserAgent()
    chrome_ua = ua.chrome
    
    assert isinstance(chrome_ua, str), "Old usage pattern should work"
    assert len(chrome_ua) > 0, "Should return valid user agent"


def test_version_constant_type():
    """Test that VERSION is still a string (as it was before)"""
    assert isinstance(fake_useragent.VERSION, str), \
        "VERSION should remain a string for compatibility"


def test_version_constant_value_unchanged():
    """Test that VERSION value is exactly what it was before"""
    assert fake_useragent.VERSION == '0.1.6', \
        "VERSION value should remain unchanged"


def test_module_api_completeness():
    """Test that all expected module attributes are present"""
    # Core functionality
    assert hasattr(fake_useragent, 'UserAgent'), \
        "UserAgent should be available"
    
    # Version info
    assert hasattr(fake_useragent, 'VERSION'), \
        "VERSION should be available (backward compatibility)"
    
    # New PEP 396 compliance
    assert hasattr(fake_useragent, '__version__'), \
        "__version__ should be available (new feature)"


def test_no_api_breaking_changes():
    """Test that no existing APIs were broken"""
    # Get all public attributes
    public_attrs = [attr for attr in dir(fake_useragent) 
                   if not attr.startswith('_') or attr == '__version__']
    
    # Should have at least these
    expected_attrs = ['UserAgent', 'VERSION', '__version__']
    
    for attr in expected_attrs:
        assert attr in public_attrs, \
            f"{attr} should be in module's public API"


def test_old_code_checking_version_exists():
    """Test old code that might check if VERSION exists"""
    # Old code might have done this check
    if hasattr(fake_useragent, 'VERSION'):
        version = fake_useragent.VERSION
        assert version == '0.1.6', "Should still work as before"
    else:
        assert False, "VERSION should exist for backward compatibility"


if __name__ == '__main__':
    print("Running Backward Compatibility Tests...")
    print("=" * 60)
    
    tests = [
        test_old_code_using_version_constant,
        test_old_code_user_agent_import,
        test_old_code_basic_usage,
        test_version_constant_type,
        test_version_constant_value_unchanged,
        test_module_api_completeness,
        test_no_api_breaking_changes,
        test_old_code_checking_version_exists,
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
        print("🎉 All compatibility tests passed!")
    else:
        sys.exit(1)
