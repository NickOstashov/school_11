class Weapon:
    def __init__(self, name, dmg, stamin):
        self.name = name
        self.dmg = dmg
        self.stamin = stamin


class Character:
    def __init__(self, attr, hp, armor, stamin, weapon: Weapon):
        self.attr = attr
        self.hp = hp
        self.armor = armor
        self.stamin = stamin
        self.weapon = weapon
        self.is_dead = False

    def attack(self, other_character : 'Character'):
        print(f"[*]{self.__class__.__name__} атакует {other_character.__class__.__name__} оружием {self.weapon.name}")
        if other_character.armor > 0:
            other_character.armor -= self.weapon.dmg
            print(f"[*]Уровень брони врага снизился до {other_character.armor}")
        else:
            other_character.hp -= self.weapon.dmg
            print(f"[*]Уровень HP врага снизился до {other_character.hp}")

        if other_character.hp <= 0:
            other_character.rip()

    def rip(self):
        self.is_dead = True
        print(f"[*]Храбрый {self.__class__.__name__} героически погиб на поле боя")

    def take_weapon(self, other: "Character"):
        if other.is_dead:
            self.weapon = other.weapon
            print(f"[*]{self.__class__.__name__} отнимаем оружие {other.weapon.name}")
            other.weapon = Weapon('руки', 5, 5)
        else:
            print(f"{other.__class__.__name__} ещё жив")
            other.attack(self)


class MagicStaff(Weapon):
    def __init__(self, name, dmg, stamin, mp):
        self.mp = mp
        super().__init__(name, dmg, stamin)


class Wizard(Character):
    def __init__(self, attr, hp, armor, stamin, weapon: Weapon, mp):
        self.mp = mp
        super().__init__(attr, hp, armor, stamin, weapon)


class Warrior(Character):
    def __init__(self, attr, hp, armor, stamin, weapon: Weapon):
        super().__init__(attr, hp, armor, stamin, weapon)


def main():
    wr_wp = Weapon("меч", 20, 10)
    wr = Warrior("сила", 300, 200, 100, wr_wp)

    ms = MagicStaff("магический посох", 100, 10, 20)
    wz = Wizard("магия", 100, 0, 100, ms, 100)

    for i in range(6):
        wr.attack(wz)

    if wz.is_dead:
        wr.weapon = wz.take_weapon()

    print(wr.weapon.name)

if __name__ == "__main__":
    main()
