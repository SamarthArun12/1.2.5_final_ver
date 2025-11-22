class entity:
    def __init__(self, health, skills, x, y):
        self.max_hp = health
        self.hp = health
        self.skills = skills
        self.x = x
        self.y = y
    
    def get_skills(self):
        return self.skills

    def get_skill(self, index):
        return self.skills[index]
    
    def take_damage(self, damage):
        self.hp -= damage
        return self.hp
    
    def get_hp(self):
        return self.hp
    
    def get_pos(self):
        return self.x, self.y
    
