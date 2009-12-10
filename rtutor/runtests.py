"""
This file mainly exists to allow python setup.py test to work.
"""

import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'rtutor.settings'
TEST_DIR = os.path.dirname(__file__)
sys.path.insert(0, TEST_DIR)

from django.test.utils import get_runner
from django.conf import settings


def runtests():
    test_runner = get_runner(settings)
    failures = test_runner([], verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
