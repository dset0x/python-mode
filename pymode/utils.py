""" Pymode utils. """
import os.path
import sys
import threading
import warnings
from contextlib import contextmanager

import vim # noqa
from ._compat import StringIO, PY2


DEBUG = int(vim.eval('g:pymode_debug'))

warnings.filterwarnings('ignore')


@contextmanager
def silence_stderr():
    """ Redirect stderr. """
    if DEBUG:
        yield

    else:
        with threading.Lock():
            stderr = sys.stderr
            sys.stderr = StringIO()

        yield

        with threading.Lock():
            sys.stderr = stderr


def patch_paths(pylama=True, rope=True):
    """Patch `sys.path` with the libraries that we wish to use.

    :param pylama: Add pylama library to `sys.path`
    :param rope: Add rope library to `sys.path`
    """
    if pylama:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'libs',))

    print rope
    if rope:
        if PY2:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'libs2'))
        else:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'libs3'))
