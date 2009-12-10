"""
Tests to be run for tutoring
"""

from tutoring.tests.unit import *
from tutoring.tests.functional import *

__all__ = []

def __fill_all():
    import tutoring.tests.unit
    import tutoring.tests.functional
    __all__.extend(tutoring.tests.unit.__all__)
    __all__.extend(tutoring.tests.functional.__all__)

