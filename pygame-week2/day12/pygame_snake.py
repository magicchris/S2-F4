# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #蛇前进的方向

snake = [[8,3],[9,3],[10,3]]
apple = [3,1]

def screen_result(screen):
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 100)
    text = font.render("You Lose!!!", True, [255,0,0])
    screen.blit(text, [0,100])
    pygame.display.flip()

def screen_show(screen):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()

def snake_update():
    global dirt,apple
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == apple:
        snake.insert(0, new_body)
    else:
        snake.insert(0, new_body)
        snake.pop()
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        apple = get_new_position(apple)
        pygame.time.delay(100)
    # if (snake[0][0] == 0 or snake[0][0] == WIDTH or snake[0][1] == 0 or snake[0][1] == HEIGHT) or (snake[0] in snake[1:]):
    if snake[0] in snake[1:]:
        screen1 = pygame.display.set_mode([WIDTH, HEIGHT])
        screen_result(screen1)
        pygame.time.delay(1000)
        pygame.quit()

def get_new_position(apple_b):
    lst = apple_b[:]
    is_new = True
    while is_new:
        if lst[0] == apple_b[0] and lst[1] == apple_b[1]:
            is_new = False
        if is_new:
            break
        else:
            lst[0] = random.randint(1, SCALE - 1)
            lst[1] = random.randint(1, SCALE - 1)
    return lst

def w_down_cb():
    global dirt
    if snake[0][1] <= snake[1][1]:
        dirt = 0

def s_down_cb():
    global dirt
    if snake[0][1] >= snake[1][1]:
        dirt = 2

def a_down_cb():
    global dirt
    if snake[0][0] <= snake[1][0]:
        dirt = 1

def d_down_cb():
    global dirt
    if snake[0][0] >= snake[1][0]:
        dirt = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    running  = True

    while running:

        snake_update()
        if len(snake) <= 4:
            pygame.time.delay(600)
        elif len(snake) <= 6:
            pygame.time.delay(400)
        else:
            pygame.time.delay(200)
        screen_show(screen)
        # get_new_position(apple)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()
