"""Fake User Agent library - After Fix

This version properly exposes the __version__ attribute following PEP 396.
The __version__ attribute is now accessible at the module level, while maintaining
backward compatibility with the VERSION constant.
"""
from __future__ import absolute_import, unicode_literals

from fake_useragent.fake import UserAgent  # noqa
from fake_useragent.settings import __version__  # noqa

# Maintain backward compatibility with old code using VERSION
VERSION = __version__

# Expose public API
__all__ = ['UserAgent', '__version__', 'VERSION']
