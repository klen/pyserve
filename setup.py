from os.path import join, dirname

from setuptools import setup, find_packages


CURDIR = dirname(__file__)
NAME = 'pyserve'
MODULE = __import__(NAME)
README = join(CURDIR, 'README.rst')
REQUIREMENTS = open(join(CURDIR, 'requirements.txt')).readlines()
COMMANDS = ["%s = %s" % item for item in dict(
        serve='pyserve.main:main'
).items()]


setup(
    name=NAME,
    version=MODULE.__version__,
    license=MODULE.__license__,
    author=MODULE.__author__,
    author_email=MODULE.__email__,
    url=MODULE.__url__,
    packages=find_packages(),
    long_description=open(README).read(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points={'console_scripts': COMMANDS},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Environment :: Console',
        'Topic :: Software Development :: Code Generators',
    ],
    # test_suite='tests'
)
