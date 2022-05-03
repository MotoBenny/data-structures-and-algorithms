from data_structures.queue import Queue
from data_structures.linked_list import Node


class AnimalShelter:

    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):

        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        if isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)

    def dequeue(self, perf):

        if perf is 'dog':
            return self.dog_queue.dequeue()
        if perf is 'cat':
            return self.cat_queue.dequeue()
        if perf != 'dog' and perf != 'cat':
            return None

class Dog:
    pass


class Cat:
    pass
