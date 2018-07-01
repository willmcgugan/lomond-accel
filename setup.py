from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet'
]

# http://bit.ly/2alyerp
with open('lomond_accel/_version.py') as f:
    exec(f.read())

with open('README.md') as f:
    long_desc = f.read()

extensions = [
    Extension('lomond_accel.mask', ['lomond_accel/_mask.pyx']),
    Extension('lomond_accel.utf8validator', ['lomond_accel/_utf8validator.pyx']),
]

setup(
    name='lomond-accel',
    packages=find_packages(),
    ext_modules=cythonize(extensions)
)
