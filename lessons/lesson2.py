
class Hero:
    # конструктор класса
    def __init__(self, nick, lvl, hp):
        # Атрибута класса
        self.nick = nick
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.nick} base action activate"

class MageHero(Hero):

    def __init__(self, nick, lvl, hp, mp):
        super().__init__(nick, lvl, hp)
        self.mp = mp

    def action(self):
        return f"This is new method - child cass {self.nick}"

# asuna = Hero("Asuna", 999, 9999)
# mage_kirito = MageHero("Ardager", 100, 1000, 100)

# print(type(asuna))
# print(type(kirito))

# print(mage_kirito.nick)
# print(asuna.action())

class Animal:

    def action(self):
        print(f"Animal action")

class Fly(Animal):

    def action(self):
        super().action()
        print(f"Fly action")

class Swim(Animal):

    def action(self):
        super().action()
        print(f"Swim action")

class Duck(Fly, Swim):
    def action(self):
        super().action()
        print(f"Duck action")

donald_duck = Duck()
donald_duck.action()
print(Duck.__mro__)

