from enum import Enum

_translations = {
    'WEIGHT_MAINTENANCE': "Manutenção do Peso",
    'WEIGHT_REDUCE': "Perda de Peso",
    'WEIGHT_GAIN': "Ganho de Peso",
}

class Operations(Enum):

    WEIGHT_MAINTENANCE = 1
    WEIGHT_REDUCE = 2
    WEIGHT_GAIN = 3

    
    def to_string(self):
        return _translations[self.name]
