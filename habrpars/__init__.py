import os
import sys

from .console import Colors  # noqa
from .dates import (normalize_date, get_first_date_in_week, # noqa
                    date_to_string, get_last_date_in_week)  # noqa
from .helpers import get_max_len_number, timed, flat_list, get_max_len_word  # noqa

from .habrpars import (main, clean_text, normalize_words,  # noqa
    get_words_on_date, scraping_html, fetch_request, fetch_raw_text)  # noqa


sys.path.insert(0, os.path.abspath('.')) # noqa
