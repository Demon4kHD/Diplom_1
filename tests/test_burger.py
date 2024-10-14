import pytest

from data_burgers import DATA_BUNS
from praktikum.bun import Bun


class TestBurger:
    def test_add_new_bun_and_set_adding(self, set_bun_in_order):
        burger, price = set_bun_in_order
        assert price == DATA_BUNS['prices'][0] * 2

    def test_changing_the_selection_bun_true(self, set_bun_in_order):
        burger, price = set_bun_in_order
        bun = Bun(DATA_BUNS['names'][1], DATA_BUNS['prices'][1])
        burger.set_buns(bun)
        price = burger.get_price()
        assert price == DATA_BUNS['prices'][1] * 2


