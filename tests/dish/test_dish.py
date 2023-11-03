import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish_main = Dish("sushi", 1.50)
    ingredient_main = Ingredient("salmão")
    restriction = {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_main.name == "sushi"

    assert dish_main.price == 1.50

    assert dish_main.recipe == {}

    assert dish_main == Dish("sushi", 1.50)

    dish_main.add_ingredient_dependency(ingredient_main, 1)

    assert dish_main.recipe == {Ingredient("salmão"): 1}

    assert hash(dish_main) == hash("Dish('sushi', R$1.50)")

    assert repr(dish_main) == "Dish('sushi', R$1.50)"

    assert dish_main.get_restrictions() == restriction

    assert dish_main.get_ingredients() == {Ingredient("salmão")}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("sushi", "1.50")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("sushi", 0)
