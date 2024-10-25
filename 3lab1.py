import threading
import time

class Pot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.servings = 0
        self.lock = threading.Lock()
        self.pot_not_empty = threading.Condition(self.lock)
        self.pot_not_full = threading.Condition(self.lock)

    def get_serving(self, savage_name):
        with self.pot_not_empty:
            while self.servings == 0:
                print(f"{savage_name} ждет, пока повар наполнит кастрюлю...")
                self.pot_not_empty.wait()
            self.servings -= 1
            print(f"{savage_name} съедает порцию, оставшиеся порции: {self.servings}")
            if self.servings == 0:
                self.pot_not_full.notify()

    def fill_pot(self):
        with self.pot_not_full:
            while self.servings > 0:
                self.pot_not_full.wait()
            self.servings = self.capacity
            print(f"Повар наполняет кастрюлю до {self.servings} порций.")
            self.pot_not_empty.notify_all()

class Savage(threading.Thread):
    def __init__(self, pot, name):
        super().__init__()
        self.pot = pot
        self.name = name

    def run(self):
        while True:
            self.pot.get_serving(self.name)
            time.sleep(1)

class Cook(threading.Thread):
    def __init__(self, pot):
        super().__init__()
        self.pot = pot

    def run(self):
        while True:
            self.pot.fill_pot()
            time.sleep(1)

if __name__ == "__main__":
    N = 5
    pot = Pot(N)

    cook_thread = Cook(pot)
    cook_thread.start()

    num_savages = 10
    for i in range(num_savages):
        Savage(pot, f"Дикарь {i}").start()