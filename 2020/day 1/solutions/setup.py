from setuptools import setup
from Cython.Build import cythonize

setup(
    name='solution 1',
    ext_modules=cythonize("solution_1_cython.pyx"),
    zip_safe=False,
)
