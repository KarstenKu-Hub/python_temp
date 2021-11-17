
"""
setuptools is used to build a python package.

- packages = find_packages(include=['temp_pyuq'])
  can be written to specify the files which will be exported

- for tests: 
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'  

- install_requires has all dependencies 
"""

from setuptools import find_packages, setup

setup(
    name='python_temp',
    packages=find_packages(),
    version='0.0.1',
    description='My first Python libary',
    author='Me',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)
