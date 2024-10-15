import random

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger
from data_burgers import DATA_BUNS, DATA_INGREDIENTS


@pytest.fixture
def create_bun():
    name  = random.choice(DATA_BUNS['names'])
    price = random.choice(DATA_BUNS['prices'])
    bun = Bun(name, price)
    return name, price, bun

@pytest.fixture
def create_ingredient():
    ingredient_type = random.choice(DATA_INGREDIENTS['types'])
    name  = random.choice(DATA_INGREDIENTS['names'])
    price = random.choice(DATA_INGREDIENTS['prices'])
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient_type, name, price, ingredient

@pytest.fixture
def create_database():
    database = Database()
    return database

@pytest.fixture
def create_burger():
    burger = Burger()
    return burger

@pytest.fixture
def set_bun_in_order(create_burger):
    burger = create_burger
    name = random.choice(DATA_BUNS['names'])
    price = random.choice(DATA_BUNS['prices'])
    bun = Bun(name, price)
    burger.set_buns(bun)
    return burger, price, name

@pytest.fixture
def add_ingredient_and_bun_for_test(set_bun_in_order, create_ingredient):
    burger, bun_price, bun_name = set_bun_in_order
    ingredient_type, ingredient_name, ingredient_price, ingredient = create_ingredient
    burger.add_ingredient(ingredient)
    return burger, bun_price, bun_name, ingredient_type, ingredient_name, ingredient_price, ingredient

@pytest.fixture
def add_two_ingredient_and_one_bun_for_test(set_bun_in_order):
    burger, bun_price, bun_name = set_bun_in_order
    first_ingredient_type = DATA_INGREDIENTS['types'][3]
    first_ingredient_name = DATA_INGREDIENTS['names'][3]
    first_ingredient_price = DATA_INGREDIENTS['prices'][3]
    first_ingredient = Ingredient(first_ingredient_type, first_ingredient_name, first_ingredient_price)
    burger.add_ingredient(first_ingredient)
    second_ingredient_type = DATA_INGREDIENTS['types'][0]
    second_ingredient_name = DATA_INGREDIENTS['names'][0]
    second_ingredient_price = DATA_INGREDIENTS['prices'][0]
    second_ingredient = Ingredient(second_ingredient_type, second_ingredient_name, second_ingredient_price)
    burger.add_ingredient(second_ingredient)
    return (burger, bun_price, bun_name, first_ingredient_type,
            first_ingredient_name, first_ingredient_price, first_ingredient,
            second_ingredient_type, second_ingredient_name, second_ingredient_price,
            second_ingredient)