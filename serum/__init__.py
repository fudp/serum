from abc import abstractmethod, abstractstaticmethod, abstractclassmethod

from ._dependency import *
from ._environment import *
from ._functions import *
from ._inject import *


def load_ipython_extension(_):
    try:
        from ipython_environment import environment
        environment.__enter__()
    except ModuleNotFoundError:
        pass


def unload_ipython_extension(_):
    try:
        from ipython_environment import environment
        environment.__exit__(None, None, None)
    except ModuleNotFoundError:
        pass
