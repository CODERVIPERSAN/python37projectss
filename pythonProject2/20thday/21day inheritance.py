# class inheritance
class Fish:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("intake of dissolved oxygen")


class BlueFish(Fish):
    def __init__(self):
        self.eyes = 34

    def swimming(self):
        super().breath()
        print("fish swim")


fish = BlueFish()
print(fish.childeye)
fish.breath()
fish.swimming()
print(fish.eyes)
##########################################################
# if somebody have created the main class then
# we can create the derived class on the top of the main class
# advantage is we can access the main class  by using only derived class
# we can make a connection between main class and child class
# we can also change the function in main class by using the
# derived class
###############################################################