from animal import Animal 
from constants import *
import math

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


def get_diary_amount_of_food(ne: float, em: float):
    """Returns the amount of food in g/day that the animal should eat.
    NE: Necessidade Energética
    EM: Energia de Manutenção"""
    return (ne * 1000) / em