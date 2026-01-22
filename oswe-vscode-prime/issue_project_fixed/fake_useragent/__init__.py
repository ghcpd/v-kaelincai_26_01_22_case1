"""Fake User Agent - fixed entry point (PEP 396 compliant)

Expose a standard `__version__` attribute while keeping the
legacy `VERSION` name for backward compatibility.
"""
from __future__ import absolute_import, unicode_literals

# Re-export core API
from .fake import UserAgent  # noqa: F401

# Import the canonical version from settings (do NOT redefine it here)
from .settings import __version__ as __version__  # PEP 396: provide __version__

# Keep the historical constant for backward compatibility
VERSION = __version__

# Public API
__all__ = ["UserAgent", "__version__", "VERSION"]
