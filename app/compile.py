from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("find_primes",
    ["find_primes.py"],
    libraries=["m"],  #    Comment this line out on Windows
    extra_compile_args=["-ffast-math"]
    ),
]

setup(
    name = 'Find primes in range lib',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
