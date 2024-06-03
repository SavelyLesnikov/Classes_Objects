class Building:
    def __init__(self, number_of_floors: int, building_type: str):
        self.number_of_floors: int = number_of_floors
        self.building_type: str = building_type

       def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type


b1 = Building(5, 'Industrial')
b2 = Building(35, 'Office')
print(b1 == b2)
