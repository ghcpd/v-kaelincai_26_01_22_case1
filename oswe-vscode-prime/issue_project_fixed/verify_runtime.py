"""Runtime verification script for issue_project_fixed
Runs the same checks from the task brief and prints concise results.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fake_useragent

print("RUNTIME VERIFICATION — issue_project_fixed")
print("package path:", os.path.dirname(fake_useragent.__file__))
print("__version__:", fake_useragent.__version__)
print("VERSION:", fake_useragent.VERSION)
print("versions_equal:", fake_useragent.__version__ == fake_useragent.VERSION)

ua = fake_useragent.UserAgent()
print("sample_chrome:", ua.chrome[:60])
print("sample_firefox:", ua.firefox[:60])
print("sample_random:", ua.random[:60])
print("OK: runtime checks completed")
