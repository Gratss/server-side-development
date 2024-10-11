from typing import List
from vegetables.vegetable import Vegetable

class Salad:
    def __init__(self):
        self.vegetables: List[Vegetable] = []

    def add_vegetable(self, vegetable: Vegetable):
        self.vegetables.append(vegetable)

    def total_calories(self) -> float:
        return sum(veg.get_calories() for veg in self.vegetables)

    def sort_vegetables(self, key='calories'):
        if key == 'calories':
            self.vegetables.sort(key=lambda x: x.get_calories())

    def find_vegetables_in_calorie_range(self, min_calories: float, max_calories: float) -> List[Vegetable]:
        return [veg for veg in self.vegetables if min_calories <= veg.get_calories() <= max_calories]

    def __str__(self):
        return "\n".join(str(veg) for veg in self.vegetables)
