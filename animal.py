from enum import Enum

class Animal(Enum):
    CAT = 1
    DOG = 2

    def to_string(self):
        return self.name.replace("DOG", "Cachorro").replace("CAT", "Gato")
    