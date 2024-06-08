class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Количество этажей в доме:", self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors(10)