import sys
import inspect
import numpy as np

sourceString = inspect.getsource(np.roll)

sys.stdout.write(sourceString)