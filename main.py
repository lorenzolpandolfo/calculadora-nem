from utils import *
from constants import *
from animal import Animal
from operations import Operations
import log


def draw_menu(title: str = TITLE_MAIN, options: list = MENU_OPTIONS) -> int:
    print("\n" + title + "=" * len(title))
    print(*(f"({i + 1}) {option}" for i, option in enumerate(options)), sep="\n")

    user_option = int(input("\n> Escolha uma opção: "))
    return user_option


def select_animal_type():
    formatted_animal_list = [animal.to_string() for animal in ANIMALS]
    animal_id = draw_menu(TITLE_ANIMAL_SELECT, formatted_animal_list)
    return Animal(animal_id)
    

def calculate_ne(operation: str, animal: str, corporal_weight: float):
    match operation:
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


def stream_handler(data: dict):

    if data['operation'] == Operations.WEIGHT_REDUCE.value:
        data['grams_of_food'] = calculate_amount_of_food(data['ne_value'])

    generate_report(data=data)



if __name__ == "__main__":

    while True:
        operation = draw_menu()
        animal = select_animal_type()

        corporal_weight = float(input(TITLE_SELECT_ANIMAL_WEIGHT).replace(",", "."))
        ne_value = calculate_ne(operation, animal, corporal_weight)

        data = {
            'operation': operation,
            'animal': animal,
            'ne_value': ne_value,
            'corporal_weight': corporal_weight
        }

        stream_handler(data)

        # log.create_log_record(data)

        loop = input(TITLE_LOOP)
        if loop != "":
            exit()
