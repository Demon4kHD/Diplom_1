import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_name_ingredient_true(self, create_ingredient):
        ingredient_type, name, price, ingredient = create_ingredient

        assert ingredient.get_name() == name

    def test_get_price_ingredient_true(self, create_ingredient):
        ingredient_type, name, price, ingredient = create_ingredient

        assert ingredient.get_price() == price

    def test_get_type_ingredient_true(self, create_ingredient):
        ingredient_type, name, price, ingredient = create_ingredient

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', [('VEGETABLES', 'salad', 150)])
    def test_create_self_ingredients_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
