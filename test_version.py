"""Test script to demonstrate Issue #40 - BEFORE FIX

This script shows that __version__ is NOT available in the package.
Only VERSION constant is available.
"""
import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fake_useragent

print("=" * 60)
print("Testing fake-useragent BEFORE FIX (Issue #40)")
print("=" * 60)

# Test 1: Check if VERSION exists
print("\nTest 1: Checking VERSION constant...")
try:
    version = fake_useragent.VERSION
    print(f"[OK] VERSION exists: {version}")
except AttributeError as e:
    print(f"[FAIL] VERSION not found: {e}")

# Test 2: Check if __version__ exists
print("\nTest 2: Checking __version__ attribute...")
try:
    version = fake_useragent.__version__
    print(f"[OK] __version__ exists: {version}")
except AttributeError as e:
    print(f"[FAIL] __version__ NOT FOUND (This is the problem!)")
    print(f"   Error: {e}")

# Test 3: Test basic functionality
print("\nTest 3: Testing basic UserAgent functionality...")
ua = fake_useragent.UserAgent()
print(f"[OK] Chrome UA: {ua.chrome[:50]}...")
print(f"[OK] Firefox UA: {ua.firefox[:50]}...")
print(f"[OK] Random UA: {ua.random[:50]}...")

print("\n" + "=" * 60)
print("SUMMARY: __version__ is missing - needs to be added!")
print("=" * 60)
