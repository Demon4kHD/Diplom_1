import pytest

from praktikum.bun import Bun


class TestsBun:
    def test_get_name_true(self, create_bun):
        name, price,  bun = create_bun
        current_name = bun.get_name()
        assert current_name == name

    def test_get_price_true(self, create_bun):
        name, price, bun = create_bun
        current_price = bun.get_price()
        assert current_price == price

    @pytest.mark.parametrize('name, price', [('salty bun', 150), ('sugar bun', 350)])
    def test_create_self_bun_true(self, name, price):
        bun = Bun(name, price)
        current_name = bun.get_name()
        current_price = bun.get_price()

        assert current_name == name
        assert current_price == price

