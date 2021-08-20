from re import findall
from typing import List, Dict, Union, AnyStr


class DishesModule:
    def __init__(self, data_file_location: str):
        self._dishes_menu: Dict[str, List[Dict[str, Union[str, int]]]] = {}
        self._prepare_dict(self._load_data(f"{data_file_location}/input_data.txt"))

    @classmethod
    def _load_data(cls, file_path: str) -> List[AnyStr]:
        """
            Method to extract lines data from file
        :param file_path: Path to the file
        :return: List with file lines content
        """
        return [
            line.removesuffix("\n")
            for line in open(file=file_path, mode="r", encoding="utf-8").readlines()
            if line.removesuffix("\n") != ""
        ]

    @classmethod
    def _has_delimiter(cls, input_string: str) -> bool:
        """
            Method to check if line has delimiter
        :param input_string: Line to check for delimiter
        :return: Has line delimiter or no
        """
        return bool(findall(r"\s\|\s", string=input_string))

    def get_dishes_menu(self):
        return self._dishes_menu

    def _prepare_dict(
        self,
        raw_data_list: List[AnyStr],
    ) -> None:
        """
            Method to assemble dish dictionary for future use
        :param raw_data_list: List of raw lines data from file
        :return:
        """
        dish_name: str = ""
        ingredients_count: int = 0
        existing_ingredients: List[str] = []
        for idx, data_line in enumerate(raw_data_list):
            if not self._has_delimiter(data_line) and not data_line.isnumeric():
                self._dishes_menu[data_line] = []
                dish_name = data_line
            elif data_line.isnumeric():
                ingredients_count = int(data_line)
            elif (
                self._has_delimiter(data_line)
                and not data_line.isnumeric()
                and data_line not in existing_ingredients
            ):
                for ingredient_line in raw_data_list[idx : idx + ingredients_count]:
                    existing_ingredients.append(ingredient_line)
                    ingredient_line = ingredient_line.split(" | ")
                    self._dishes_menu[dish_name].append(
                        {
                            "ingredient_name": ingredient_line[0],
                            "quantity": int(ingredient_line[1]),
                            "measure": ingredient_line[2],
                        }
                    )
        del existing_ingredients, ingredients_count, dish_name

    def get_shop_list_by_dishes(
        self, dishes_list: List[str], person_count: int
    ) -> Dict[str, Dict[str, int]]:
        """
            Method to assemble shopping list of ingredients
        :param dishes_list: List of dishes to search for ingredients
        :param person_count: How many guests would be
        :return: Dictionary of ingredients and their amount to buy
        """
        shopping_bag: Dict[str, Dict[str, int]] = {}

        for dish in dishes_list:
            if list(self._dishes_menu.keys()).__contains__(dish):
                for ingredient in self._dishes_menu.get(dish):
                    shopping_bag.update(
                        {
                            ingredient.get("ingredient_name"): {
                                "measure": ingredient.get("measure"),
                                "quantity": ingredient.get("quantity") * person_count,
                            }
                        }
                    )
            else:
                print(f"\nТакого блюда [ {dish} ] нету в меню", end="\n")

        return shopping_bag
