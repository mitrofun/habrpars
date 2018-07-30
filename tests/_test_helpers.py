# import pytest
# from datetime import datetime, timedelta
#

# @pytest.mark.parametrize('word', [
#     'код',
#     'параметр',
#     'частота',
# ])
# def test_is_noun_for_noun(word):
#     assert is_noun(word) is True
#
#
# @pytest.mark.parametrize('word', [
#     'копить',
#     'вычислять',
#     'писать',
# ])
# def test_is_noun_for_verb(word):
#     assert is_noun(word) is False
#
#
# @pytest.mark.parametrize('text', [
#     '«Сбербанк Управление Активами» вносит в анкету новых клиентов посторонний e-mail',
#     'Определение части речи слов в русском тексте [теги] на Python 3',
#     'Поиск узлов дисперсии управления (как перестать делать тупую работу и передать её другому)',
#     '«Герои Меча и Магии» в браузере: долго, сложно и невыносимо интересно'
# ])
# def test_clean_text(text):
#     assert clean_text(text).isdigit() is False
#     assert clean_text(text).find('»') == -1
#     assert clean_text(text).find('[') == -1
#     assert clean_text(text).find(']') == -1
#     assert clean_text(text).find('(') == -1
#     assert clean_text(text).find('Python') == -1
#
#
# def test_normalize_word():
#     assert normalize_word('дома') == 'дом'
#     assert normalize_word('почты') == 'почта'
#     assert normalize_word('стали') == 'стать'
#
#
# def test_get_normalize_noun_from_post_title():
#     assert get_normalize_noun_from_post_title('проверки томов') == ['проверка', 'том']
#
#
