from enum import Enum

_translations = {
    'RESTING': 'Repouso', 
    'INACTIVE': 'Inativo',
    'ACTIVE': 'Ativo',
    'INDOOR': 'Indoor',
    'OBESE': 'Obeso'
}

class Condition(Enum):

    RESTING = 1
    INACTIVE = 2
    ACTIVE = 3
    INDOOR = 4
    OBESE = 5
    
    def to_string(self):
        return _translations[self.name]
