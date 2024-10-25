import threading
import time
from queue import Queue

class Pot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.servings = 0
        self.lock = threading.Lock()
        self.pot_not_empty = threading.Condition(self.lock)
        self.pot_not_full = threading.Condition(self.lock)
        self.queue = Queue()

    def get_serving(self, savage_name):
        with self.lock:
            my_turn = threading.Condition(self.lock)
            self.queue.put(my_turn)

            while self.servings == 0 or self.queue.queue[0] is not my_turn:
                my_turn.wait()

            self.queue.get()
            self.servings -= 1
            print(f"{savage_name} съедает порцию, оставшиеся порции: {self.servings}")

            if self.servings == 0:
                self.pot_not_full.notify()

            if not self.queue.empty():
                next_savage = self.queue.queue[0]
                with next_savage:
                    next_savage.notify()

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