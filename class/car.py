class Car:
    def __init__(self, car_color, door_number, fuel):
        self.color : str = car_color
        self.doors_number : int = door_number
        self.fuel : str = fuel

    def print_info(self):
        print("цвет :", self.color)
        print("количество дверей :", self.doors_number)
        print("топливо: ", self.fuel)


def main():
    car1 = Car("желтая", 2, "бензин")
    #car1.print_info()

    car2 = Car("Черный", 4, "электричество")
    #print(len(car2))

    print(car1 > car2)



if __name__ == "__main__":
    main()


