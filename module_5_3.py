class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor and self.number_of_floors >= 1:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other
    def __lt__(self, other):
        return self.number_of_floors < other
    def __le__(self, other):
        return self.number_of_floors <= other
    def __gt__(self, other):
        return self.number_of_floors > other
    def __ge__(self, other):
        return self.number_of_floors >= other
    def __ne__(self, other):
        return self.number_of_floors != other
    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        return House(self.name, self.number_of_floors + value)
    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(str(h1))
print(str(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(str(h1))
print(h1 == h2)

h1 += 10 # __iadd__
print(str(h1))

h2 = 10 + h2 # __radd__
print(str(h2))

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

