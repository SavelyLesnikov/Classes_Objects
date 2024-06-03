class House:
    def __init__(self, number_of_floors):
        self.number_of_floors = number_of_floors

    def __setNewNumberOfFloors__(floors):
        number_of_floors = floors
        print(f'Количество этажей: {number_of_floors}')


House.__setNewNumberOfFloors__(14)
