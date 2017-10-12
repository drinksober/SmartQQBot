#!/usr/bin/python
import os
import sys
import shutil
from setuptools import setup
with open('src/__init__.py', 'r') as fd:
    VERSION = fd.readline().split('=')[-1].strip().strip("'")

if sys.argv[-1] == 'publish':
    if os.system("wheel version"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload -r pypi dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('paraer.egg-info')
    sys.exit()

README = """
qq webhook for github
Installation
From pip:
pip install qq_webhook
Project @ https://github.com/drinksober/qq_webhook
"""

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='qq_webhook',
    version=VERSION,
    install_requires=[
        'qqbot'
    ],
    packages=['src'],
    include_package_data=True,
    license='MIT',
    description='github webhook for qq',
    long_description=README,
    test_suite='tests',
    author='drinksober',
    author_email='drinksober@foxmail.com',
    url='https://github.com/drinksober/qq_webhook',
    zip_safe=False
)
