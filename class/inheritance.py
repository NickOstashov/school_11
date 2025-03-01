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
    def __init__(self, skin, color, kind):
        super().__init__(skin, color, kind)


def main():
    cat = Cat("шерсть", "черно-белый", "домашний")
    print(cat)
    cat.move()


if __name__ == "__main__":
    main()