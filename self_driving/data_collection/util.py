import time


def get_date():
    """
    Gives you the date in form:
    year-month-day-hours-minutes-second
    :rtype: str
    """
    return time.strftime('%Y-%m-%d-%H-%-M-%S')
