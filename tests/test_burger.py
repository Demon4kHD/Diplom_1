from data_burgers import DATA_BUNS
from praktikum.bun import Bun
from helpers import create_receipt_for_check


class TestBurger:
    def test_add_new_bun_and_set_adding(self, set_bun_in_order):
        burger, price, name = set_bun_in_order
        burger_price = burger.get_price()
        bun_price = price * 2
        assert burger_price == bun_price

    def test_changing_the_selection_bun_true(self, set_bun_in_order):
        burger, price, name = set_bun_in_order
        bun = Bun(DATA_BUNS['names'][1], DATA_BUNS['prices'][1])
        burger.set_buns(bun)
        burger_price = burger.get_price()
        bun_price = DATA_BUNS['prices'][1] * 2
        assert burger_price == bun_price

    def test_add_new_ingredient_and_get_price(self, add_ingredient_and_bun_for_test):
        (burger, bun_price, bun_name,
         ingredient_type, ingredient_name, ingredient_price, ingredient) = add_ingredient_and_bun_for_test
        price_burger = burger.get_price()
        check_value = bun_price * 2 + ingredient_price
        assert price_burger == check_value

    def test_remove_ingredient_in_burger(self, add_ingredient_and_bun_for_test):
        (burger, bun_price, bun_name,
         ingredient_type, ingredient_name, ingredient_price, ingredient) = add_ingredient_and_bun_for_test
        burger.remove_ingredient(0)
        price_burger = burger.get_price()
        check_value = bun_price * 2
        assert price_burger == check_value

    def test_get_receipt_burger(self, add_ingredient_and_bun_for_test):
        (burger, bun_price, bun_name,
         ingredient_type, ingredient_name, ingredient_price, ingredient) = add_ingredient_and_bun_for_test
        check_price_value = bun_price * 2 + ingredient_price
        burgers_receipt = burger.get_receipt()
        check_burger_receipt = create_receipt_for_check(bun_name,
                                                        [[ingredient_type, ingredient_name]],
                                                        check_price_value)
        assert burgers_receipt == check_burger_receipt

    def test_move_ingredient_in_burger(self, add_two_ingredient_and_one_bun_for_test):
        (burger, bun_price, bun_name, ingredient_type, ingredient_name, ingredient_price, ingredient,
         second_ingredient_type, second_ingredient_name, second_ingredient_price, second_ingredient) = (
            add_two_ingredient_and_one_bun_for_test
        )
        burger.move_ingredient(1, 0)
        check_price_value = bun_price * 2 + ingredient_price + second_ingredient_price
        burgers_receipt = burger.get_receipt()
        check_burger_receipt = create_receipt_for_check(bun_name,
                                                        [[second_ingredient_type, second_ingredient_name],
                                                         [ingredient_type, ingredient_name]
                                                         ],
                                                        check_price_value)
        assert burgers_receipt == check_burger_receipt
