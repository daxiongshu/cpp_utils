from setuptools import Extension, setup, find_packages

try:
    from Cython.Build import cythonize
except ImportError:
    # create closure for deferred import
    def cythonize(*args, ** kwargs):
        from Cython.Build import cythonize
        return cythonize(*args, ** kwargs)

setup(
    name="cpp_utils",
    author='jiwei',
    setup_requires=[
        'cython',
    ],
    ext_modules=cythonize([
        Extension(
            'cpp_utils',
            sorted(['python/session.pyx','cpp/src/session.cpp']),
            include_dirs=[
                # c/cpp defination includes folder path
                'cpp/include'
            ],
            extra_link_args=[],  # like '-lX11'
            language='c++'
        ),
        
    ]
    ),
    zip_safe=False,
)
