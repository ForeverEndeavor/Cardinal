called = False


class TestCloseTooManyArgumentsPlugin:
    def close(self, cardinal, _):
        """This should never be hit due to wrong number of args."""
        global called
        called = True


def setup():
    return TestCloseTooManyArgumentsPlugin()
