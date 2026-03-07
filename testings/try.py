import sys
import os

# Add the parent directory (SiftOutProject root) to the python path 
# so the IDE can find the `siftout` module when you run this script directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from siftout import Janitor 

cleaner = Janitor(extra_patterns=["*.bak"])
report = cleaner.self_destruct()
print(f"Cleaner Report: {report}") 

cleaner.secure_env()
print("Environment Secured")
