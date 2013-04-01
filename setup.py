from os.path import join, dirname

from setuptools import setup, find_packages # nolint


CURDIR = dirname(__file__)
NAME = 'pyserve'
MODULE = __import__(NAME)
README = join(CURDIR, 'README.rst')
REQUIREMENTS = open(join(CURDIR, 'requirements.txt')).readlines()
COMMANDS = ['pyserve = pyserve.main:main']


setup(
    name=NAME,
    version=MODULE.__version__,
    license=MODULE.__license__,
    author=MODULE.__author__,
    author_email=MODULE.__email__,
    url=MODULE.__url__,
    description='Serve local dirs.',
    long_description=open(README).read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points={'console_scripts': COMMANDS},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', # nolint
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Environment :: Console',
        'Topic :: Software Development :: Code Generators',
    ],
    test_suite='tests',
    tests_require='webtest',
)
