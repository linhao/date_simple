import pytest
import datetime
import date_simple as ds

def test_get_date_object():
    no_arg = datetime.date.today()
    dateobj1 = ds.get_date_object()
    assert no_arg == dateobj1

def test_get_date_object_arg(date='2018-02-26'):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    date_obj2 = ds.get_date_object(date='2018-02-26')
    assert date_obj == date_obj2

def test_get_date_string():
    date_str_no_arg = datetime.date.today().strftime('%Y-%m-%d')
    date_str1 = ds.get_date_string()
    assert date_str_no_arg == date_str1

def test_get_date_string_arg(date_object='2018-01-01'):
    date_str = datetime.datetime.strptime(date_object, '%Y-%m-%d').date()
    date_str = date_str.strftime('%Y-%m-%d')
    date_str2 = ds.get_date_string(date_object='2018-01-01')
    assert date_str == date_str2

def test_get_date_object_arg_badformat(date='bad date'):
    with pytest.raises(ValueError):
        ds.get_date_object('bad date')

def test_get_date_object_arg_notstring(date=123):
    with pytest.raises(TypeError):
        ds.get_date_object(123)

def test_get_date_string_arg_notdate(date_object='not_a_date_object'):
    with pytest.raises(ValueError):
        ds.get_date_string('not_a_date_object')