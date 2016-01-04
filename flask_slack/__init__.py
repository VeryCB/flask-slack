"""
    flask_slack
    ~~~~~~~~~~~~~~~

    Slack extension for Flask.

    :copyright: (c) 2014 by VeryCB.
    :license: BSD, see LICENSE for more details.
"""
from .slack import Slack
from .exceptions import SlackError
from .utils import link_string


__all__ = ['Slack', 'SlackError', 'link_string']
__version__ = '0.1.5'
__author__ = 'VeryCB <imcaibin@gmail.com>'
