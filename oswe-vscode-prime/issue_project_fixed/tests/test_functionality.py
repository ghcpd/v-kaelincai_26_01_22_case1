"""Core functionality tests for UserAgent (non-regressive)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fake_useragent import UserAgent


def test_useragent_properties_return_strings_and_known_values():
    ua = UserAgent()

    c = ua.chrome
    assert isinstance(c, str)
    assert 'Mozilla' in c
    assert c in ua.data['chrome']

    f = ua.firefox
    assert isinstance(f, str)
    assert 'Mozilla' in f
    assert f in ua.data['firefox']

    r = ua.random
    assert isinstance(r, str)
    assert r in (ua.data['chrome'] + ua.data['firefox'])
