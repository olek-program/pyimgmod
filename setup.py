from setuptools import setup, find_packages

VERSION = '0.0.01'
DESCRIPTION = 'Generating random imagaes and manipulating it'
LONG_DESCRIPTION = 'Library for python with this library you can generate random images and modify it'

setup(
    name="pyimgen",
    version=VERSION,
    author="Lemskyy (olek-program)",
    author_email="<lemskyyyt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pypng'],
    keywords=['python', 'pypng', 'png', 'images'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)