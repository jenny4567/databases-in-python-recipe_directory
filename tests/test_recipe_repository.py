from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipe.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new ArtistRepository

    recipies = repository.all()

    # Assert on the results
    assert recipies == [
        Recipe(1, 'Lasagna', 150, 4),
        Recipe(2, 'Pizza', 30, 2),
        Recipe(3, 'Pudding', 70, 3)
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipe.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(2)
    assert recipe == Recipe(2, 'Pizza', 30, 2)




