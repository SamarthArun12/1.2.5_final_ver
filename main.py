import time
from skill_class import Skill
from entity_class import entity
import random

#pygame initialization
import pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


#colors, AI written
white  = (255, 255, 255)
black  = (0, 0, 0)
red    = (255, 0, 0)
green  = (0, 255, 0)
blue   = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
gray   = (128, 128, 128)
dark_gray = (50, 50, 50)

#fonts
arial_small = pygame.font.SysFont("Arial", 20)
arial_medium = pygame.font.SysFont("Arial", 30)
arial_large = pygame.font.SysFont("Arial", 50)

background = pygame.image.load("BOBackground.jpeg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#lines 35 to 44 AI generated, nothing really to change I just didn't want to type the line out a bunch
# Player Sprites
player_idle   = pygame.transform.scale(pygame.image.load("1.2.5_anims/player_idle.png").convert_alpha(), (116, 104))
player_attack = pygame.transform.scale(pygame.image.load("1.2.5_anims/player_attack.png").convert_alpha(), (116, 104))
player_hurt   = pygame.transform.scale(pygame.image.load("1.2.5_anims/player_hurt.png").convert_alpha(), (116, 104))
player_move   = pygame.transform.scale(pygame.image.load("1.2.5_anims/player_move.png").convert_alpha(), (116, 104))

# Enemy Sprites
enemy_idle = pygame.transform.scale(pygame.image.load("1.2.5_anims/enemy_idle.png").convert_alpha(), (300, 400))
enemy_hurt = pygame.transform.scale(pygame.image.load("1.2.5_anims/enemy_hurt.png").convert_alpha(), (300, 400))
enemy_move = pygame.transform.scale(pygame.image.load("1.2.5_anims/enemy_move.png").convert_alpha(), (300, 400))
enemy_win  = pygame.transform.scale(pygame.image.load("1.2.5_anims/enemy_win.png").convert_alpha(), (300, 400))


# Player intialization
player_skill1 = Skill(4, 4, 3, "Player Skill 1", 3) # Base power 4, Coin power 4, 3 coins, 3 uses
player_skill2 = Skill(5, 5, 3, "Player Skill 2", 2) # Base power 5, Coin power 5, 3 coins, 2 uses
player_skill3 = Skill(8, 6, 2, "Player Skill 3", 1) # Base power 8, Coin power 6, 2 coins, 1 use
player_skills = [player_skill1, player_skill2, player_skill3]
player = entity(100, player_skills, 100, 320)

# Enemy initialization
enemy_skill1 = Skill(3, 3, 4, "Enemy Skill 1", 3) # Base power 3, Coin power 3, 4 coins, 3 uses
enemy_skill2 = Skill(4, 4, 4, "Enemy Skill 2", 2) # Base power 4, Coin power 4, 4 coins, 2 uses
enemy_skill3 = Skill(6, 5, 3, "Enemy Skill 3", 1) # Base power 6, Coin power 5, 3 coins, 1 use
enemy_skills = [enemy_skill1, enemy_skill2, enemy_skill3]
enemy = entity(100, enemy_skills, 650, 120)

initialize_chars = True
testing = True


def clashing(player, enemy, p_skill, e_skill):
    player = player
    enemy = enemy
    p_coins = p_skill.initial_coins()
    e_coins = e_skill.initial_coins()
    clash = True
    win_log = []
    coin_log = []
    loser = None
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
            win_log.append("player")
            coin_log.append((p_num, e_num))
            print("Enemy loses 1 coin and has " + str(e_coins) + " remaining!")
        elif e_num > p_num:
            p_coins -= 1
            if not testing:
                time.sleep(0.5)
            win_log.append("enemy")
            coin_log.append((e_num, p_num))
            print("Player loses 1 coin and has " + str(p_coins) + " remaining!")
        if not testing:
            time.sleep(1)
        print(" ")
        #nobody loses coins if roll same number

        if e_coins == 0 and loser is None:
            loser = enemy
            loser_name = "enemy"
            winner_skill = p_skill
            damage_num = winner_skill.calculate(p_coins)
            skill_name = winner_skill.get_name()
            print("Player attacks with " + str(p_coins) + " coins!")
            print("Player has " + str(p_skill.get_uses()) + " uses of " + str(p_skill.get_name()) + " remaining!")
            clash = False
        if p_coins == 0 and loser is None:
            loser = player 
            loser_name = "player"
            winner_skill = e_skill
            damage_num = winner_skill.calculate(e_coins)
            skill_name = winner_skill.get_name()
            print("Enemy attacks with " + str(e_coins) + " coins!")
            print("Enemy has " + str(e_skill.get_uses()) + " uses of " + str(e_skill.get_name()) + " remaining!")
            clash = False
    p_skill.change_uses(False)
    e_skill.change_uses(False)
    return loser, damage_num, skill_name, loser_name, win_log, coin_log

def print_clash_results(results):
    loser, damage_to_take, skills_name, loser_name = results
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

def skill_refreshing(player_or_enemy):
    skills = player_or_enemy.get_skills()
    refresh_skills = True
    for skill in skills:
        if skill.get_uses() > 0:
            refresh_skills = False
    if refresh_skills == True:
        for skill in skills:
            skill.change_uses(True)

def draw_text(text, font, color, x, y):
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def draw_health_bar(entity_obj, x, y, width, height):
    # Max HP
    pygame.draw.rect(screen, black, (x, y, width, height), 0, 5) 
    # Current HP
    health_width = (entity_obj.get_hp() / entity_obj.max_hp) * width
    pygame.draw.rect(screen, red, (x, y, health_width, height), 0, 5)
    # HP text
    hp_text = "HP: " + str(entity_obj.get_hp()) + "/" + str(entity_obj.max_hp)
    draw_text(hp_text, arial_small, black, x + width/2, y + 5)


def draw_ui():
    global initialize_chars

    #Healthbars
    draw_health_bar(player, 50, 50, 300, 30)
    draw_health_bar(enemy, 650, 50, 300, 30)
    draw_text("Player", arial_medium, white, 50, 10)
    draw_text("Enemy", arial_medium, white, 650, 10)

    if initialize_chars:
        screen.blit(player_idle, (100, 320))
        screen.blit(enemy_idle, (650, 120))
    
    # Draw Information based on State
    if state == "select_skill":
        draw_text("Select Skill (Press 1, 2, or 3)", arial_medium, white, 400, 380)
        # Display skills
        skills = player.get_skills()
        for skill in skills:
             i = skills.index(skill)
             draw_text("[" + str(i) + "]" + skill.get_name() + " (Uses: " + str(skill.get_uses()) + ")", arial_small, white, 100, 450 + i * 30)
             if skill.get_uses() <= 0:
                 draw_text("No uses remain", arial_small, red, 300, 450 + i * 30)

    elif state == "clash_result":
        loser, damage_to_take, skill_name, loser_name, win_log, coin_log = results
        
        result_text = loser_name + " takes " + str(damage_to_take) + " damage from " + skill_name + "!"
        draw_text(result_text, arial_medium, white, 400, 450)
        
        skill_refreshing(player)
        skill_refreshing(enemy)
             
        draw_text("SPACE to continue to next turn", arial_small, white, 400, 550)
    
    elif state == "game_over":
        winner = "player" if enemy.get_hp() <= 0 else "enemy" 
        draw_text("GAME OVER!", arial_large, red, 350, 250) 
        draw_text(winner + " wins", arial_large, blue, 375, 300)
        draw_text("Esc to exit", arial_small, white, 900, 550)

def animate_clash(win_log, coin_log):

    global player, enemy
    px, py = player.get_pos()
    ex, ey = enemy.get_pos()

    #line 210 AI generated
    for index, winner in enumerate(win_log):
        midpoint = (px + ex)/2
        dist = midpoint - px
        offset = 116
        if winner == "player":
            p_coin, e_coin = coin_log[index]
        elif winner == "enemy":
            e_coin, p_coin = coin_log[index]
        draw_text(str(p_coin), arial_medium, white, 50, 100)
        draw_text(str(e_coin), arial_medium, white, 650, 100)
        for i in range(10):
            screen.blit(background, (0,0))
            #was too many variables to unpack
            final_px = px + (i * dist/10) - offset
            final_ex = ex - (i * dist/10)
            screen.blit(background, (0,0)) 
            screen.blit(player_move, (final_px, py))
            screen.blit(enemy_move, (final_ex, ey))
            draw_text(str(p_coin), arial_medium, white, 50, 100)
            draw_text(str(e_coin), arial_medium, white, 650, 100)
            draw_ui()
            pygame.display.flip()
            time.sleep(0.05)
        if winner == "player":
            screen.blit(background, (0,0)) 
            screen.blit(player_idle, (midpoint - offset, py))
            screen.blit(enemy_hurt, (midpoint, ey))
            draw_ui()
            pygame.display.flip()
            time.sleep(0.5)
        if winner == "enemy":
            screen.blit(background, (0,0))
            screen.blit(player_hurt, (midpoint - offset, py))
            screen.blit(enemy_win, (midpoint, ey))
            draw_ui()
            pygame.display.flip()
            time.sleep(0.5)


#AI made the event system with pygame and the key press detection, but I implemented all my functions myself
def game_loop():
    global state, results, player, enemy

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if state == "select_skill":
                    e_skill_index = random.randint(0,2)
                    enemy_skill = enemy.get_skill(e_skill_index)
                    e_skill = enemy_skill
                    draw_text("Enemy is using its skill " + str(e_skill_index + 1), arial_medium, white, 450, 500)
                    
                    #checks which skill was going to be used
                    if event.key == pygame.K_1:
                        selected_skill = 0
                    elif event.key == pygame.K_2:
                        selected_skill = 1
                    elif event.key == pygame.K_3:
                        selected_skill = 2

                    #only lets a valid skill be selected
                    p_skill = player.get_skill(selected_skill)
                    if p_skill.get_uses() > 0:
                        
                        #clashing returns a tuple with 6 elements
                        results = clashing(player, enemy, p_skill, e_skill)

                        screen.blit(background, (0, 0))
                        draw_ui()
                        pygame.display.flip()
                        #elements of 5 and 6 of the results are logs of the winners of micro-clashes and the numbers they rolled
                        animate_clash(results[4], results[5])
                        #take the damage after the animations
                        results[0].take_damage(results[1])

                        if player.get_hp() <= 0 or enemy.get_hp() <= 0:
                            state = "game_over"
                        else:
                            state = "clash_result"

                    else:
                        print("No uses remaining")
                elif state == "clash_result" and event.key == pygame.K_SPACE:
                    state = "select_skill"
                    results = None
                elif state == "game_over" and event.key == pygame.K_ESCAPE:
                    running = False
                
        screen.blit(background, (0, 0))
        draw_ui()

        #makes changes visible
        pygame.display.flip()
        
        clock.tick(60) 

    pygame.quit()

state = "select_skill"
if __name__ == "__main__":
    print("Sprites from Limbus Company, I was trying to make my own but too busy")
    print("They make ghosts fight because I can't figure out how to make them fight")
    game_loop()

