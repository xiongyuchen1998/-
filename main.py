import pygame
import sys
import traceback
import myplane
import enemy
from pygame.locals import *


pygame.init()
pygame.mixer.init()


bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")



background = pygame.image.load("images/background.png").convert()


# 载入游戏音乐
pygame.mixer.music.load("sound/back.mp3")
pygame.mixer.music.set_volume(0.2)

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    pygame.mixer.music.play(-1)

    # 生成我方飞机
    me = myplane.MyPlane(bg_size)
    


    # 生成敌方飞机
    enemies = pygame.sprite.Group()
    # 生成小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # 生成中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 15)
    # 生成大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 15)
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #检测用户的键盘操作
        key_pressd = pygame.key.get_pressed()

        if key_pressd[K_w] or key_pressd[K_UP]:
            me.moveUp()
            
        if key_pressd[K_s] or key_pressd[K_DOWN]:
            me.moveDown()
            
        if key_pressd[K_a] or key_pressd[K_LEFT]:
            me.moveLeft()
            
        if key_pressd[K_d] or key_pressd[K_RIGHT]:
            me.moveRight()

        
        screen.blit(background,(0,0))

        # 绘制大型敌机
        for each in big_enemies:
            each.move()
            screen.blit(each.image, each.rect)

        # 绘制中型敌机
        for each in mid_enemies:
            each.move()
            screen.blit(each.image, each.rect)

        # 绘制小型敌机
        for each in small_enemies:
            each.move()
            screen.blit(each.image, each.rect)

        # 绘制我方飞机
        screen.blit(me.image,me.rect)
        
        pygame.display.flip()
        
        clock.tick(60)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
