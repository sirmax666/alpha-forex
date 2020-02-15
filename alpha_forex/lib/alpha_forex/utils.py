# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------
# Author: Maxime Sirois
# -----------------------------------------------------------------------------
"""
"""
# -----------------------------------------------------------------------------


from datetime import datetime


def now(fmt='%Y-%m-%d %H:%M:%S'):
    """Function that gives the current timestamp

    Current timestamp given by the operating system.

    Args:
        fmt (str): The timestamp format you which to output the timestamp.

    Returns:
        str: The current timestamp
    """
    return datetime.now().strftime(fmt)
