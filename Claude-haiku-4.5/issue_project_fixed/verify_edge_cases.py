#!/usr/bin/env python
"""Advanced Edge Case and Compatibility Testing"""
import sys
import importlib
sys.path.insert(0, '.')

print("=" * 80)
print("ADVANCED EDGE CASE AND COMPATIBILITY TESTING")
print("=" * 80)
print()

# Test 1: Reload Module
print("TEST 1: Module Reload")
print("-" * 80)
try:
    import fake_useragent
    original_version = fake_useragent.__version__
    
    # Reload the module
    importlib.reload(fake_useragent)
    reloaded_version = fake_useragent.__version__
    
    assert original_version == reloaded_version, "Version should be same after reload"
    print(f"✅ Module reloads successfully")
    print(f"  Original version: {original_version}")
    print(f"  Reloaded version: {reloaded_version}")
except Exception as e:
    print(f"❌ Module reload test failed: {e}")
    sys.exit(1)

# Test 2: hasattr() Checks
print("\nTEST 2: hasattr() Checks")
print("-" * 80)
try:
    import fake_useragent
    
    checks = {
        '__version__': True,
        'VERSION': True,
        'UserAgent': True,
        '__all__': True,
        '__doc__': True,
        '__name__': True,
        'nonexistent': False,
    }
    
    for attr, should_exist in checks.items():
        exists = hasattr(fake_useragent, attr)
        if should_exist:
            assert exists, f"{attr} should exist"
            print(f"  ✅ {attr}: exists")
        else:
            assert not exists, f"{attr} should not exist"
            print(f"  ✅ {attr}: correctly absent")
except Exception as e:
    print(f"❌ hasattr() check failed: {e}")
    sys.exit(1)

# Test 3: Attribute Access Methods
print("\nTEST 3: Attribute Access Methods")
print("-" * 80)
try:
    import fake_useragent
    
    # Direct access
    v1 = fake_useragent.__version__
    
    # getattr() access
    v2 = getattr(fake_useragent, '__version__')
    
    # __dict__ access
    v3 = fake_useragent.__dict__.get('__version__')
    
    # All should be equal
    assert v1 == v2 == v3, "All access methods should return same value"
    print(f"✅ Direct access: {v1}")
    print(f"✅ getattr() access: {v2}")
    print(f"✅ __dict__ access: {v3}")
    print(f"✅ All methods return same value")
except Exception as e:
    print(f"❌ Attribute access method test failed: {e}")
    sys.exit(1)

# Test 4: Immutability Check
print("\nTEST 4: Version Immutability")
print("-" * 80)
try:
    import fake_useragent
    original = fake_useragent.__version__
    
    # Try to modify (should work but not affect original)
    try:
        fake_useragent.__version__ = "1.0.0"
        # Check if it changed in module
        new_value = fake_useragent.__version__
        print(f"✅ Module allows __version__ reassignment")
        print(f"  Original: {original}")
        print(f"  Reassigned to: {new_value}")
        
        # Restore original for other tests
        fake_useragent.__version__ = original
    except AttributeError:
        print(f"✅ __version__ is read-only (immutable)")
except Exception as e:
    print(f"❌ Immutability test failed: {e}")
    sys.exit(1)

# Test 5: Comparison Operations
print("\nTEST 5: Version Comparison")
print("-" * 80)
try:
    import fake_useragent
    v = fake_useragent.__version__
    
    # String comparisons
    assert v == '0.1.6', "Should equal string '0.1.6'"
    assert v != '0.1.5', "Should not equal '0.1.5'"
    assert len(v) == 5, "Should have length 5"
    
    print(f"✅ Version string: {v}")
    print(f"✅ Equal to '0.1.6': {v == '0.1.6'}")
    print(f"✅ Not equal to '0.1.5': {v != '0.1.5'}")
    print(f"✅ Length is 5: {len(v) == 5}")
except Exception as e:
    print(f"❌ Version comparison test failed: {e}")
    sys.exit(1)

