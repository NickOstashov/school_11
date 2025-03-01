class Animal:
    def __init__(self, skin, color, kind):
        self.skin = skin
        self.color = color
        self.kind = kind

    def __repr__(self):
        return f"<Animal skin: {self.skin}, color: {self.color}, kind: {self.kind}>"

    def move(self):
        print(f"{self.kind} ползет по земле")


class Cat(Animal):
    def __init__(self, skin, color, kind, night_vision):
        self.night_vision = night_vision
        super().__init__(skin, color, kind)

    def down(self):
        print(f"{self.kind} приземлился на лапы")


class HomeCat(Cat):
    def __init__(self, skin, color, kind, night_vision):
        super().__init__(skin, color, kind, night_vision)


def main():
    home_cat = HomeCat("шерсть", "черно-белый", "домашний кот", True)
    print(home_cat)
    home_cat.move()


if __name__ == "__main__":
    main()