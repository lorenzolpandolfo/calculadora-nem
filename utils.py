from animal import Animal 
from constants import *
import math

kcal_mapping_dogs = {
        Condition.RESTING: RESTING_DOG_WEIGHT_MAINTANCE_KCAL,
        Condition.INACTIVE: INACTIVE_DOG_WEIGHT_MAINTANCE_KCAL,
        Condition.ACTIVE: ACTIVE_DOG_WEIGHT_MAINTANCE_KCAL,
    }


kcal_mapping_cats = {
        Condition.ACTIVE: ACTIVE_CAT_WEIGHT_MAINTANCE_KCAL,
        Condition.INDOOR: INDOOR_CAT_WEIGHT_MAINTANCE_KCAL,
        Condition.OBESE: OBESE_CAT_WEIGHT_MAINTANCE_KCAL,
    }

expoent_mapping_dogs = {
        Condition.RESTING: RESTING_DOG_WEIGHT_MAINTANCE_EXPOENT,
        Condition.INACTIVE: INACTIVE_DOG_WEIGHT_MAINTANCE_EXPOENT,
        Condition.ACTIVE: ACTIVE_DOG_WEIGHT_MAINTANCE_EXPOENT,
}

expoent_mapping_cats = {
        Condition.ACTIVE: ACTIVE_CAT_WEIGHT_MAINTANCE_EXPOENT,
        Condition.INDOOR: INDOOR_CAT_WEIGHT_MAINTANCE_EXPOENT,
        Condition.OBESE: OBESE_CAT_WEIGHT_MAINTANCE_EXPOENT,
}


def __calc_weight_loss_cat(corporal_weight: float) -> float:
    return CAT_LOSS_WEIGHT_MULTIPLIER * math.pow(corporal_weight, CAT_LOSS_WEIGHT_EXPOENT)


def __calc_weight_loss_dog(corporal_weight: float) -> float:
    return DOG_LOSS_WEIGHT_MULTIPLIER * math.pow(corporal_weight, DOG_LOSS_WEIGHT_EXPOENT)


def calc_weight_loss(animal: Animal, corporal_weight: float) -> float:
    match animal:
        case Animal.CAT:
            return __calc_weight_loss_cat(corporal_weight)

        case Animal.DOG:
            return __calc_weight_loss_dog(corporal_weight)



def calc_weight_maintance(animal: Animal, corporal_weight: float, fisiologic_condition: Condition) -> float:
    kcal_mapping = kcal_mapping_dogs if animal == Animal.DOG else kcal_mapping_cats
    expoent_mapping = expoent_mapping_dogs if animal == Animal.DOG else expoent_mapping_cats

    necessary_kcal = kcal_mapping.get(fisiologic_condition, 0)
    expoent = expoent_mapping.get(fisiologic_condition, 0)

    return necessary_kcal * math.pow(corporal_weight, expoent)


def get_diary_amount_of_food(ne: float, em: float):
    """Returns the amount of food in g/day that the animal should eat.
    NE: Necessidade Energética
    EM: Energia de Manutenção"""
    return (ne * 1000) / em