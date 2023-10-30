
"https://stackoverflow.com/questions/16981921/relative-imports-in-python-3"

# For relative imports to work in Python 3.6

import os, sys

path = os.path.dirname(os.path.realpath(__file__))
print(path)

sys.path.append(path)