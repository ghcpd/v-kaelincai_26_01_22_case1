"""Fake User Agent library - After Fix (Issue #40)
这个版本同时提供 __version__ 属性和 VERSION 常量
"""
from __future__ import absolute_import, unicode_literals

from fake_useragent.fake import UserAgent  # noqa
from fake_useragent.settings import __version__  # noqa - Import __version__ directly for PEP 396 compliance
from fake_useragent.settings import __version__ as VERSION  # noqa - Keep backward compatibility