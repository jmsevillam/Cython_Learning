from distutils.core import setup
from Cython.Build import cythonize

setup(name='Integration app',
      ext_modules=cythonize("integration.pyx"))

