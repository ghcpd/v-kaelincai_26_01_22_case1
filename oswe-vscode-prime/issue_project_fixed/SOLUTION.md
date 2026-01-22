Problem
=======
The package exposed a `VERSION` constant by importing
`__version__` from `settings` as `VERSION`, but it did not
export the canonical `__version__` name at the package top-level.

Root cause
==========
In `fake_useragent.__init__` the code performed:

from fake_useragent.settings import __version__ as VERSION

which defines `VERSION` but never binds `__version__` in the
package namespace. Tools and users that expect `package.__version__`
(PEP 396) therefore fail.

Solution
========
- Export `__version__` from `fake_useragent.__init__` by importing
  the value from `settings` and also aliasing `VERSION = __version__`.
- Keep `settings.__version__` as the single source of truth.
- Add tests that assert both names exist and are equal.

Rationale and alternatives
==========================
- Minimal change: only the package entry point was modified.
- Alternative: read version from a single file (e.g. _version.py) or use
  importlib.metadata for distribution metadata — unnecessary here.

Impact
======
- Restores PEP 396 compatibility.
- Backward compatible: `VERSION` continues to work.
- No behavioral changes to `UserAgent`.

How to verify
=============
- Run `pytest tests/` — all tests should pass.
- Import the package and check `__version__` and `VERSION` equality.