from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Generating and modyfing inages'
LONG_DESCRIPTION = 'A package that allows generate images with numbers, letters and modify the inages'



# Setting up
setup(
    package_dir = {"": "src"},
    packages=['imgen'],
    name="pyimgmod",
    version=VERSION,
    author="Lemskyy (olek-program)",
    author_email="<lemskyyyt+projects@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=find_packages(),
    install_requires=['pypng'],
    keywords=['python', 'image', 'py', 'png', 'library'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)