import turtle as trtl
import random
import time
from skill_class import Skill
from entity_class import entity

# Player intialization
player_skill1 = Skill(4, 4, 3, "Player Skill 1", 3) # Base power 4, Coin power 4, 3 coins, 3 uses
player_skill2 = Skill(5, 5, 3, "Player Skill 2", 2) # Base power 5, Coin power 5, 3 coins, 2 uses
player_skill3 = Skill(8, 6, 2, "Player Skill 3", 1) # Base power 8, Coin power 6, 2 coins, 1 use

player_skills = [player_skill1, player_skill2, player_skill3]

player = entity(100, player_skills)

# Enemy initialization
enemy_skill1 = Skill(3, 3, 4, "Enemy Skill 1", 3) # Base power 3, Coin power 3, 4 coins, 3 uses
enemy_skill2 = Skill(4, 4, 4, "Enemy Skill 2", 2) # Base power 4, Coin power 4, 4 coins, 2 uses
enemy_skill3 = Skill(6, 5, 3, "Enemy Skill 3", 1) # Base power 6, Coin power 5, 3 coins, 1 use

enemy_skills = [enemy_skill1, enemy_skill2, enemy_skill3]

enemy = entity (100, enemy_skills)

testing = True

def clashing(p_skill, e_skill):
    p_coins = p_skill.initial_coins()
    e_coins = e_skill.initial_coins()
    clash = True
    while clash:
        p_num = p_skill.calculate(p_coins)
        e_num = e_skill.calculate(e_coins)
        print("Player rolls a " + str(p_num))
        if not testing:
            time.sleep(0.5)
        print("Enemy rolls a " + str(e_num))
        if not testing:
            time.sleep(0.5)
        if p_num > e_num:
            e_coins -= 1
            if not testing:
                time.sleep(0.5)
            print("Enemy loses 1 coin and has " + str(e_coins) + " remaining!")
        elif e_num > p_num:
            p_coins -= 1
            if not testing:
                time.sleep(0.5)
            print("Player loses 1 coin and has " + str(p_coins) + " remaining!")
        if not testing:
            time.sleep(1)
        print(" ")
        #nobody loses coins if roll same number
        if e_coins == 0:
            loser = "Enemy" #placeholder, change later to enemy object
            damage_num = p_skill.calculate(p_coins)
            skill_name = p_skill.get_name()
            print("Player attacks with " + str(p_coins) + " coins!")
            p_skill.change_uses(False)
            print("Player has " + str(p_skill.get_uses()) + " uses of " + str(p_skill.get_name()) + " remaining!")
            clash = False
        elif p_coins == 0:
            loser = "Player" #placeholder, change later to player object
            damage_num = e_skill.calculate(e_coins)
            skill_name = e_skill.get_name()
            print("Enemy attacks with " + str(e_coins) + " coins!")
            e_skill.change_uses(False)
            print("Enemy has " + str(e_skill.get_uses()) + " uses of " + str(e_skill.get_name()) + " remaining!")
            clash = False
    return loser, damage_num, skill_name

def print_clash_results(results):
    loser, damage_to_take, skills_name = results
    print(print(loser + " takes " + str(damage_to_take) + " damage to " + skills_name + "!"))

def player_select_skill():
    list_of_skills = player.get_skills()
    print("Here are your skills: \n")
    for skill in list_of_skills:
        print(skill.__read__())
        print(" ")
    print("Reminder: Your skill uses will refresh once all your skills are used \n")
    selecting = True
    while selecting:
        request = int(input("Please enter the skill you would like to use as an integer (1, 2, or 3): "))
        selected = player.get_skill(request - 1)
        if selected.get_uses() <= 0:
            print("Please select a skill with uses remaining")
        else:
            selecting = False
    return selected

while True:
    selected_skill = player_select_skill()
    print_clash_results(clashing(selected_skill, enemy_skill1))