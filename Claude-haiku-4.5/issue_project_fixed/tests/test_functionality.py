"""Functionality completeness tests

This module tests that the core UserAgent functionality works properly
and that the fix doesn't break any existing functionality.
"""
import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fake_useragent
import pytest


class TestUserAgentClass:
    """Test suite for UserAgent class functionality"""
    
    def test_useragent_class_exists(self):
        """Verify that UserAgent class is accessible"""
        assert hasattr(fake_useragent, 'UserAgent'), \
            "UserAgent class should be accessible from module"
    
    def test_useragent_instantiation(self):
        """Verify that UserAgent can be instantiated"""
        ua = fake_useragent.UserAgent()
        assert ua is not None, "UserAgent should be instantiable"
        assert isinstance(ua, fake_useragent.UserAgent), \
            "Instance should be of UserAgent type"
    
    def test_chrome_property(self):
        """Verify that chrome property returns a user agent string"""
        ua = fake_useragent.UserAgent()
        chrome_ua = ua.chrome
        assert isinstance(chrome_ua, str), "chrome property should return string"
        assert len(chrome_ua) > 0, "chrome user agent string should not be empty"
        assert 'Chrome' in chrome_ua or 'Chrome' in str(chrome_ua), \
            "chrome property should return Chrome user agent"
    
    def test_firefox_property(self):
        """Verify that firefox property returns a user agent string"""
        ua = fake_useragent.UserAgent()
        firefox_ua = ua.firefox
        assert isinstance(firefox_ua, str), "firefox property should return string"
        assert len(firefox_ua) > 0, "firefox user agent string should not be empty"
        assert 'Firefox' in firefox_ua or 'Firefox' in str(firefox_ua), \
            "firefox property should return Firefox user agent"
    
    def test_random_property(self):
        """Verify that random property returns a user agent string"""
        ua = fake_useragent.UserAgent()
        random_ua = ua.random
        assert isinstance(random_ua, str), "random property should return string"
        assert len(random_ua) > 0, "random user agent string should not be empty"
    
    def test_multiple_instances(self):
        """Verify that multiple UserAgent instances work independently"""
        ua1 = fake_useragent.UserAgent()
        ua2 = fake_useragent.UserAgent()
        
        chrome1 = ua1.chrome
        chrome2 = ua2.chrome
        
        # Both should be valid strings
        assert isinstance(chrome1, str) and isinstance(chrome2, str)
        # Both should return Chrome user agents (though possibly different ones)
        assert 'Chrome' in chrome1 or 'Chrome' in str(chrome1)
        assert 'Chrome' in chrome2 or 'Chrome' in str(chrome2)
    
    def test_random_variety(self):
        """Verify that random property returns different values"""
        ua = fake_useragent.UserAgent()
        agents = set()
        
        # Generate multiple random user agents
        for _ in range(10):
            agent = ua.random
            agents.add(agent)
        
        # Should have at least 2 different agents
        assert len(agents) >= 2, \
            "random property should return different user agents"


class TestPublicAPI:
    """Test suite for public API completeness"""
    
    def test_all_export(self):
        """Verify that __all__ is properly defined"""
        assert hasattr(fake_useragent, '__all__'), \
            "Module should define __all__"
        
        all_items = fake_useragent.__all__
        # Should at least include UserAgent, __version__, and VERSION
        assert 'UserAgent' in all_items, "__all__ should include UserAgent"
        assert '__version__' in all_items, "__all__ should include __version__"
        assert 'VERSION' in all_items, "__all__ should include VERSION"


class TestImportVariations:
    """Test suite for different import styles"""
    
    def test_from_import_version(self):
        """Verify that __version__ can be imported directly"""
        from fake_useragent import __version__
        assert __version__ == '0.1.6'
    
    def test_from_import_useragent(self):
        """Verify that UserAgent can be imported directly"""
        from fake_useragent import UserAgent
        ua = UserAgent()
        assert ua is not None
    
    def test_from_import_version_constant(self):
        """Verify that VERSION can be imported directly"""
        from fake_useragent import VERSION
        assert VERSION == '0.1.6'
    
    def test_star_import(self):
        """Verify that star import works properly"""
        # Note: In real projects, star imports are discouraged,
        # but we test that __all__ is proper
        import fake_useragent
        for name in fake_useragent.__all__:
            assert hasattr(fake_useragent, name), \
                f"__all__ lists {name} but it's not accessible"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
