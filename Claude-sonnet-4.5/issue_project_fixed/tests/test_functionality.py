"""Functionality Completeness Tests

Tests to ensure that the fix doesn't break core UserAgent functionality.
"""
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import fake_useragent


def test_user_agent_can_be_imported():
    """Test that UserAgent class can be imported"""
    assert hasattr(fake_useragent, 'UserAgent'), \
        "UserAgent class should be importable from module"


def test_user_agent_instantiation():
    """Test that UserAgent can be instantiated"""
    ua = fake_useragent.UserAgent()
    assert ua is not None, "UserAgent should be instantiable"


def test_chrome_user_agent():
    """Test that Chrome user agent works"""
    ua = fake_useragent.UserAgent()
    chrome_ua = ua.chrome
    
    assert isinstance(chrome_ua, str), "Chrome UA should be a string"
    assert len(chrome_ua) > 0, "Chrome UA should not be empty"
    assert 'Chrome' in chrome_ua, "Chrome UA should contain 'Chrome'"


def test_firefox_user_agent():
    """Test that Firefox user agent works"""
    ua = fake_useragent.UserAgent()
    firefox_ua = ua.firefox
    
    assert isinstance(firefox_ua, str), "Firefox UA should be a string"
    assert len(firefox_ua) > 0, "Firefox UA should not be empty"
    assert 'Firefox' in firefox_ua, "Firefox UA should contain 'Firefox'"


def test_random_user_agent():
    """Test that random user agent works"""
    ua = fake_useragent.UserAgent()
    random_ua = ua.random
    
    assert isinstance(random_ua, str), "Random UA should be a string"
    assert len(random_ua) > 0, "Random UA should not be empty"
    assert 'Mozilla' in random_ua, "Random UA should contain 'Mozilla'"


def test_user_agent_returns_different_values():
    """Test that user agent can return different values on repeated calls"""
    ua = fake_useragent.UserAgent()
    
    # Get multiple random UAs
    uas = [ua.random for _ in range(10)]
    
    # Should have at least some variation (not all the same)
    # This might fail rarely due to randomness, but very unlikely with 10 calls
    assert len(set(uas)) > 1 or len(uas) == 1, \
        "Random UA should provide variation (or have only one option)"


def test_user_agent_properties_are_properties():
    """Test that chrome, firefox, random are properties"""
    ua = fake_useragent.UserAgent()
    
    # Properties should be accessible without calling as methods
    try:
        _ = ua.chrome
        _ = ua.firefox
        _ = ua.random
    except TypeError:
        assert False, "Properties should be accessible without ()"


def test_multiple_instances():
    """Test that multiple UserAgent instances work independently"""
    ua1 = fake_useragent.UserAgent()
    ua2 = fake_useragent.UserAgent()
    
    assert ua1 is not ua2, "Different instances should be different objects"
    
    # Both should work independently
    assert isinstance(ua1.chrome, str), "First instance should work"
    assert isinstance(ua2.chrome, str), "Second instance should work"


if __name__ == '__main__':
    print("Running Functionality Completeness Tests...")
    print("=" * 60)
    
    tests = [
        test_user_agent_can_be_imported,
        test_user_agent_instantiation,
        test_chrome_user_agent,
        test_firefox_user_agent,
        test_random_user_agent,
        test_user_agent_returns_different_values,
        test_user_agent_properties_are_properties,
        test_multiple_instances,
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
        print("🎉 All functionality tests passed!")
    else:
        sys.exit(1)
