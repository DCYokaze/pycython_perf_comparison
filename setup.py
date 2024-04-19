# remove deprecate package, use setuptools instead
# from distutils.core import setup 
from setuptools import setup
from Cython.Build import cythonize
pyx_files = [
    "sol01_pure_python_cy.pyx",
    "sol01_cy_cpdef.pyx",
    # "yet_another_file.pyx"
]
setup(
    ext_modules=cythonize(
        pyx_files, compiler_directives={"language_level": "3"}
    )
)