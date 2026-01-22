"""Fake User Agent library - FIXED Version

This version properly exposes both __version__ and VERSION attributes.
Fix for Issue #40: Missing __version__ attribute.
"""
from __future__ import absolute_import, unicode_literals

from fake_useragent.fake import UserAgent  # noqa
# Import __version__ from settings and keep it as __version__
from fake_useragent.settings import __version__  # noqa

# Also expose VERSION for backward compatibility
# Both __version__ and VERSION point to the same value
VERSION = __version__
