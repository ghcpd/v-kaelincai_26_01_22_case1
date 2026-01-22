"""
Simple Test Runner - Windows Compatible
No Unicode characters to avoid encoding issues
"""
import sys
import os

# Add the fixed package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("FAKE-USERAGENT FIX - FINAL VERIFICATION")
print("=" * 70)

success = True

# Test 1: Import
print("\n[TEST 1] Importing fake_useragent...")
try:
    import fake_useragent
    print("PASS - Module imported successfully")
except Exception as e:
    print(f"FAIL - {e}")
    success = False

# Test 2: __version__ exists
print("\n[TEST 2] Checking __version__ attribute...")
try:
    assert hasattr(fake_useragent, '__version__')
    print(f"PASS - __version__ = {fake_useragent.__version__}")
except AssertionError:
    print("FAIL - __version__ attribute not found")
    success = False

# Test 3: VERSION exists
print("\n[TEST 3] Checking VERSION constant...")
try:
    assert hasattr(fake_useragent, 'VERSION')
    print(f"PASS - VERSION = {fake_useragent.VERSION}")
except AssertionError:
    print("FAIL - VERSION constant not found")
    success = False

# Test 4: Values match
print("\n[TEST 4] Checking values match...")
try:
    assert fake_useragent.__version__ == fake_useragent.VERSION
    print(f"PASS - Both equal to {fake_useragent.__version__}")
except AssertionError:
    print("FAIL - Values don't match")
    success = False

# Test 5: Correct version
print("\n[TEST 5] Checking version number...")
try:
    assert fake_useragent.__version__ == '0.1.6'
    print("PASS - Version is 0.1.6")
except AssertionError:
    print("FAIL - Unexpected version number")
    success = False

# Test 6: UserAgent works
print("\n[TEST 6] Testing UserAgent functionality...")
try:
    ua = fake_useragent.UserAgent()
    chrome = ua.chrome
    firefox = ua.firefox
    random_ua = ua.random
    
    assert isinstance(chrome, str) and len(chrome) > 0
    assert isinstance(firefox, str) and len(firefox) > 0
    assert isinstance(random_ua, str) and len(random_ua) > 0
    
    print("PASS - UserAgent works correctly")
    print(f"  Chrome: {chrome[:50]}...")
    print(f"  Firefox: {firefox[:50]}...")
except Exception as e:
    print(f"FAIL - {e}")
    success = False

# Test 7: Import patterns
print("\n[TEST 7] Testing import patterns...")
try:
    from fake_useragent import UserAgent
    from fake_useragent import __version__
    from fake_useragent import VERSION
    
    test_ua = UserAgent()
    assert test_ua is not None
    assert __version__ == '0.1.6'
    assert VERSION == '0.1.6'
    
    print("PASS - All import patterns work")
except Exception as e:
    print(f"FAIL - {e}")
    success = False

# Summary
print("\n" + "=" * 70)
if success:
    print("SUCCESS! All tests passed!")
    print("=" * 70)
    print("\nSummary:")
    print("  - __version__ attribute: AVAILABLE")
    print("  - VERSION constant: AVAILABLE")
    print("  - Values match: YES")
    print("  - Version: 0.1.6")
    print("  - PEP 396 compliant: YES")
    print("  - Backward compatible: YES")
    print("  - UserAgent works: YES")
    print("\nThe fix is complete and working perfectly!")
    sys.exit(0)
else:
    print("FAILURE! Some tests failed.")
    print("=" * 70)
    sys.exit(1)
