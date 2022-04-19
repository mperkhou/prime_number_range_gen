from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("find_primes",
    ["find_primes.py"],
    #libraries=["m"],  #    leave commented out on Windows. Uncomment on Linux
    extra_compile_args=["-ffast-math"]
    ),
]

setup(
    name = 'My factors lib',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
