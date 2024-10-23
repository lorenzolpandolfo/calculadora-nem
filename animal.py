from enum import Enum

_translations = {
    'CAT': 'Gato',
    'DOG': 'Cachorro'
}

class Animal(Enum):
    CAT = 1
    DOG = 2

    def to_string(self):
        return _translations[self.name]
    