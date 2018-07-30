import pytest

from datetime import datetime

from habrpars import (
    clean_text, normalize_words, get_words_on_date,
    scraping_html, fetch_request, fetch_raw_text,
    main
)


@pytest.mark.parametrize('text', [
    '«Сбербанк Управление Активами» вносит в анкету новых клиентов посторонний e-mail',
    'Определение части речи слов в русском тексте [теги] на Python 3',
    'Поиск узлов дисперсии управления (как перестать делать тупую работу и передать её другому)',
    '«Герои Меча и Магии» в браузере: долго, сложно и невыносимо интересно'
])
def test_clean_text(text):
    assert clean_text(text).isdigit() is False
    assert clean_text(text).find('»') == -1
    assert clean_text(text).find('[') == -1
    assert clean_text(text).find(']') == -1
    assert clean_text(text).find('(') == -1
    assert clean_text(text).find('Python') == -1


@pytest.mark.parametrize('words', [
    ['дома', 'почты'],
    ['дома', 'выросли', 'почту'],
    ['дома', 'выросли', 'в', 'почту'],
])
def test_normalize_words(words):
    assert normalize_words(words) == ['дом', 'почта']


def test_get_words_on_date():
    date = datetime(year=2018, month=1, day=1)
    assert get_words_on_date([('тестируем код скрипта', date)]) == {
        '2018-W1': ['тестируем', 'код', 'скрипта']
    }


def test_scraping_html(page_content):
    assert scraping_html(page_content) == [
        ('Создатель Питона я устал я ухожу', datetime(2018, 7, 13).date())
    ]


def test_fetch_request(requests_mock, page_raw_content):
    requests_mock.get('https://habr.com/all/', text=page_raw_content)
    assert fetch_request(page_number='', url='https://habr.com/all/') == page_raw_content


def test_fetch_raw_text(requests_mock, page_raw_content):
    for page in range(1, 6):
        requests_mock.get(f'https://habr.com/all/page{page}/', text=page_raw_content)

    assert fetch_raw_text(url='https://habr.com/all/', start_page=1, page_count=5) == [
        page_raw_content,
        page_raw_content,
        page_raw_content,
        page_raw_content,
        page_raw_content
    ]


def test_main(requests_mock, page_raw_content, capfd):
    for page in range(1, 11):
        requests_mock.get(f'https://habr.com/all/page{page}/', text=page_raw_content)
    main()
    out, err = capfd.readouterr()
    assert 'week' in out
    assert 'создатель' in out
    assert 'питон' in out
    assert '10' in out
