class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = None

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(self.new_floor + 1):
                print(f'Этаж: {i}')


h1 = House('ЖК Простоквашино', 14)
h2 = House('ЖК Муравейник', 28)

h1.go_to(5)
h2.go_to(29)
