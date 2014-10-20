"""
    flask_slack
    ~~~~~~~~~~~~~~~

    Slack extension for Flask.

    :copyright: (c) 2014 by VeryCB.
    :license: BSD, see LICENSE for more details.
"""
from .slack import Slack
from .exceptions import SlackError


__all__ = ['Slack', 'SlackError']
__version__ = '0.1.2'
__author__ = 'VeryCB <imcaibin@gmail.com>'
