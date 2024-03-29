from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            # todas as paginas disponiveis na aplicacao
            page_range=list(range(1, 21)),
            qty_pages=4,  # quantidade de links que o usuario vera
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_page_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        # current page = 1 - Qty Page = 2 - Middle page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,  # quantidade de links que o usuario vera
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        # current page = 2 - Qty Page = 2 - Middle page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,  # quantidade de links que o usuario vera
            current_page=2,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        # current page = 3 - Qty Page = 2 - Middle page = 2
        # HERE RANGE SHOLUD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,  # quantidade de links que o usuario vera
            current_page=3,
        )
        self.assertEqual([2, 3, 4, 5], pagination)
