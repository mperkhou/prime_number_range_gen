from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("find_primes",
    ["find_primes.py"],
    extra_compile_args=["-ffast-math"]
    ),
]

setup(
    name = 'My tools lib',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
