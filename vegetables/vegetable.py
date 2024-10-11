class Vegetable:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name} (Calories: {self.calories})"

    def get_calories(self):
        return self.calories