import os
import re

from setuptools import setup


def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as f:
        return f.read()


content = fread('flask_slack.py')
m = re.findall(r'__version__\s*=\s*\'(.*)\'', content)
version = m[0]


setup(
    name='Flask-Slack',
    version=version,
    url='https://github.com/verycb/flask-slack',
    author='VeryCB',
    author_email='imcaibin@gmail.com',
    description='Slack extension for Flask.',
    long_description=fread('README.rst'),
    license='BSD',
    py_modules=['flask_slack'],
    zip_safe=False,
    platforms='any',
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
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
