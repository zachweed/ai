from setuptools import setup

setup(name='jint',
  version='0.1',
  description='I analyze things my author writes',
  url='http://github.com/zachweed/jint',
  author='Zach Weed',
  license='MIT',
  install_requires=[
  'nltk',
  'fire',
  'textblob'
  ],
  zip_safe=False)
