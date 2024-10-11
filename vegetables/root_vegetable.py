from .vegetable import Vegetable

class RootVegetable(Vegetable):
    def __init__(self, name: str, calories: float, root_type: str):
        super().__init__(name, calories)
        self.root_type = root_type

    def __str__(self):
        return f"{super().__str__()} - Type: {self.root_type}"
