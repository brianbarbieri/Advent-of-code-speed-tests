from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='day 17',
    ext_modules=cythonize("solution_1_cython.pyx"),
    zip_safe=False,
    include_dirs=[numpy.get_include()]
)

# python3 setup.py build_ext --inplace