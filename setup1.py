from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'example',
        ['example.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='example',
    version='0.0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A test project using pybind11',
    ext_modules=ext_modules,
)

