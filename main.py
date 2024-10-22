from utils import *
from constants import *
from animal import Animal


def draw_menu(title: str = MAIN_TITLE, options: list = MENU_OPTIONS):
    print("\n" + title + "=" * len(title) + "\n Escolha uma opção:")
    print(*(f"({i + 1}) {option}" for i, option in enumerate(options)), sep="\n")

    user_option = input("\n> Escolha uma opção: ")
    return user_option


def select_animal_type():
    animal_id = draw_menu(ANIMAL_SELECT_TITLE, [animal.to_string() for animal in ANIMALS])
    

def calculate(operation: str, animal: str):
    match operation:
        case '1':
            calc_weight_loss(animal)



if __name__ == "__main__":
    operation = draw_menu()
    animal = select_animal_type()

    calculate(operation, animal)


    print(f"Operação: {operation}\nAnimal: {animal}")
    



