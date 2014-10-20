class SlackError(Exception):
    """Base Slack Exception"""

    def __init__(self, msg):
        """Return error message to user

        :param msg: the error message to return
        """
        self.msg = msg
