from data_source import get_name
from decorators import noise_logger

class Person(object):
    def __init__(self):
        self.pet = Pet()

    def name(self):
        return get_name()

class Pet():
    @noise_logger
    def noise(self):
        return "Woof"