

class Character:
    def __init__(self, name, life, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        other.life -= self.attack
    
    def __str__(self):
        return f"{self.name} now has {self.life} hp and {self.attack} damage."
    
class Druid(Character):
    pass

    def meditate(self):
        self.life += 10
        self.attack -=2
        print(f"{self.name} used meditation.")

    def animal_help(self):
        self.attack +=5
        print(f"{self.name} used animal help.")

    def fight(self, other):
        other.life -= int(0.75*self.life + 0.75*self.attack)
        print(f"{self.name} used 'fight' on {other.name}")


class Warrior(Character):
    pass

    def brawl(self, other):
        other.life -= 2*self.attack
        self.life += 0.5*self.attack
        print(f"{self.name} used 'brawl' on {other.name}")

    def train(self):
        self.life +=2
        self.attack+=2
        print(f"{self.name} used train")

    def roar(self,other):
        other.attack -= 3
        print(f"{self.name} used 'roar' on {other.name}")



class Mage(Character):
    pass

    def curse(self,other):
        other.attack -=2
        print(f"{self.name} used 'curse' on {other.name}")

    def summon(self):
        self.attack +=3
        print(f"{self.name} used summon")

    def cast_spell(self,other):
        other.life -= int(self.life/self.attack)
        print(f"{self.name} used 'cast spell' on {other.name}")


furion = Druid("Natures Prophet", 200, 20)
beastmaster = Warrior("Beastmaster", 300, 15)
invoker = Mage("Invoker", 150, 30)

# # Checking all methods of all characters

# # Default methods
print(furion)
print(beastmaster)
print(invoker)
furion.basic_attack(beastmaster)
beastmaster.basic_attack(invoker)
invoker.basic_attack(furion)
print(furion)
print(beastmaster)
print(invoker)

# Checking furion's methods

print(furion)
furion.meditate()
print(furion)
furion.animal_help()
print(furion)
print(beastmaster)
furion.fight(beastmaster)
print(beastmaster)

# Cheking beastmaster's methods
print(furion)
print(beastmaster)
beastmaster.brawl(furion)
print(furion)
print(beastmaster)

print(beastmaster)
beastmaster.train()
print(beastmaster)

print(furion)
print(beastmaster)
beastmaster.roar(furion)
print(furion)
print(beastmaster)

# Checking Invoker's methods

print(invoker)
print(beastmaster)
invoker.curse(beastmaster)
print(invoker)
print(beastmaster)

print(invoker)
invoker.summon()
print(invoker)

print(invoker)
print(beastmaster)
invoker.cast_spell(beastmaster)
print(invoker)
print(beastmaster)