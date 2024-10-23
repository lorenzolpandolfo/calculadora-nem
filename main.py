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
    

def calculate_ne(operation: str, animal: str, corporal_weight: float):
    match operation:
        case 1:
            fisiologic_condition_id = draw_menu("Selecione a Condição Fisiológica do Animal:\n", [c.to_string() for c in MENU_FISIOLOGIC_CONDITIONS])
            return calc_weight_maintance(animal, corporal_weight, Condition(fisiologic_condition_id))

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

    print(f"[=] Para um {animal_format} de {corporal_weight}kg, na opção {operation_format}, a Necessidade Energética (NE) é de {ne_value:.2f}kcal" +
          f" e a quantidade DIÁRIA de ração é de {grams_of_food:.2f} gramas.\n")


def calculate_amount_of_food(ne: float) -> float:
    kcal_in_kg = float(input("[?] Quantas Kcal tem em 1kg da ração? ").replace(",", "."))
    return get_diary_amount_of_food(ne, kcal_in_kg)


if __name__ == "__main__":

    while True:
        operation = draw_menu()
        animal = select_animal_type()
        corporal_weight = float(input(TITLE_SELECT_ANIMAL_WEIGHT).replace(",", "."))
        ne_value = calculate_ne(operation, animal, corporal_weight)
        grams_of_food = calculate_amount_of_food(ne_value)

        data = {
            'operation': operation,
            'animal': animal,
            'corporal_weight': corporal_weight,
            'ne_value': ne_value,
            'grams_of_food': grams_of_food
        }

        generate_report(data=data)

        log.create_log_record(data)

        loop = input(TITLE_LOOP)
        if loop != "":
            exit()
