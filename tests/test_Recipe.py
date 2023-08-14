from lib.recipe import Recipe

"""
Artist constructs with an id, name and genre
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe 1", 20, 4)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test Recipe 1"
    assert recipe.cooking_time == 20
    assert recipe.rating == 4

"""
We can format recipies to strings nicely
"""
def test_recipe_format_nicely():
    recipe = Recipe(1, "Test Recipe 1", 20, 4)
    assert str(recipe) == "Test Recipe 1 - 20 mins - 4/5 stars"

"""
We can compare two identical recipies
And have them be equal
"""
def test_recipies_are_equal():
    recipe1 = Recipe(1, "Test Recipe 1", 20, 4)
    recipe2 = Recipe(1, "Test Recipe 1", 20, 4)
    assert recipe1 == recipe2
