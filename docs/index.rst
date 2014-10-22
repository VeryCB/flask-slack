Welcome to Flask-Slack's documentation!
=======================================

.. module:: Flask-Script

**Flask-Slack** is a Flask extension which makes it easy to interact with Slack slash commands.


Quickstart
----------
You can register your Slack slash command to a method as follows.
::

    from flask_slack import Slack


    slack = Slack(app)


    @slack.command('your_command', token='your_token',
                   team_id='your_team_id', methods=['POST'])
    def your_method(**kwargs):
        text = kwargs.get('text')
        return slack.response(text)

All registered methods are dispatched through ``slack.dispatch`` method. You can connect it to an endpoint which you wish Slack robots to request with.
::

    app.add_url_rule('/', view_func=slack.dispatch)


Installation
------------

You can install Flask-Slack with pip::

    $ pip install flask-slack

Or, with setuptools easy_install in case you didn't have pip::

    $ easy_install flask-slack


API Reference
-------------

.. toctree::
   :maxdepth: 2

   slack
   exceptions
