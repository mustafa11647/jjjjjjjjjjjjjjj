import math
import random
import pygame
screen_width=800
screen_heigth=500
player_start_X=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption("space invader")
icon=pygame.image.load('6.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('5.png')
playerx=player_start_X
playery=player_start_y
playerx_change=0
enemyimg=[]
enemyx=[]
enemyY=[]
enemyx_change=[]
enemyY_change=[]
num_of_enemies=6
for _i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('4.png'))
    enemyx.append(random.randint(0,screen_width-64))
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
bulletimg=pygame.image.load('j.png')
bulletx=0
bulletY=player_start_y
bulletx_change=0
bulletY_change=bullet_speed_y
bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
textY=10
over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyY,bulletx,bulletY):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyY-bulletY)**2)
    return distance<collision_distance

