import os

from utils import *
from constants import *
from animal import Animal
from operations import Operations
import log


def draw_menu(title: str = TITLE_MAIN, options: list = [o.to_string() for o in MENU_OPTIONS]) -> int:
    print(f"\n{title}" + "=" * len(title))
    print(*(f"({i + 1}) {option}" for i, option in enumerate(options)), sep="\n")

    user_option = int(input("\n> Escolha uma opção: "))
    return user_option


def select_animal_type():
    animal_id = draw_menu(TITLE_ANIMAL_SELECT, [a.to_string() for a in ANIMALS])
    return Animal(animal_id)
    

def calculate_ne(operation: str, animal: Animal, corporal_weight: float, f_condition: Condition | bool):
    match operation:
        case 1:
            return calc_weight_maintance(animal, corporal_weight, f_condition)

        case 2:
            return calc_weight_loss(animal, corporal_weight)

def generate_report(title: str = "[Relatório Final]", data: dict | bool = False):
    if not data:
        return

    print(f"\n{title}\n" + "=" * len(title))

    animal_format = Animal(animal).to_string()
    operation_format = Operations(operation).to_string()
    corporal_weight = data['corporal_weight']
    grams_of_food = data['grams_of_food']
    f_condition_format = Condition(f_condition).to_string() if f_condition else ""

    condition_phrase = f" na condição {f_condition_format}" if f_condition else ""

    print(f"\n> Para um {animal_format} de {corporal_weight}kg{condition_phrase} e na opção {operation_format},\n" +
          f"a Necessidade Energética (NE) é de {ne_value:.2f}kcal e a quantidade DIÁRIA de ração é de {grams_of_food:.2f} gramas.\n" +
          f"Considerando 3 refeições por dia, cada uma deve ter {(grams_of_food / 3):.2f} gramas.\n")


def calculate_amount_of_food(ne: float) -> float:
    kcal_in_kg = float(input("\n[?] Quantas Kcal tem em 1kg da ração? ").replace(",", "."))
    return get_diary_amount_of_food(ne, kcal_in_kg)


def select_fisiologic_condition(animal: Animal):
    is_cat = animal == Animal.CAT
    f_conditions = MENU_CAT_FISIOLOGIC_CONDITIONS if is_cat else MENU_DOG_FISIOLOGIC_CONDITIONS
    fc_id = draw_menu("Selecione a Condição Fisiológica do Animal:\n", [c.to_string() for c in f_conditions])
    return Condition(f_conditions[fc_id - 1])


if __name__ == "__main__":

    while True:
        operation = draw_menu()
        animal = select_animal_type()
        corporal_weight = float(input(TITLE_SELECT_ANIMAL_WEIGHT).replace(",", "."))
        f_condition = False
        
        if operation == Operations.WEIGHT_MAINTENANCE:
            f_condition = select_fisiologic_condition(animal)

        ne_value = calculate_ne(operation, animal, corporal_weight, f_condition)
        grams_of_food = calculate_amount_of_food(ne_value)

        data = {
            'operation': operation,
            'animal': animal,
            'corporal_weight': corporal_weight,
            'f_condition': f_condition,
            'ne_value': ne_value,
            'grams_of_food': grams_of_food
        }

        generate_report(data=data)

        log.create_log_record(data)

        loop = input(TITLE_LOOP)
        os.system('cls')
        
        if loop != "":
            exit()
