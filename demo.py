r"""Please follow the standard of the ftw-tools as below, if you want to extend the tool packages"""


def demo_function(*args, **kwargs):
    r"""Illustration for the function.

    Args:
        args (type): Illustration.
        kwargs (type): Illustration.

    Returns:
        return items.
    """
    pass
    return None


class DemoClass:
    r"""Illustration for the class.

    Args:
        arg (type): Illustration.
        kwargs (type): Illustration.
    """

    def __init__(self, *args, **kwargs):
        self.attr = None

    def demo_method(self, *args, **kwargs):
        r"""Illustration for the method.

        Args:
            args (type): Illustration.
            kwargs (type): Illustration.

        Returns:
            return items.
        """
        self.attr = None
        return None
