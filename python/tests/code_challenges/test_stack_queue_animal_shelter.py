import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat
from data_structures.queue import InvalidOperationError


def test_cat_enqueue(): # confirm my enqueue is working
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.cat_queue.size
    expected = 1
    assert  actual == expected


def test_dog_enqueue():  # confirm my enqueue is working
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dog_queue.size
    expected = 1
    assert actual == expected


def test_cat_dequeue():  # confirm my enqueue is working
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    shelter.dequeue('cat')
    actual = shelter.cat_queue.size
    expected = 0
    assert actual == expected


def test_dog_dequeue():  # confirm my enqueue is working
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.dequeue('dog')
    actual = shelter.dog_queue.size
    expected = 0
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected  # truthy is this node = the same node


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual
