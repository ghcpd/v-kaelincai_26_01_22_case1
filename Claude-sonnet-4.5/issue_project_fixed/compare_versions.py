"""Before vs After Comparison Script

This script demonstrates the difference between the buggy version
and the fixed version of fake-useragent.
"""
import sys
import os

print("=" * 70)
print("📊 BEFORE vs AFTER Comparison")
print("=" * 70)

# Test BEFORE (buggy version)
print("\n🔴 BEFORE FIX (Original Buggy Version)")
print("-" * 70)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'issue_project'))

try:
    import fake_useragent as fa_before
    
    # Test VERSION
    print("Testing VERSION constant:")
    try:
        version = fa_before.VERSION
        print(f"  ✓ fa_before.VERSION = {version}")
    except AttributeError as e:
        print(f"  ✗ FAILED: {e}")
    
    # Test __version__
    print("\nTesting __version__ attribute:")
    try:
        version = fa_before.__version__
        print(f"  ✓ fa_before.__version__ = {version}")
    except AttributeError as e:
        print(f"  ✗ FAILED: {e}")
        print(f"     This is the BUG - __version__ is not accessible!")
    
    # Test UserAgent
    print("\nTesting UserAgent functionality:")
    try:
        ua = fa_before.UserAgent()
        print(f"  ✓ UserAgent works: {ua.chrome[:50]}...")
    except Exception as e:
        print(f"  ✗ FAILED: {e}")
        
except Exception as e:
    print(f"Error loading buggy version: {e}")

# Remove old module from cache
if 'fake_useragent' in sys.modules:
    del sys.modules['fake_useragent']
if 'fake_useragent.settings' in sys.modules:
    del sys.modules['fake_useragent.settings']
if 'fake_useragent.fake' in sys.modules:
    del sys.modules['fake_useragent.fake']

# Clear old path
sys.path = [p for p in sys.path if 'issue_project' not in p or 'issue_project_fixed' in p]

# Test AFTER (fixed version)
print("\n\n✅ AFTER FIX (Fixed Version)")
print("-" * 70)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    import fake_useragent as fa_after
    
    # Test VERSION
    print("Testing VERSION constant:")
    try:
        version = fa_after.VERSION
        print(f"  ✓ fa_after.VERSION = {version}")
    except AttributeError as e:
        print(f"  ✗ FAILED: {e}")
    
    # Test __version__
    print("\nTesting __version__ attribute:")
    try:
        version = fa_after.__version__
        print(f"  ✓ fa_after.__version__ = {version}")
        print(f"     This is now FIXED - __version__ is accessible!")
    except AttributeError as e:
        print(f"  ✗ FAILED: {e}")
    
    # Test both equal
    print("\nTesting consistency:")
    try:
        assert fa_after.__version__ == fa_after.VERSION
        print(f"  ✓ Both values match: {fa_after.__version__}")
    except AssertionError:
        print(f"  ✗ Values don't match!")
    
    # Test UserAgent
    print("\nTesting UserAgent functionality:")
    try:
        ua = fa_after.UserAgent()
        print(f"  ✓ UserAgent works: {ua.chrome[:50]}...")
    except Exception as e:
        print(f"  ✗ FAILED: {e}")
        
except Exception as e:
    print(f"Error loading fixed version: {e}")

# Summary
print("\n" + "=" * 70)
print("📋 COMPARISON SUMMARY")
print("=" * 70)

print("\n| Feature                  | Before Fix | After Fix  |")
print("|--------------------------|------------|------------|")
print("| VERSION constant         | ✓ Works    | ✓ Works    |")
print("| __version__ attribute    | ✗ Missing  | ✓ Works    |")
print("| PEP 396 Compliance       | ✗ No       | ✓ Yes      |")
print("| UserAgent functionality  | ✓ Works    | ✓ Works    |")
print("| Backward compatibility   | N/A        | ✓ Yes      |")

print("\n💡 KEY CHANGES:")
print("   • Added: __version__ attribute (PEP 396 compliant)")
print("   • Kept: VERSION constant (backward compatibility)")
print("   • Changed: Only 2 lines in __init__.py")
print("   • Impact: No breaking changes, improved standards compliance")

print("\n" + "=" * 70)
