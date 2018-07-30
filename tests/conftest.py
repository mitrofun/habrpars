import os
import sys

import pytest
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.abspath('.'))


@pytest.fixture
def page():
    path = os.path.abspath('.')
    filename = os.path.join(path, 'fixtures', 'page.html')
    return filename


@pytest.fixture
def page_raw_content(page):
    with open(page, 'r', encoding='utf-8') as handler:
        html_content = handler.read()
        return html_content


@pytest.fixture
def page_content(page_raw_content):
    soup = BeautifulSoup(page_raw_content, 'html.parser')
    return soup
