|Build Status| |Coverage Status| |PyPI Version| |PyPI Downloads|

Flask-Slack
============

Flask-Slack is a Flask extension which makes it easy to interact with Slack slash commands.


Installation
------------

You can install Flask-Slack with pip::

    $ pip install flask-slack

Or, with setuptools easy_install in case you didn't have pip::

    $ easy_install flask-slack


Usage
-----
::

    from flask_slack import Slack


    slack = Slack(app)
    app.add_url_rule('/', view_func=slack.dispatch)


    @slack.command('your_command', token='your_token',
                   team_id='your_team_id', methods=['POST'])
    def your_method(**kwargs):
        text = kwargs.get('text')
        return slack.response(text)


Documentation
-------------
The full documentation is available at `readthedocs.org <http://flask-slack.readthedocs.org>`_


.. |Build Status| image:: https://travis-ci.org/VeryCB/flask-slack.svg?branch=master
   :target: https://travis-ci.org/VeryCB/flask-slack
   :alt: Build Status
.. |PyPI Version| image:: https://img.shields.io/pypi/v/Flask-Slack.svg
   :target: https://pypi.python.org/pypi/Flask-Slack
   :alt: PyPI Version
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/Flask-Slack.svg
   :target: https://pypi.python.org/pypi/Flask-Slack
   :alt: Downloads
.. |Coverage Status| image:: https://img.shields.io/coveralls/VeryCB/flask-slack.svg
   :target: https://coveralls.io/r/VeryCB/flask-slack
   :alt: Coverage Status
