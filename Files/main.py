from pprint import pprint
from typing import List

from modules import DishesModule, FilesModule

DATA_FILES_LOCATION: str = f"{__file__}/../data"

INPUT_FILES: List[str] = ["1.txt", "2.txt", "3.txt"]
OUTPUT_FILE: str = f"{DATA_FILES_LOCATION}/output.txt"


def files_hw():
    print(f'\n{"#" * 30}\n' f"#   Задания с Файлами" f'\n{"#" * 30}\n')
    file_task: FilesModule = FilesModule(DATA_FILES_LOCATION, INPUT_FILES)
    file_task.write_output_file()
    file_task.read_output_file_content()


def dishes_hw():
    print(f'\n{"#"*30}\n' f"#   Задания с Блюдами" f'\n{"#"*30}\n')
    dish_menu: DishesModule = DishesModule(data_file_location=DATA_FILES_LOCATION)
    print("Меню блюд с ингредиентами:" f'\n{"-"*60}')
    pprint(dish_menu.get_dishes_menu())
    print(f'\n{"="*100}\n')
    dishes_list: List[str] = ["Запеченный картофель", "Омлет"]
    guests_count: int = 2
    print(
        f"Список покупок для {dishes_list} на {guests_count} гостей\n{'-'*60}",
        end="\n",
    )
    pprint(dish_menu.get_shop_list_by_dishes(dishes_list, guests_count))
    print(f'\n{"=" * 100}\n')


def main():
    dishes_hw()
    files_hw()


if __name__ == "__main__":
    main()
