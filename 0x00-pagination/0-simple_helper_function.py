#!/usr/bin/env python3
"""0-simple_helper_function module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieving the inddex range"""

    returns((page - 1) * page_size, ((page - 1) * page_size) + page_size)
