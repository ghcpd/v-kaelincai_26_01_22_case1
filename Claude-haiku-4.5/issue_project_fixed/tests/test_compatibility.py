"""Backward compatibility tests

This module tests that the fix maintains backward compatibility with
code written before the fix was applied.
"""
import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest


class TestBackwardCompatibility:
    """Test suite for backward compatibility"""
    
    def test_old_code_using_version(self):
        """
        Simulate old code that uses VERSION constant.
        This code should continue to work without modification.
        """
        import fake_useragent
        
        # Old code pattern: using VERSION
        version = fake_useragent.VERSION
        assert version == '0.1.6'
    
    def test_old_code_using_useragent(self):
        """
        Simulate old code that uses UserAgent class.
        This code should continue to work without modification.
        """
        import fake_useragent
        
        # Old code pattern: instantiating UserAgent
        ua = fake_useragent.UserAgent()
        chrome = ua.chrome
        firefox = ua.firefox
        
        assert isinstance(chrome, str)
        assert isinstance(firefox, str)
        assert len(chrome) > 0
        assert len(firefox) > 0
    
    def test_old_version_access_pattern(self):
        """
        Test that the old pattern of accessing VERSION still works.
        This ensures that existing code in the wild won't break.
        """
        # This is how old code might have accessed version info
        import fake_useragent
        
        # Should work (old way)
        v1 = fake_useragent.VERSION
        
        # Should also work now (new way)
        v2 = fake_useragent.__version__
        
        # Both should be equal
        assert v1 == v2
    
    def test_settings_import_unchanged(self):
        """Verify that settings module structure is unchanged"""
        from fake_useragent import settings
        assert hasattr(settings, '__version__')
        assert settings.__version__ == '0.1.6'
    
    def test_fake_module_unchanged(self):
        """Verify that fake module (UserAgent) is unchanged"""
        from fake_useragent import fake
        assert hasattr(fake, 'UserAgent')
        
        ua = fake.UserAgent()
        assert hasattr(ua, 'chrome')
        assert hasattr(ua, 'firefox')
        assert hasattr(ua, 'random')
    
    def test_old_style_useragent_import(self):
        """Test importing UserAgent the old way"""
        from fake_useragent import UserAgent
        ua = UserAgent()
        
        # All these should work
        _ = ua.chrome
        _ = ua.firefox
        _ = ua.random


class TestNoBreakingChanges:
    """Test suite to ensure no breaking changes were introduced"""
    
    def test_version_value_unchanged(self):
        """Verify that the version value hasn't changed"""
        import fake_useragent
        assert fake_useragent.__version__ == '0.1.6'
        assert fake_useragent.VERSION == '0.1.6'
    
    def test_useragent_api_unchanged(self):
        """Verify that UserAgent API hasn't changed"""
        from fake_useragent import UserAgent
        
        ua = UserAgent()
        
        # All expected properties should be present
        assert hasattr(ua, 'chrome'), "chrome property removed"
        assert hasattr(ua, 'firefox'), "firefox property removed"
        assert hasattr(ua, 'random'), "random property removed"
        
        # All properties should be callable/accessible
        assert callable(getattr(type(ua), 'chrome').fget), \
            "chrome should be a property"
        assert callable(getattr(type(ua), 'firefox').fget), \
            "firefox should be a property"
        assert callable(getattr(type(ua), 'random').fget), \
            "random should be a property"
    
    def test_no_new_module_dependencies(self):
        """Verify that no new external dependencies were added"""
        # The fix should only require standard library imports
        import fake_useragent
        import fake_useragent.fake
        import fake_useragent.settings
        
        # Just verify modules import without errors
        assert fake_useragent is not None
        assert fake_useragent.fake is not None
        assert fake_useragent.settings is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
