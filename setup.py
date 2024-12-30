from setuptools import setup

setup(name='comms',
  version='0.1',
  description='I analyze things my author writes',
  url='http://github.com/zachweed/jint',
  author='Zach Weed',
  license='MIT',
  install_requires=[
  'nltk',
  'fire',
  'textblob',
  'transformers',
  'tensorflow',
  'tf_keras'
  ],
  zip_safe=False)