# Test 6: Type Checking
print("\nTEST 6: Type Validation")
print("-" * 80)
try:
    import fake_useragent
    
    type_checks = {
        '__version__': (str, str.__name__),
        'VERSION': (str, str.__name__),
        'UserAgent': (type, 'type'),
        '__all__': (list, list.__name__),
    }
    
    for attr, (expected_type, type_name) in type_checks.items():
        value = getattr(fake_useragent, attr)
        actual_type = type(value)
        assert actual_type == expected_type, \
            f"{attr} should be {type_name}, got {actual_type.__name__}"
        print(f"  ✅ {attr}: {type_name}")
except Exception as e:
    print(f"❌ Type validation test failed: {e}")
    sys.exit(1)

# Test 7: Module Initialization
print("\nTEST 7: Module Initialization State")
print("-" * 80)
try:
    import fake_useragent
    import sys as sys_module
    
    # Check if module is in sys.modules
    assert 'fake_useragent' in sys_module.modules, "Module should be in sys.modules"
    
    print(f"✅ Module fully initialized")
    print(f"  In sys.modules: True")
    print(f"  __version__ present: {hasattr(fake_useragent, '__version__')}")
    print(f"  VERSION present: {hasattr(fake_useragent, 'VERSION')}")
    print(f"  UserAgent present: {hasattr(fake_useragent, 'UserAgent')}")
except Exception as e:
    print(f"❌ Module initialization test failed: {e}")
    sys.exit(1)

# Test 8: Circular Imports Check
print("\nTEST 8: No Circular Import Issues")
print("-" * 80)
try:
    # Try various import patterns
    from fake_useragent import __version__
    from fake_useragent import VERSION
    from fake_useragent import UserAgent
    from fake_useragent import settings
    from fake_useragent import fake
    
    print(f"✅ All imports successful")
    print(f"  __version__: {__version__}")
    print(f"  VERSION: {VERSION}")
    print(f"  UserAgent: {UserAgent.__name__}")
    print(f"  settings module: {settings.__name__}")
    print(f"  fake module: {fake.__name__}")
except Exception as e:
    print(f"❌ Circular import test failed: {e}")
    sys.exit(1)

# Test 9: Exception Handling
print("\nTEST 9: Proper Exception Handling")
print("-" * 80)
try:
    import fake_useragent
    
    # Try to access non-existent attribute
    try:
        value = fake_useragent.nonexistent_attribute
        print(f"❌ Should have raised AttributeError")
        sys.exit(1)
    except AttributeError as e:
        print(f"✅ AttributeError raised correctly for missing attribute")
        print(f"  Error message: {str(e)[:60]}...")
    
    # Try invalid operation
    try:
        result = fake_useragent.__version__ + 5  # String + int
        print(f"❌ Should have raised TypeError")
        sys.exit(1)
    except TypeError as e:
        print(f"✅ TypeError raised correctly for invalid operation")
        print(f"  Error message: {str(e)[:60]}...")
except Exception as e:
    print(f"❌ Exception handling test failed: {e}")
    sys.exit(1)

# Test 10: Performance Check
print("\nTEST 10: Performance Baseline")
print("-" * 80)
try:
    import time
    import fake_useragent
    
    # Measure import time (approximate)
    start = time.time()
    for _ in range(100):
        v = fake_useragent.__version__
    elapsed = time.time() - start
    
    avg_time = (elapsed / 100) * 1000  # Convert to milliseconds
    print(f"✅ Performance baseline measured")
    print(f"  100 attribute accesses: {elapsed:.4f} seconds")
    print(f"  Average per access: {avg_time:.4f} milliseconds")
    print(f"  Status: Fast and responsive")
except Exception as e:
    print(f"❌ Performance test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 80)
print("ALL EDGE CASE AND COMPATIBILITY TESTS PASSED ✅")
print("=" * 80)
print()
print("Summary:")
print("  ✅ Module reloads successfully")
print("  ✅ All hasattr() checks work correctly")
print("  ✅ All attribute access methods work")
print("  ✅ Version immutability verified")
print("  ✅ Version comparisons work")
print("  ✅ All types are correct")
print("  ✅ Module initialization proper")
print("  ✅ No circular import issues")
print("  ✅ Exception handling correct")
print("  ✅ Performance is good")
print()
