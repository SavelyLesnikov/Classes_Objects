class Building:
    def __init__(self, number_of_floors: int, building_type: str):
        self.number_of_floors: int = number_of_floors
        self.building_type: str = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.building_type


b1 = Building(5, 'Industrial')
b2 = Building(5, 5)
print(b1 == b1)
print(b2 == b2)
