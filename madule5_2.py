class house:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'This is house {self.name}, namber floors {self.number_of_floors}')


    def go_to(self, new_floors):
        for i in range(1, new_floors):
            if new_floors > self.number_of_floors or new_floors < 1:
                print(f"There is no such floor{new_floors}")
                break
            else:
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Names: {self.name}, quantity floors:{self.number_of_floors}  "
h1 = house('ЖК Горский', 6)
h2 = house('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# __str__
# print(h1)
# print(h2)
#
# __len__
# print(len(h1))
# print(len(h2))
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20
#
# Примечания: