# Copyright (C) 2009 Abhishek Mukherjee <abhishek.mukher.g@gmail.com>
#
# This file is part of rtutor.
#
# rtutor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rtutor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rtutor.  If not, see <http://www.gnu.org/licenses/>.

try:
    from distribute_setup import use_setuptools
except ImportError:
    pass
else:
    use_setuptools()

from setuptools import setup, find_packages

setup(name="rtutor",
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Lnguage :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Communications',
            'Topic :: Education',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        packages=find_packages(),
        install_requires=[
            'django',
            'django_cas',
            'django-evolution',
        ],
        extras_require={
            'FastCGI': ['flup'],
        },
        dependency_links = [
            'http://django-evolution.googlecode.com/svn/trunk/',
        ],
        test_suite='rtutor.runtests.runtests',
)

