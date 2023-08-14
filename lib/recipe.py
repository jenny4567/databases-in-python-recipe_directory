class Recipe():
    def __init__(self, id, recipe_name, cooking_time, rating):
        self.id = id
        self.recipe_name = recipe_name
        self.cooking_time = cooking_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"{self.recipe_name} - {self.cooking_time} mins - {self.rating}/5 stars"
