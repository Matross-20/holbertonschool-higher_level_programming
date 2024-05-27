class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Test script for Dragon

# Instantiate an object of the Dragon class named draco
draco = Dragon()

# Demonstrate draco's abilities
draco.swim()  # Should print "The creature swims!"
draco.fly()   # Should print "The creature flies!"
draco.roar()  # Should print "The dragon roars!"
