fake-useragent — minimal reproduced project (fixed)

Overview
--------
This repository contains a minimal reproduction of the issue where
`fake_useragent` did not expose the standard `__version__` attribute.
A fix is provided that is PEP 396 compliant and preserves backward
compatibility with the legacy `VERSION` constant.

Quick-start
-----------
From the repository root:

python -m pytest tests/

Before (broken):

import fake_useragent
fake_useragent.VERSION        # works
hasattr(fake_useragent, '__version__')  # False (bug)

After (fixed):

import fake_useragent
fake_useragent.VERSION        # works
fake_useragent.__version__    # works and equals VERSION

License
-------
Example/demo code for a bug-fix task.