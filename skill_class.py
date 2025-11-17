import random

class Skill:

    def __init__(self, base_power, coin_power, coin_num, name, uses):
        self.b_power = base_power
        self.c_power = coin_power
        self.c_num = coin_num
        self.name = name
        self.initial_uses = uses
        self.uses_left = uses
    
    def __read__(self):
        #AI generated, very simple line but long so I just had AI make it for me, I added the \n
        return "Skill name: " + self.name + "\n Base power: " + str(self.b_power) + "\n Coin_power: " + str(self.c_power) + "\n Number of coins: " + str(self.c_num) + " \n You have " + str(self.uses_left) + " uses of this skill left"    
    
    def get_name(self):
        return self.name

    def initial_coins(self):
        return self.c_num
    
    def get_uses(self):
        return self.uses_left
    
    def change_uses(self, refresh):
        if refresh == True:
            self.uses_left = self.initial_uses
        else:
            self.uses_left -= 1

    def calculate(self, coins):
        final_power = self.b_power
        for i in range(0, coins):
            headsortails = random.randint(1,2)
            if headsortails == 1:
                final_power += self.c_power
        
        return final_power