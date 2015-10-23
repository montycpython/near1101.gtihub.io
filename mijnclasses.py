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
        return "... %s %s Energy times %d!\nAnd it was good." % (x.twee, x.zes.title(), x.joules)

class Hero(Energy):
    def __init__(self, name=None):
        if name:
            self.name = name
        elif not name:
            self.name = self.christen()
        self.currency = 5
        super(Hero, self).__init__()
    def eat(self, food):
        if food == "apple":
            print "Our hero %s ate an apple." % self.name
            self.joules += 10
            sleep(1)
            print "His energy went to %d." % self.joules
        elif food == "ham":
            print "Our hero %s ate some ham." % self.name
            self.joules += 20
            sleep(1)
            print "His energy shot to %d." % self.joules
        else:
            print "Our hero %s ate some %s." % (self.name, food)
            self.joules -= 50
            sleep(2)
            print "His energy dropped to %d." % self.joules
    def christen(self):
        names = ["Socrates","Plato","Aristotle","Pythagorus","Archimedes","Homer","Ramses","Tutankhamun","Blæc",
                 "Peracles","Sophia","Aristophanes"]
        return choice(names)
    def virtue(self):
        greek = ("justice","temperance","courage","piety","wisdom")
        return choice(greek)
    def __repr__(self):
        return "There once went a hero called %s;\nHe was filled with %s %s Energy;\nHe had %d Joules of it." % (self.name, self.twee.title(), self.zes.title(), self.joules)
if __name__ == "__main__":
    x = Energy()
    print x
    moon = Hero()
    print moon
    moon.eat("apple")
    moon.eat("ham")
    moon.eat("shit")
    print moon
