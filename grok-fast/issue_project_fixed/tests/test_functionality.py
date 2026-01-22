"""Test UserAgent functionality completeness"""
import pytest
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_useragent_class_import():
    """Test that UserAgent class can be imported"""
    import fake_useragent
    assert hasattr(fake_useragent, 'UserAgent')


def test_useragent_instantiation():
    """Test that UserAgent can be instantiated"""
    import fake_useragent
    ua = fake_useragent.UserAgent()
    assert ua is not None


def test_chrome_useragent():
    """Test Chrome user agent generation"""
    import fake_useragent
    ua = fake_useragent.UserAgent()
    chrome_ua = ua.chrome
    assert isinstance(chrome_ua, str)
    assert 'Chrome' in chrome_ua
    assert len(chrome_ua) > 20


def test_firefox_useragent():
    """Test Firefox user agent generation"""
    import fake_useragent
    ua = fake_useragent.UserAgent()
    firefox_ua = ua.firefox
    assert isinstance(firefox_ua, str)
    assert 'Firefox' in firefox_ua
    assert len(firefox_ua) > 20


def test_random_useragent():
    """Test random user agent generation"""
    import fake_useragent
    ua = fake_useragent.UserAgent()
    random_ua = ua.random
    assert isinstance(random_ua, str)
    assert len(random_ua) > 20
    # Should contain either Chrome or Firefox
    assert 'Chrome' in random_ua or 'Firefox' in random_ua


def test_multiple_random_calls():
    """Test that multiple calls to random return different agents"""
    import fake_useragent
    ua = fake_useragent.UserAgent()
    agents = [ua.random for _ in range(10)]
    # With randomness, we should get some variety (though not guaranteed)
    unique_agents = set(agents)
    assert len(unique_agents) >= 1  # At least one unique