try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
from codecs import open
import os

reboundxfmodule = Extension('reboundxf',
                    sources = [ 'cext/libreboundxf.c',
                                ],
                    define_macros=[ ('COLLISIONS_NONE',None) ],
                    extra_compile_args=['-fstrict-aliasing', '-O3','-std=c99','-march=native'],
                                    )

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='reboundxf',
    version='0.0.1',
    description='A library for including additional forces in REBOUND',
    long_description=long_description,
    url='http://github.com/dtamayo/reboundxf',
    author='Daniel Tamayo',
    author_email='tamayo.daniel@gmail.com',
    license='GPL',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='astronomy astrophysics nbody integrator',
    packages=['reboundxf'],
    install_requires=[],
    ext_modules = [reboundxfmodule],
    zip_safe=False)
