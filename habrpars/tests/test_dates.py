from datetime import datetime, timedelta

from dates import (
    normalize_date,
    _normalize_date_from_date_in_words,
    _normalize_date_from_date_with_month_without_year,
    _normalize_date_from_date_with_month_and_year,
    get_first_date_in_week,
    get_last_date_in_week,
    date_to_string
)


def test_normalize_date_from_date_in_words():
    today = datetime.now().date()
    assert _normalize_date_from_date_in_words('сегодня в 12:20') == today
    assert _normalize_date_from_date_in_words('вчера в 14:08') == today - timedelta(days=1)
    assert _normalize_date_from_date_in_words('просто в 17:30') == ''


def test_normalize_date_from_date_with_month_without_year():
    today = datetime.now().date()
    assert _normalize_date_from_date_with_month_without_year('18 июля в 12:30') == datetime(
        year=today.year, month=7, day=18).date()
    assert _normalize_date_from_date_with_month_without_year('18 снежника в 12:30') == ''
    assert _normalize_date_from_date_with_month_without_year('') == ''


def test_normalize_date_from_date_with_month_and_year():
    assert _normalize_date_from_date_with_month_and_year('19 июня 2014 в 04:41') == datetime(
        year=2014, month=6, day=19).date()
    assert _normalize_date_from_date_with_month_and_year('11 травеня 1700 в 11:30') == ''
    assert _normalize_date_from_date_with_month_and_year('') == ''


def test_normalize_date():
    today = datetime.now().date()
    assert normalize_date('') == ''
    assert normalize_date('сегодня в 12:20') == today
    assert normalize_date('вчера в 14:08') == today - timedelta(days=1)
    assert normalize_date('18 июля в 12:30') == datetime(year=today.year, month=7, day=18).date()
    assert normalize_date('19 июня 2014 в 04:41') == datetime(year=2014, month=6, day=19).date()


def test_get_first_date_in_week():
    assert get_first_date_in_week('2018-W01').date() == datetime(year=2018, month=1, day=1).date()
    assert get_first_date_in_week('2018-W31').date() == datetime(year=2018, month=7, day=30).date()


def test_get_last_date_in_week():
    assert get_last_date_in_week(datetime(year=2018, month=1, day=1).date()) == datetime(
        year=2018, month=1, day=7).date()


def test_date_to_string():
    assert date_to_string(datetime(year=2018, month=1, day=1)) == '2018-01-01'
    assert date_to_string(datetime(year=2018, month=12, day=6)) == '2018-12-06'
