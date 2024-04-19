# remove deprecate package, use setuptools instead
# from distutils.core import setup 
from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
# extensions = [
    # Extension(
    #     "sol01_cypp_cpdef_vector",
    #     sources=["sol01_cypp_cpdef_vector.pyx"],
    #     language="c++",
    #     include_dirs=["/usr/include"],
    # ),
    # Extension(
    #     "sol01_cypp_cpdef",
    #     sources=["sol01_cypp_cpdef.pyx"],
    #     language="c++",
    #     include_dirs=["/usr/include"],
    # ),
# ]
setup(
    ext_modules=cythonize(
        ["sol01_cypp_cpdef_vector.pyx", "sol01_cypp_cpdef.pyx"], compiler_directives={"language_level": "3"}
    )
)
