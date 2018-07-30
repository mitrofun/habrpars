import locale

import calendar
from datetime import datetime, timedelta

locale.setlocale(locale.LC_ALL, 'ru_RU')


def _normalize_date_from_date_in_words(date_in_words):
    if not date_in_words:
        return ''
    today = datetime.today().date()
    tomorrow = today - timedelta(days=1)
    date_text = date_in_words.split(' ')[:1][0]
    humanize_date_dicts = {'сегодня': today, 'вчера': tomorrow}
    if date_text in humanize_date_dicts.keys():
        date = humanize_date_dicts[date_text]
        return date
    return ''


def _normalize_date_from_date_with_month_without_year(date_with_month_without_year):
    if not date_with_month_without_year:
        return ''
    date_list = date_with_month_without_year.split(' ')[:2]
    day = int(date_list[0])
    month_name = date_list[1]
    month_name_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
    try:
        month = month_name_to_num[month_name]
        if month:
            return datetime(day=day, month=month, year=datetime.now().year).date()
    except KeyError:
        pass
    return ''


def _normalize_date_from_date_with_month_and_year(date_with_month_and_year):
    if not date_with_month_and_year:
        return ''
    date_time_list = date_with_month_and_year.split(' ')
    year = int(date_time_list.pop(2))
    date_with_month_without_year = ' '.join(date_time_list)
    date_in_current_year = _normalize_date_from_date_with_month_without_year(
        date_with_month_without_year)
    if date_in_current_year:
        return date_in_current_year.replace(year=year)
    return ''


def normalize_date(humanize_date):
    """
    Format date and time examples:
    'сегодня в hh:mm',
    'вчера в hh:mm',
    'dd month_ru в hh:mm',
    'dd month_ru yyyy в hh:mm
    """
    if not humanize_date:
        return ''
    date = ''
    if len(humanize_date.split(' ')) == 3:
        date = _normalize_date_from_date_in_words(humanize_date)
    if len(humanize_date.split(' ')) == 4:
        date = _normalize_date_from_date_with_month_without_year(humanize_date)
    if len(humanize_date.split(' ')) == 5:
        date = _normalize_date_from_date_with_month_and_year(humanize_date)
    return date


def get_first_date_in_week(week_string):
    """Return date for sending string with year and week number, like '2018-W20' """
    return datetime.strptime(week_string + '-1', "%Y-W%W-%w")


def get_last_date_in_week(first_date_week):
    return first_date_week + timedelta(6)


def date_to_string(date):
    return date.date().isoformat()
