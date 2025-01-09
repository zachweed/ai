from setuptools import setup

setup(name='ai',
  version='0.2',
  description='I analyze things my author writes',
  url='http://github.com/zachweed/ai',
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
