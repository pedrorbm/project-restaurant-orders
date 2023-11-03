import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = dict()

        with open(self.source_path, encoding="utf8") as file:
            recipes = csv.reader(file, delimiter=",", quotechar='"')
            next(recipes)

            for dish, price, ingredient, amount in recipes:
                real = float(price)
                ingredients = Ingredient(ingredient)
                amounts = int(amount)

                if dish not in self.dishes:
                    self.dishes[dish] = Dish(dish, real)

                self.dishes[dish].add_ingredient_dependency(
                    ingredients, amounts
                )

            self.dishes = set(self.dishes.values())
