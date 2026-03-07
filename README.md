# Siftout

A smart, automated workspace cleaner and security hardener for Python projects.

## Installation

```bash
pip install siftout
```

## Usage

```python
from siftout import Janitor

# Instantiate the cleaner (can provide extra file extensions if desired)
cleaner = Janitor(extra_patterns=["*.bak"])

# Clean the workspace
stats = cleaner.self_destruct()
print(stats)
```
