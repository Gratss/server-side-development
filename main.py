from vegetables.root_vegetable import RootVegetable
from vegetables.leafy_vegetable import LeafyVegetable
from salad.salad import Salad

def menu():
    salad = Salad()

    while True:
        print("\n1. Добавить овощ")
        print("2. Подсчитать калории салата")
        print("3. Отсортировать овощи по калорийности")
        print("4. Найти овощи в заданном диапазоне калорийности")
        print("5. Показать все овощи в салате")
        print("6. Выход")
        
        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Введите имя овоща: ")
            calories = float(input("Введите калорийность овоща: "))
            type_ = input("Введите тип (корень/листья): ")
            if type_ == "корень":
                root_type = input("Введите подтип корня: ")
                salad.add_vegetable(RootVegetable(name, calories, root_type))
            elif type_ == "листья":
                leaf_type = input("Введите подтип листа: ")
                salad.add_vegetable(LeafyVegetable(name, calories, leaf_type))
            else:
                print("Недопустимый тип овоща!")

        elif choice == "2":
            print(f"Общая калорийность салата: {salad.total_calories()}")

        elif choice == "3":
            salad.sort_vegetables()
            print("Овощи отсортированы по калорийности")

        elif choice == "4":
            min_calories = float(input("Введите минимальную калорийность: "))
            max_calories = float(input("Введите максимальную калорийность: "))
            found_vegetables = salad.find_vegetables_in_calorie_range(min_calories, max_calories)
            print("Найденные овощи:", found_vegetables)

        elif choice == "5":
            print("Овощи в салате:")
            print(salad)

        elif choice == "6":
            print("Выход...")
            break

        else:
            print("Недопустимый выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
