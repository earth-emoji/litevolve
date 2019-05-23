from collections import OrderedDict

def get_progress(goal, completed):
    try:
        progress = completed / goal
    except ZeroDivisionError:
        progress = 0
    percent = progress * 100

    return percent

