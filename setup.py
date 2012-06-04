from os.path import join, dirname

from setuptools import setup, find_packages


NAME = 'pyserve'
MODULE = __import__(NAME)
README = 'README.rst'


setup(
    name=NAME,
    version=MODULE.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), README)).read(),
    include_package_data=True,
    install_requires=['Flask==0.8'],
    test_suite='tests'
)
