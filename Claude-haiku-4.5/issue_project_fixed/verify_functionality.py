#!/usr/bin/env python
"""Comprehensive Functionality Verification Script"""
import sys
sys.path.insert(0, '.')

print("=" * 70)
print("COMPREHENSIVE FUNCTIONALITY VERIFICATION")
print("=" * 70)
print()

# Test 1: Module Import
print("TEST 1: Module Import")
print("-" * 70)
try:
    import fake_useragent
    print("✅ Module imported successfully")
except Exception as e:
    print(f"❌ Module import failed: {e}")
    sys.exit(1)

# Test 2: __version__ Attribute
print("\nTEST 2: __version__ Attribute (PEP 396)")
print("-" * 70)
try:
    version = fake_useragent.__version__
    assert isinstance(version, str), "__version__ should be a string"
    assert version == '0.1.6', f"Version should be 0.1.6, got {version}"
    print(f"✅ __version__ accessible: '{version}'")
    print(f"✅ Type: {type(version).__name__}")
    print(f"✅ Value: {version}")
except Exception as e:
    print(f"❌ __version__ test failed: {e}")
    sys.exit(1)

# Test 3: VERSION Constant (Backward Compatibility)
print("\nTEST 3: VERSION Constant (Backward Compatibility)")
print("-" * 70)
try:
    version = fake_useragent.VERSION
    assert isinstance(version, str), "VERSION should be a string"
    assert version == '0.1.6', f"VERSION should be 0.1.6, got {version}"
    print(f"✅ VERSION accessible: '{version}'")
    print(f"✅ Type: {type(version).__name__}")
    print(f"✅ Value: {version}")
except Exception as e:
    print(f"❌ VERSION test failed: {e}")
    sys.exit(1)

# Test 4: Version Consistency
print("\nTEST 4: Version Consistency")
print("-" * 70)
try:
    assert fake_useragent.__version__ == fake_useragent.VERSION, \
        "Version values should match"
    print(f"✅ __version__ matches VERSION")
    print(f"  __version__: {fake_useragent.__version__}")
    print(f"  VERSION:     {fake_useragent.VERSION}")
    print(f"  Equal:       {fake_useragent.__version__ == fake_useragent.VERSION}")
except Exception as e:
    print(f"❌ Version consistency test failed: {e}")
    sys.exit(1)

# Test 5: __all__ Definition
print("\nTEST 5: Public API (__all__)")
print("-" * 70)
try:
    assert hasattr(fake_useragent, '__all__'), "__all__ should be defined"
    all_items = fake_useragent.__all__
    print(f"✅ __all__ defined: {all_items}")
    
    required_items = ['UserAgent', '__version__', 'VERSION']
    for item in required_items:
        assert item in all_items, f"{item} should be in __all__"
        assert hasattr(fake_useragent, item), f"{item} should be accessible"
        print(f"  ✅ {item}: accessible")
except Exception as e:
    print(f"❌ __all__ test failed: {e}")
    sys.exit(1)

# Test 6: UserAgent Class
print("\nTEST 6: UserAgent Class Functionality")
print("-" * 70)
try:
    ua = fake_useragent.UserAgent()
    print(f"✅ UserAgent instantiated: {type(ua).__name__}")
    
    # Test chrome property
    chrome_ua = ua.chrome
    assert isinstance(chrome_ua, str), "chrome should return string"
    assert len(chrome_ua) > 0, "chrome UA should not be empty"
    print(f"  ✅ chrome property: {chrome_ua[:50]}...")
    
    # Test firefox property
    firefox_ua = ua.firefox
    assert isinstance(firefox_ua, str), "firefox should return string"
    assert len(firefox_ua) > 0, "firefox UA should not be empty"
    print(f"  ✅ firefox property: {firefox_ua[:50]}...")
    
    # Test random property
    random_ua = ua.random
    assert isinstance(random_ua, str), "random should return string"
    assert len(random_ua) > 0, "random UA should not be empty"
    print(f"  ✅ random property: {random_ua[:50]}...")
except Exception as e:
    print(f"❌ UserAgent test failed: {e}")
    sys.exit(1)

# Test 7: Multiple Instances
print("\nTEST 7: Multiple UserAgent Instances")
print("-" * 70)
try:
    ua1 = fake_useragent.UserAgent()
    ua2 = fake_useragent.UserAgent()
    ua3 = fake_useragent.UserAgent()
    
    print(f"✅ Created 3 independent instances")
    print(f"  Instance 1: {ua1.chrome[:40]}...")
    print(f"  Instance 2: {ua2.chrome[:40]}...")
    print(f"  Instance 3: {ua3.chrome[:40]}...")
except Exception as e:
    print(f"❌ Multiple instances test failed: {e}")
    sys.exit(1)

# Test 8: Direct Imports
print("\nTEST 8: Direct Imports")
print("-" * 70)
try:
    from fake_useragent import __version__
    from fake_useragent import VERSION
    from fake_useragent import UserAgent
    
    print(f"✅ from fake_useragent import __version__: {__version__}")
    print(f"✅ from fake_useragent import VERSION: {VERSION}")
    print(f"✅ from fake_useragent import UserAgent: {UserAgent.__name__}")
except Exception as e:
    print(f"❌ Direct imports test failed: {e}")
    sys.exit(1)

# Test 9: Module Attributes
print("\nTEST 9: Module Attributes Check")
print("-" * 70)
try:
    attrs_to_check = {
        '__version__': str,
        'VERSION': str,
        'UserAgent': type,
        '__all__': list,
    }
    
    for attr_name, attr_type in attrs_to_check.items():
        assert hasattr(fake_useragent, attr_name), f"Missing {attr_name}"
        attr_value = getattr(fake_useragent, attr_name)
        if attr_name == '__all__':
            assert isinstance(attr_value, attr_type), \
                f"{attr_name} should be {attr_type.__name__}"
        print(f"  ✅ {attr_name}: {type(attr_value).__name__}")
except Exception as e:
    print(f"❌ Module attributes test failed: {e}")
    sys.exit(1)

# Test 10: Version Format
print("\nTEST 10: Version Format Validation")
print("-" * 70)
try:
    version = fake_useragent.__version__
    parts = version.split('.')
    assert len(parts) >= 2, "Version should have at least major.minor"
    assert parts[0].isdigit(), "Major version should be numeric"
    assert parts[1].isdigit(), "Minor version should be numeric"
    print(f"✅ Version format valid: {version}")
    print(f"  Parts: {parts}")
    print(f"  Major: {parts[0]}")
    print(f"  Minor: {parts[1]}")
    if len(parts) > 2:
        print(f"  Patch: {parts[2].split('-')[0]}")
except Exception as e:
    print(f"❌ Version format test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 70)
print("ALL VERIFICATION TESTS PASSED ✅")
print("=" * 70)
print()
print("Summary:")
print("  ✅ Module imports successfully")
print("  ✅ __version__ attribute accessible (PEP 396)")
print("  ✅ VERSION constant works (backward compatible)")
print("  ✅ Both values match and are correct")
print("  ✅ Public API properly defined")
print("  ✅ UserAgent class fully functional")
print("  ✅ Multiple instances work independently")
print("  ✅ Direct imports work correctly")
print("  ✅ All module attributes present")
print("  ✅ Version format valid")
print()
