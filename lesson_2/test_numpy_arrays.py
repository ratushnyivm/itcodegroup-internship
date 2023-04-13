from numpy_arrays import make_click_numbers, get_range, get_mean, get_max_clicks_day, get_min_clicks_day  # noqa: E501
import random
import pytest


MIN_CLICKS = 1200
MAX_CLICKS = 2500


@pytest.fixture(scope='session')
def clicks():
    random.seed(42)
    return [random.randrange(MIN_CLICKS, MAX_CLICKS) for _ in range(365)]


def test_make_click_numbers(clicks):
    assert make_click_numbers(clicks).shape[0] == 365


def test_get_range(clicks):
    clicks_per_day = make_click_numbers(clicks)
    assert get_range(clicks_per_day) == 1297


def test_get_mean(clicks):
    clicks_per_day = make_click_numbers(clicks)
    assert pytest.approx(get_mean(clicks_per_day), rel=1e-3) == 1829


def test_get_max_clicks_day(clicks):
    clicks_per_day = make_click_numbers(clicks)
    assert get_max_clicks_day(clicks_per_day) == 363


def test_get_min_clicks_day(clicks):
    clicks_per_day = make_click_numbers(clicks)
    assert get_min_clicks_day(clicks_per_day) == 157
