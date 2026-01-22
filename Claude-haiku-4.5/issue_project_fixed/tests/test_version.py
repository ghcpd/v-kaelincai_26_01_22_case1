"""Version attribute tests

This module tests that the __version__ attribute is properly exposed
according to PEP 396 standard while maintaining backward compatibility.
"""
import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fake_useragent
import pytest


class TestVersionAttribute:
    """Test suite for __version__ attribute"""
    
    def test_version_attribute_exists(self):
        """Verify that __version__ attribute exists"""
        assert hasattr(fake_useragent, '__version__'), \
            "Module 'fake_useragent' should have __version__ attribute (PEP 396)"
    
    def test_version_is_string(self):
        """Verify that __version__ is a string"""
        assert isinstance(fake_useragent.__version__, str), \
            "__version__ should be a string"
    
    def test_version_format(self):
        """Verify that __version__ has valid semantic versioning format"""
        version = fake_useragent.__version__
        # Should be in format X.Y.Z or X.Y.Z-suffix
        parts = version.split('.')
        assert len(parts) >= 2, \
            f"Version should have at least major.minor: {version}"
        # Check that first two parts are numeric
        assert parts[0].isdigit() and parts[1].isdigit(), \
            f"Major and minor version should be numeric: {version}"
    
    def test_version_value(self):
        """Verify that __version__ has the correct value"""
        assert fake_useragent.__version__ == '0.1.6', \
            "Version should be '0.1.6'"


class TestVersionConstant:
    """Test suite for backward compatibility with VERSION constant"""
    
    def test_version_constant_exists(self):
        """Verify that VERSION constant still exists for backward compatibility"""
        assert hasattr(fake_useragent, 'VERSION'), \
            "VERSION constant should exist for backward compatibility"
    
    def test_version_constant_is_string(self):
        """Verify that VERSION constant is a string"""
        assert isinstance(fake_useragent.VERSION, str), \
            "VERSION should be a string"
    
    def test_version_constant_value(self):
        """Verify that VERSION has the correct value"""
        assert fake_useragent.VERSION == '0.1.6', \
            "VERSION should be '0.1.6'"


class TestVersionConsistency:
    """Test suite for consistency between __version__ and VERSION"""
    
    def test_version_and_version_constant_match(self):
        """Verify that __version__ and VERSION refer to the same value"""
        assert fake_useragent.__version__ == fake_useragent.VERSION, \
            "__version__ and VERSION should have the same value"
    
    def test_both_accessible_from_module(self):
        """Verify that both attributes are accessible from the module"""
        # Test direct import
        import fake_useragent as fu
        assert hasattr(fu, '__version__')
        assert hasattr(fu, 'VERSION')
        
        # Test attribute access
        v1 = getattr(fu, '__version__')
        v2 = getattr(fu, 'VERSION')
        assert v1 == v2


class TestPEP396Compliance:
    """Test suite for PEP 396 compliance"""
    
    def test_pep396_compliance(self):
        """
        Verify compliance with PEP 396 (Module Version Numbers)
        https://www.python.org/dev/peps/pep-0396/
        """
        # Module should have __version__ attribute
        assert hasattr(fake_useragent, '__version__'), \
            "PEP 396 requires modules to have __version__ attribute"
        
        # __version__ should be a string
        assert isinstance(fake_useragent.__version__, str), \
            "PEP 396 requires __version__ to be a string"
        
        # Version string should be valid
        version = fake_useragent.__version__
        assert len(version) > 0, "Version string should not be empty"
        assert version[0].isdigit(), "Version should start with a digit"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
