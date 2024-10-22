from animal import Animal 
from constants import *
import math

def __calc_weight_loss_cat(corporal_weight: float) -> float:
    print(corporal_weight)
    return CAT_LOSS_WEIGHT_MULTIPLIER * math.pow(corporal_weight, CAT_LOSS_WEIGHT_EXPOENT)


def __calc_weight_loss_dog(corporal_weight: float) -> float:
    return DOG_LOSS_WEIGHT_MULTIPLIER * math.pow(corporal_weight, DOG_LOSS_WEIGHT_EXPOENT)


def calc_weight_loss(animal: Animal, corporal_weight: float) -> float:
    print(animal)

    match animal:
        case Animal.CAT:
            return __calc_weight_loss_cat(corporal_weight)

        case Animal.DOG:
            return __calc_weight_loss_dog(corporal_weight)
