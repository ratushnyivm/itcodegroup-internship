# https://ru.hexlet.io/courses/python-numpy

def get_max_weekly(clicks):
    return [
        clicks[monday:monday + 7].max() for monday in range(0, len(clicks), 7)
    ]


def get_min_weekly(clicks):
    return [
        clicks[monday:monday + 7].min() for monday in range(0, len(clicks), 7)
    ]


def get_day_of_week_mean(clicks):
    return [
        clicks[day::7].mean() for day in range(7)
    ]


def get_placement_max_clicks(clicks, platform_number):
    return clicks[:, platform_number].max()
