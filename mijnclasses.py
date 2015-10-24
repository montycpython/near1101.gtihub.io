# -*- coding: UTF-8 -*-
from time import sleep
from random import choice, randint
things = ("energy","element","molecule","planet",
          "archebacteria","eubacteria","protist","fungi",
          "plant","animal","human","alien",
          "divinity") # list vs tuples: changeable, less memory efficient

energy = {} # remember the dict is also called map or hash table and can contain class instances or any data type
energy["name"] = "dark energy"
energy["unit"] = "dark bits"
energy["quantity"] = "the amount of free memory on master device"

class Energy(object):
    """
    A measure of a system's ability to do work
    """
    # classes package attributes (variables) and actions (functions) http://www.astrotheme.com/astrology_houses.php
    def __init__(self):
        self.twee = self.twoEnergies()
        self.zes = self.sixEnergies()
        self.joules = self.kracht()
    def twoEnergies(self):
        Twee = ("Potential","Kinetic")
        twee = choice(Twee)
        return twee
    def sixEnergies(self):
        six_blacks = {1:"chemical",2:"electrical",3:"mechanical",4:"nuclear",5:"radiant",6:"thermal"}
        zes = choice(six_blacks.values())
        return zes
    def kracht(self):
        joules = randint(1,400)
        return joules
    def __repr__(self):
        return "The Creator said, Let there be %s %s Energy times %d!\nAnd it was good." % (self.twee, self.zes.title(), self.joules)

class Hero(Energy):
    def __init__(self, name=None, gender=None):
        if gender is None:
            genders = ["male","female"]
            self.gender = choice(genders)

        elif gender is True or gender.lower.startswith('m'):
            self.gender = "male"
        
        elif gender is False or gender.lower.startswith('f') or gender.lower.startswith('w'):
            self.gender = "female"

        else:
            genders = ["male","female"]
            self.gender = choice (genders)
            
        if name is None:
            self.name = self.christen()
        elif not name:
            self.name = self.christen()

        if self.gender == "male":
            self.thirdperson = "he"
            self.possessive = "his"
            self.objective = "him"
            self.classname = "hero"
        elif self.gender == "female":
            self.thirdperson = "she"
            self.possessive = "her"
            self.objective = "her"
            self.classname = "heroine"


        super(Hero, self).__init__()
        
        self.attackStrength = self.joules / 10
        self.currency = 5

    def eat(self, food):
        if food == "watermelon":
            print "Our hero %s ate some watermelon." % self.name
            self.joules += 10
            sleep(1)
            print "%s energy went to %d." % (self.possessive.title(), self.joules)
        elif food == "chicken":
            print "Our hero %s ate some chicken." % self.name
            self.joules += 20
            sleep(1)
            print "%s energy shot to %d." % (self.possessive.title(), self.joules)
        else:
            print "Our hero %s ate some %s." % (self.name, food)
            self.joules -= 50
            sleep(2)
            print "%s energy dropped to %d." % (self.possessive.title(), self.joules)
            if self.joules <= 0:
                print "%s died because of it." % self.thirdperson.title()

    def christen(self):
        if self.gender == "male":
            names = ["Socrates","Plato","Aristotle","Pythagorus","Archimedes","Homer","Ramses","Tutankhamun","Blæc",
                 "Peracles","Aristophanes","Blake","Weisse"]
            return choice(names)
        else:
            names = ["Pythia","Eva","Solana","Venus","Elizabeth","Sophia"]
            return choice(names)

    def virtue(self):
        greek = ("justice","temperance","courage","piety","wisdom")
        return choice(greek)

    def attackEnemy(self, hero):
        if self.name == hero.name:
            self.name = "{} the Elder".format(self.name)
            hero.name = "{} the Younger".format(hero.name)
        hero.joules -= self.attackStrength
        if hero.joules <= 0:
            print "{} was the cause of {}'s death.".format(self.name, hero.name)
            self.joules += self.joules / 100
            self.currency += hero.currency / 2
        elif self.joules <= 0:
            print "{} was the cause of {}'s death.".format(hero.name, self.name)
            hero.joules += hero.joules / 100
            hero.currency += self.currency / 2
        else:
            print "{} hurt {} for {} joules!".format(self.name, hero.name, self.attackStrength)

    def __repr__(self):
        if self.joules <= 0:
            return "There once went a %s called %s;\n%s was filled with %s %s Energy;\n%s had %d Dead Joules of it.\n" % (self.classname, self.name, self.thirdperson.title(), self.twee.title(), self.zes.title(), self.thirdperson.title(), self.joules)
        else:
            return "There once went a %s called %s;\n%s was filled with %s %s Energy;\n%s had %d Living Joules of it.\n" % (self.classname, self.name, self.thirdperson.title(), self.twee.title(), self.zes.title(), self.thirdperson.title(), self.joules)

def mijnclasses():
    x = Energy()
    print x
    moon = Hero()
    sun = Hero()
    print moon
    print sun
    foods = ["watermelon","chicken","shit"]
    moon.eat(choice(foods))
    moon.eat(choice(foods))
    moon.eat(choice(foods))
    sun.eat(choice(foods))
    sun.eat(choice(foods))
    sun.eat(choice(foods))
    print moon
    print sun
    while moon.joules >= 1 and sun.joules >= 1:
        moon.attackEnemy(sun)
        sun.attackEnemy(moon)
    print moon
    print sun

    

if __name__ == "__main__":
    mijnclasses()
