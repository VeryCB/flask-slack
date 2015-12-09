import os

from setuptools import setup


def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as f:
        return f.read()


setup(
    name='Flask-Slack',
    version='0.1.3',
    url='https://github.com/verycb/flask-slack',
    author='VeryCB',
    author_email='imcaibin@gmail.com',
    description='Slack extension for Flask.',
    long_description=fread('README.rst'),
    license='BSD',
    py_modules=['flask_slack'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'six',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
