from src.models.ingredient import (Ingredient, Restriction)


# Req 1
def test_ingredient():
    ingredient_main = Ingredient("carne")
    restriction = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    assert ingredient_main.restrictions == restriction

    assert ingredient_main.name == "carne"

    assert ingredient_main == Ingredient("carne")

    assert hash(ingredient_main) == hash("carne")

    assert repr(ingredient_main) == "Ingredient('carne')"
