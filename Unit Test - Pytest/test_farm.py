# TESTING USING PYTEST FRAMEWORK

from farm import Pets as pt
from farm import FarmAnimals as fa
import pytest

# INSTANCES AND PARAMETERS - SETUP AND TEARDOWN
@pytest.fixture(scope="module")
def pet1():
    pet1 = pt('hamster', 2, 'Einstein')
    pet1.hunger = 74
    print('-----------------pet1 setup----------------- ')
    yield pet1
    print('-----------------pet1 teardown---------------- ')

@pytest.fixture(scope="module")
def pet2():
    pet2 = pt('snake', 3, 'Layla')
    print('-----------------pet2 setup----------------- ')
    yield pet2
    print('-----------------pet2 teardown---------------- ')

@pytest.fixture(scope="module")
def ani1():
    ani1 = fa('sheep', 4, 'Marry', 'baah')
    ani1.hunger = 121
    print('-----------------ani1 setup----------------- ')
    yield ani1
    print('-----------------ani1 teardown---------------- ')

@pytest.fixture(scope="module")
def ani2():
    ani2 = fa('donkey', 3, 'Oswald', 'hee-haw')
    print('-----------------pet2 setup----------------- ')
    yield ani2
    print('-----------------ani2 teardown---------------- ')

# STRING RETURNING METHODS

# Testing hungry method
@pytest.mark.string
def test_hungry(pet1, ani1):
    assert pet1.hungry() == 'Your animal is hungry! You should feed your hamster !'
    assert ani1.hungry() == 'Your sheep is full and happy :)'

# Testing makeSound method
@pytest.mark.string
def test_makeSound(ani1):
    assert ani1.makeSound() == 'sheep does baah!'

# Testing info metod
@pytest.mark.string
def test_info(pet1, ani2):  
    assert pet1.info() == 'My hamster\'s name is Einstein and he is 2 years old.'
    assert ani2.info() == 'My donkey\'s name is Oswald and he is 3 years old.'

# SETTERS TEST

@pytest.mark.setter
@pytest.mark.parametrize('new_name', ['Susan', 'Lily','Cat'])
def test_name(new_name, ani2):
    ani2.name = new_name
    assert ani2.name == new_name