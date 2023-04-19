from lesson_3.task_2 import convert_speed_to_kms
import pytest


@pytest.mark.parametrize(
    "speed_kmh, expected",
    [
        (1_079_252_848.8, 'Скорость света равна 299792 км/с.'),
        (3600, 'Скорость света равна 1 км/с.'),
        (279720.5, 'Скорость света равна 78 км/с.'),
    ]
)
def test_convert_speed_to_kms(speed_kmh, expected):
    msg = convert_speed_to_kms(speed_kmh)
    assert msg == expected
