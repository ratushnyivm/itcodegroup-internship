# https://ru.hexlet.io/courses/python-numpy

import numpy as np


def make_click_numbers(input_click_numbers):
    return np.array(input_click_numbers)


def get_range(click_numbers):
    return click_numbers.max() - click_numbers.min()


def get_mean(click_numbers):
    return click_numbers.mean()


def get_max_clicks_day(click_numbers):
    return click_numbers.argmax() + 1


def get_min_clicks_day(click_numbers):
    return click_numbers.argmin() + 1
