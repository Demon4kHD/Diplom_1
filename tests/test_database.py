import pytest
from data_burgers import DATA_BUNS, DATA_INGREDIENTS
from helpers import create_data_for_test_database


class TestDatabase:
    def test_get_available_buns_len_true(self, create_database):
        database = create_database
        list_of_bons = database.available_buns()
        assert len(list_of_bons) == 3

    list_for_parametrize = create_data_for_test_database(current_dict=DATA_BUNS, current_key='names')

    @pytest.mark.parametrize('num_object, name', list_for_parametrize)
    def test_get_available_buns_object_has_true_name(self, create_database, num_object, name):
        database = create_database
        list_of_bons = database.available_buns()

        assert list_of_bons[num_object].get_name() == name

    list_for_parametrize = create_data_for_test_database(current_dict=DATA_BUNS, current_key='prices')

    @pytest.mark.parametrize('num_object, price', list_for_parametrize)
    def test_get_available_buns_object_has_true_price(self, create_database, num_object, price):
        database = create_database
        list_of_bons = database.available_buns()
        assert list_of_bons[num_object].get_price() == price

    def test_get_available_ingredients_len_true(self, create_database):
        database = create_database
        list_of_bons = database.available_ingredients()
        assert len(list_of_bons) == 6

    list_for_parametrize = create_data_for_test_database(current_dict=DATA_INGREDIENTS, current_key='types')

    @pytest.mark.parametrize('num_object, type_ingredient', list_for_parametrize)
    def test_get_available_ingredients_object_has_true_type(self, create_database, num_object, type_ingredient):
        database = create_database
        list_of_ingredients = database.available_ingredients()
        assert list_of_ingredients[num_object].get_type() == type_ingredient

    list_for_parametrize = create_data_for_test_database(current_dict=DATA_INGREDIENTS, current_key='names')

    @pytest.mark.parametrize('num_object, name', list_for_parametrize)
    def test_get_available_ingredients_object_has_true_name(self, create_database, num_object, name):
        database = create_database
        list_of_ingredients = database.available_ingredients()
        assert list_of_ingredients[num_object].get_name() == name

    list_for_parametrize = create_data_for_test_database(current_dict=DATA_INGREDIENTS, current_key='prices')

    @pytest.mark.parametrize('num_object, price', list_for_parametrize)
    def test_get_available_ingredients_object_has_true_price(self, create_database, num_object, price):
        database = create_database
        list_of_ingredients = database.available_ingredients()
        assert list_of_ingredients[num_object].get_price() == price
