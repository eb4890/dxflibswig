#!/usr/bin/env python


from distutils.core import setup, Extension


dxflib_module = Extension('_dxflib',
                           sources=['src/dxflib.i','src/dl_dxf.cpp',"src/dl_creationadapter.cxx" , 'src/dl_writer_ascii.cpp'],
                           swig_opts = ['-c++', "-Wall"]
                           )

setup (name = 'dxflib',
       version = '0.1',
       author      = "Will Pearson",
       description = """Swig binding for dxflib""",
       ext_modules = [dxflib_module],

       py_modules = ["dxflib"],
       packages = [''],
       package_dir = {'': 'src'},
       install_path = 'dxflib'
       )

