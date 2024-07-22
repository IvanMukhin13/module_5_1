class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if self.number_of_floors <= new_floor:
            print('Такого этаже не существует')
        else:
            for i in range(new_floor + 1):
                if i == 0:
                    continue
                print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
