from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='genimg',
  version='0.0.1',
  description='Library for generating  images and modify it',
  long_description='This library can generate imaages and can modify it this is version in programming',
  url='',  
  author='Lemskyy',
  author_email='lemskyyyt@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='python images generator modyfier',
  packages=find_packages(),
  install_requires=['pypng'] 
)