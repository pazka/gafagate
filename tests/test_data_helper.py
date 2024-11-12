import pytest
from datetime import date
from data_process.data_helper import DataHelper 

def test_initialization():
    data = [
        (date(2018, 1, 1), 10.0),
        (date(2020, 6, 1), 20.0),
        (date(2021, 6, 1), 30.0),
        (date(2023, 6, 1), 40.0)
    ]
    helper = DataHelper(data)

    assert helper.min_date == date(2018, 1, 1)
    assert helper.max_date == date(2023, 6, 1)
    assert helper.min_value == 10.0
    assert helper.max_value == 40.0

def test_get_value():
    data = [
        (date(2020, 6, 1), 20.0),
        (date(2021, 6, 1), 30.0)
    ]
    helper = DataHelper(data)

    assert helper.get_value(date(2020, 6, 1)) == 20.0
    assert helper.get_value(date(2021, 6, 1)) == 30.0
    assert helper.get_value(date(2019, 1, 1)) is None

def test_to_uv():
    data = [
        (date(2020, 6, 1), 20.0),
        (date(2021, 6, 1), 30.0),
        (date(2022, 6, 1), 40.0)
    ]
    helper = DataHelper(data)

    assert helper.to_uv((date(2020, 6, 1), 20.0)) == 0.0
    assert helper.to_uv((date(2022, 6, 1), 40.0)) == 1.0
    assert helper.to_uv((date(2021, 6, 1), 30.0)) == 0.5

def test_filter_dates():
    data = [
        (date(2018, 1, 1), 10.0),
        (date(2020, 6, 1), 20.0),
        (date(2021, 6, 1), 30.0),
        (date(2023, 6, 1), 40.0)
    ]
    helper = DataHelper(data)
    helper.filter_dates(date(2020, 1, 1), date(2021, 12, 31))

    assert len(helper.data) == 2
    assert helper.min_date == date(2020, 6, 1)
    assert helper.max_date == date(2021, 6, 1)

def test_clamp_values():
    data = [
        (date(2020, 6, 1), 20.0),
        (date(2021, 6, 1), 30.0),
        (date(2022, 6, 1), 40.0)
    ]
    helper = DataHelper(data)
    helper.clamp_values(25.0, 35.0)

    assert helper.data == [
        (date(2020, 6, 1), 25.0),
        (date(2021, 6, 1), 30.0),
        (date(2022, 6, 1), 35.0)
    ]
    assert helper.min_value == 25.0
    assert helper.max_value == 35.0
