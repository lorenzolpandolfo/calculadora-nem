from animal import Animal

# Weight loss
DOG_LOSS_WEIGHT_MULTIPLIER = 64
CAT_LOSS_WEIGHT_MULTIPLIER = 85

DOG_LOSS_WEIGHT_EXPOENT = 0.75
CAT_LOSS_WEIGHT_EXPOENT = 0.4

RESTING_DOG_WEIGHT_MAINTANCE_KCAL = 70 
INACTIVE_DOG_WEIGHT_MAINTANCE_KCAL = 95
ACTIVE_DOG_WEIGHT_MAINTANCE_KCAL = 130

# Weight maintance
# Confirmar esses valores:
RESTING_DOG_WEIGHT_MAINTANCE_EXPOENT = 0.25 
INACTIVE_DOG_WEIGHT_MAINTANCE_EXPOENT = 0.75
ACTIVE_DOG_WEIGHT_MAINTANCE_EXPOENT = 0.25


SLIM_CAT_WEIGHT_MAINTANCE_KCAL = 63.5
ACTIVE_CAT_WEIGHT_MAINTANCE_KCAL = 100
OBESE_CAT_WEIGHT_MAINTANCE_KCAL = 130

SLIM_CAT_WEIGHT_MAINTANCE_KCAL = 0.57
ACTIVE_CAT_WEIGHT_MAINTANCE_KCAL = 0.57
OBESE_CAT_WEIGHT_MAINTANCE_KCAL = 0.4


# Menu constants
MAIN_TITLE = "Calculadora de Necessidade Energética\n"
MENU_OPTIONS = ["Manutenção do Peso", "Perda de Peso", "Ganho de Peso"]
ANIMAL_SELECT_TITLE = "Selecione o Animal:\n"
ANIMALS = [Animal.CAT, Animal.DOG]




