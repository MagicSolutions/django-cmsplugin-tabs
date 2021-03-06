# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

README = read('README.rst')

setup(
    name="django-cmsplugin-tabs",
    version="0.2.0",
    url='http://github.com/IndustriaTech/django-cmsplugin-tabs',
    description="Plugin for Django-CMS that create list of tabs (using jquery ui)",
    long_description=README,
    author='Venelin Stoykov',
    author_email='venelin@magicsolutions.bg',
    packages=[
        'cmsplugin_tabs',
        'cmsplugin_tabs.migrations',
        'cmsplugin_tabs.south_migrations',
    ],
    package_data={
        'cmsplugin_tabs': [
            'templates/cmsplugin_tabs/*',
            'locale/*/LC_MESSAGES/*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=1.4',
        'django-cms>=3.0',
        'djangocms-text-ckeditor>=2.4.1',
    ],
)
