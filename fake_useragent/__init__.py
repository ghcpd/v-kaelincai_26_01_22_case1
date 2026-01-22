"""Fake User Agent library - Before Fix (Issue #40)
这个版本没有 __version__ 属性，只有 VERSION
"""
from __future__ import absolute_import, unicode_literals

from fake_useragent.fake import UserAgent  # noqa
from fake_useragent.settings import __version__ as VERSION  # noqa
