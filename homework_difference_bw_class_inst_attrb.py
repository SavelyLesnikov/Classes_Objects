import random


class Building:
    total = 0

    def __init__(self, bnum):
        self.total = Building.total
        self.bnum = bnum
        Building.total += 1

    def info(self):
        return f'{self.bnum}'


Building_objects = []

for i in range(40):
    obj = Building(f'№{random.randint(1, 45)}')
    Building_objects.append(obj)

for i in Building_objects:
    print(i.info())

print(Building_objects)
print(Building.total)
