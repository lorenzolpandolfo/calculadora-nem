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
    

def calculate(operation: str, animal: str, corporal_weight: float):
    match operation:
        case 2:
            return calc_weight_loss(animal, corporal_weight)

def generate_report(title: str = "[ Relatório Final ]", data: dict | bool = False):
    if not data:
        return

    print(f"\n{title}\n" + "=" * len(title))
    print(*(f"{key}: {value}" for key, value in data.items()), sep="\n")

    animal_format = Animal(animal).to_string()
    operation_format = Operations(operation).to_string()

    corporal_weight = data['corporal_weight']

    print(f"[=] Para um {animal_format} de {corporal_weight}kg, na opção {operation_format}, o EM = {em_value}")


if __name__ == "__main__":

    while True:
        data = {}

        operation = draw_menu()
        animal = select_animal_type()

        corporal_weight = float(input(TITLE_SELECT_ANIMAL_WEIGHT).replace(",", "."))
        em_value = calculate(operation, animal, corporal_weight)

        data["operation"] = operation
        data["animal"] = animal
        data["em_value"] = em_value
        data["corporal_weight"] = corporal_weight

        generate_report(data=data)

        log.create_log_record(data)

        loop = input(TITLE_LOOP)

        if loop != "":
            exit()

    



