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

@pytest.fixture()
def set_bun_in_order(create_burger):
    burger = create_burger
    bun = Bun(DATA_BUNS['names'][0], DATA_BUNS['prices'][0])
    burger.set_buns(bun)
    price = burger.get_price()
    return burger, price
