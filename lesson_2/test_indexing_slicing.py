# https://ru.hexlet.io/courses/python-numpy

from indexing_slicing import get_max_weekly, get_min_weekly, get_day_of_week_mean, get_placement_max_clicks  # noqa: E501

import numpy as np
import pytest


@pytest.fixture(scope='session')
def clicks():
    return np.array([
        [319, 265, 319, 328],
        [292, 274, 292, 301],
        [283, 301, 274, 283],
        [328, 364, 328, 319],
        [391, 355, 373, 337],
        [445, 418, 409, 445],
        [481, 400, 481, 409],
        [333, 267, 333, 344],
        [300, 278, 300, 311],
        [289, 311, 278, 289],
        [344, 388, 344, 333],
        [421, 377, 399, 355],
        [487, 454, 443, 487],
        [531, 432, 531, 443],
        [312, 264, 312, 320],
        [288, 272, 288, 296],
        [280, 296, 272, 280],
        [320, 352, 320, 312],
        [376, 344, 360, 328],
        [424, 400, 392, 424],
        [456, 384, 456, 392],
        [347, 269, 347, 360],
        [308, 282, 308, 321],
        [295, 321, 282, 295],
        [360, 412, 360, 347],
        [451, 399, 425, 373],
        [529, 490, 477, 529],
        [581, 464, 581, 477],
    ])


def test_get_max_weekly(clicks):
    assert get_max_weekly(clicks) == [481, 531, 456, 581]


def test_get_min_weekly(clicks):
    assert get_min_weekly(clicks) == [265, 267, 264, 269]


def test_get_day_of_week_mean(clicks):
    assert list(round(value) for value in get_day_of_week_mean(clicks)) == [315, 294, 289, 346, 379, 453, 469]  # noqa: E501


def test_get_placement_max_clicks(clicks):
    assert get_placement_max_clicks(clicks, 0) == 581
    assert get_placement_max_clicks(clicks, 1) == 490
    assert get_placement_max_clicks(clicks, 2) == 581
    assert get_placement_max_clicks(clicks, 3) == 529
