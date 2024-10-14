import pytest
from praktikum.bun import Bun


class TestsBun:

    @pytest.mark.parametrize('name, price', [
        ('zero-calories bun', 12.60), ('high-calories bun', 300.0000000), ('salty bun', 100500.00)
    ])
    def test_create_new_bun_true(self, name, price):
        self.bun = Bun(name, price)

        assert self.bun.get_name() == name
        assert self.bun.get_price() == price
