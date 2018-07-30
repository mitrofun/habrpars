import sys

import os

import re

import requests
import argparse
import collections
import pymorphy2

import logging.config

from bs4 import BeautifulSoup

from .console import Colors
from .dates import (normalize_date, get_first_date_in_week, get_last_date_in_week, date_to_string)
from .helpers import timed, flat_list, get_max_len_word, get_max_len_number


URL = 'https://habr.com/all/'
PAGE_START = 1
PAGE_COUNT = 10
TOP_SIZE = 5

DEBUG = os.environ.get('DEBUG') == 'true'

if DEBUG:
    logging.config.fileConfig('log.conf')

logger = logging.getLogger(__name__)


def fetch_request(page_number, url=URL):
    try:
        if page_number:
            url += f'page{page_number}/'
        return requests.get(url).text
    except requests.exceptions.ConnectionError:
        print('Error.Check connection to internet.')
        return ''


def fetch_raw_text(url=URL, start_page=PAGE_START, page_count=PAGE_COUNT):
    start_page_number = start_page if start_page < 100 else 100
    end_page_number = start_page + page_count if (start_page + page_count) < 101 else 101
    raw_pages = []
    for page_number in range(start_page_number, end_page_number):
        page_text = fetch_request(page_number, url)
        if page_text:
            raw_pages.append(page_text)
    return raw_pages


def parse_args():
    """
    Get arguments from the command line
    :return: args from console
    """
    help_text = """
    Analyzer of the frequency of use of nouns in the headings of posts on hubr.com
    """
    parser = argparse.ArgumentParser(
        description=help_text
    )
    parser.add_argument(
        '-p',
        '--pages',
        type=int,
        dest='page_count',
        default=PAGE_COUNT,
        help=f'Number of pages to parse, default is {PAGE_COUNT}.'
    )
    parser.add_argument(
        '-s',
        '--start',
        type=int,
        default=PAGE_START,
        dest='start_page',
        help=f'Start page number, default is {PAGE_START}.',
    )
    parser.add_argument(
        '-t',
        '--top',
        type=int,
        default=TOP_SIZE,
        dest='top_size',
        help=f'The size of the top noun, default is {TOP_SIZE}.',
    )

    return parser.parse_args()


def parse_raw_text(raw_text):
    soup = BeautifulSoup(raw_text, 'html.parser')
    return soup


def clean_text(text):
    reg = re.compile('[^а-яА-Я ]')
    return reg.sub('', text)


def scraping_html(html):
    posts_title_and_dates_list = []
    for node_post in html.find_all('article'):
        post_title = node_post.find('a', {'class': 'post__title_link'}).text
        post_humanize_date = node_post.find('span', {'class': 'post__time'}).text
        clear_post_title = clean_text(post_title)
        post_date = normalize_date(post_humanize_date)
        posts_title_and_dates_list.append((clear_post_title, post_date))
        logger.debug(f'Post title: {post_title} | Post date: {post_humanize_date}')
    return posts_title_and_dates_list


def normalize_words(words):
    morph = pymorphy2.MorphAnalyzer()
    words_normal = []
    for word in words:
        parse_word = morph.parse(word)[0]
        if 'NOUN' in parse_word.tag:
            words_normal.append(parse_word.normal_form)
    return words_normal


def get_words_on_date(posts):
    words_on_date = {}
    for post in posts:
        post_title = post[0]
        post_date = post[1]
        number_week = f'{post_date.year}-W{post_date.isocalendar()[1]}'
        if number_week in words_on_date:
            words_on_date[number_week] += post_title.lower().split(' ')
        else:
            words_on_date[number_week] = post_title.lower().split(' ')
    return words_on_date


@timed
def main():
    args = parse_args()
    raw_texts = fetch_raw_text(URL, args.start_page, args.page_count)
    posts = []
    for raw_text in raw_texts:
        humanize_html = parse_raw_text(raw_text)
        post_info = scraping_html(humanize_html)
        posts += post_info
    words_on_date = get_words_on_date(posts)

    # console
    sys.stdout.write(Colors.BOLD + Colors.HEADER)
    print('=' * 80)
    sys.stdout.write(Colors.ENDC)
    sys.stdout.write(Colors.BOLD)
    print(f'Count pages have been parsed: {args.page_count}')
    print(f'Total count weeks: {len(words_on_date)}')
    print(f'Top: {args.top_size}')
    for week in words_on_date:
        words_normal_form = normalize_words(words_on_date[week])
        words_collection = collections.Counter(words_normal_form).most_common(args.top_size)
        first_day_week = get_first_date_in_week(week)
        last_day_week = get_last_date_in_week(first_day_week)
        week_name = f'week: ' \
                    f'{date_to_string(first_day_week)} - ' \
                    f'{date_to_string(last_day_week)}'
        weak_name_len = len(week_name)
        offset = int((80 - weak_name_len) / 2)
        sys.stdout.write(Colors.BOLD + Colors.GREEN)
        print('-' * offset, week_name, '-' * (offset - 1))
        sys.stdout.write(Colors.ENDC)
        sys.stdout.write(Colors.BOLD)
        flat_words_collection = flat_list(words_collection)
        max_len_word = get_max_len_word(flat_words_collection)
        max_len_number = get_max_len_number(flat_words_collection)
        for word, count in words_collection:
            str_len = len(f'{word}: {count}')
            complete_len = (max_len_word + max_len_number + 2) - str_len
            print(f'{word}: {count}', ' ' * complete_len, '*' * count)
    sys.stdout.write(Colors.BOLD + Colors.HEADER)
    print('=' * 80)
    sys.stdout.write(Colors.ENDC)


if __name__ == '__main__':
    main()
