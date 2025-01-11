class House:


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floors):
        self.new_floors = new_floors
        if self.number_of_floors >= 1:

            if self.new_floors > self.number_of_floors:
                print('this isn,t floors')
            else:
                for i in range(1, self.new_floors):
                    print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Names: {self.name}, quantity floors:{self.number_of_floors}  "
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
