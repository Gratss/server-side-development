from .vegetable import Vegetable

class LeafyVegetable(Vegetable):
    def __init__(self, name: str, calories: float, leaf_type: str):
        super().__init__(name, calories)
        self.leaf_type = leaf_type

    def __str__(self):
        return f"{super().__str__()} - Type: {self.leaf_type}"