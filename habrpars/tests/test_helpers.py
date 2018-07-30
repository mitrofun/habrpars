import pytest

from helpers import flat_list, get_max_len_word, get_max_len_number


def test_flat_list():
    assert flat_list([(1, 2)]) == [1, 2]
    assert flat_list([[1, 2, 3]]) == [1, 2, 3]
    assert flat_list([(1, 2), (3, 4)]) == [1, 2, 3, 4]


@pytest.mark.parametrize('_list', [
    ['тест', 1, 12, 'проверка'],
    ['тест', 'проверка']
])
def test_get_max_len_word(_list):
    assert get_max_len_word(_list) == 8


@pytest.mark.parametrize('_list', [
    ['тест', 1, 12, 'проверка'],
    ['тест', 'проверка', 23, 46]
])
def test_get_max_len_number(_list):
    assert get_max_len_number(_list) == 2
