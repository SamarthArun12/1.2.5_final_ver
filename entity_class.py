class entity:
    def __init__(self, health, skills):
        self.hp = health
        self.skills = skills
    
    def get_skills(self):
        return self.skills

    def get_skill(self, index):
        return self.skills[index]