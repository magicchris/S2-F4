# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE *SIZE

snake = [[8,3],[7,3],[6,3]]
apple = [3,1]
head = snake[0]
last = snake[2]

def update_apple_position():
    global apple
    if apple[0] == snake[0][0] and apple[1] == snake[0][1]:
        apple = get_new_position(apple)

def update_snake_postion():
    pass

def get_new_position(apple_b):
    lst = apple_b[:]
    is_new = True
    while is_new:
        if lst[0] == apple_b[0] and lst[1] == apple_b[1]:
            is_new = False
        if is_new:
            break
        else:
            lst[0] = random.randint(0, 20)
            lst[1] = random.randint(0, 20)
    return lst

def snake_state(snake):
    if snake[0][1] == snake[1][1] and snake[0][1] == snake[2][1]:
        state = 'level'
    elif snake[0][0] == snake[1][0] and snake[0][0] == snake[2][0]:
        state = 'vertical'
    else:
        state = 'triangle'
    # if
    return state
def screen_show(screen):
    screen.fill([255,255,255])
    pygame.draw.rect(screen, [0, 155, 0], [snake[0][0] * SIZE, snake[0][1] * SIZE, SIZE - 1, SIZE - 1])
    for body in snake[1:]:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()



def w_down_cb():
    # head
    state = snake_state(snake)
    snake_old = snake[:]
    if state == 'level':
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][1] -= 1
    # elif state == 'vertical':
    #     snake[2] = snake[1]
    #     snake[1] = snake[0]
    #     sanke[0][1] -= 1
    else:
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][1] -= 1

def s_down_cb():
    state = snake_state(snake)
    snake_old = snake[:]
    if state == 'level':
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][1] += 1
    # elif state == 'vertical':
    #     snake[2] = snake[1]
    #     snake[1] = snake[0]
    #     sanke[0][1] -= 1
    else:
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][1] += 1

def a_down_cb():
    state = snake_state(snake)
    snake_old = snake[:]
    if state == 'level':
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][0] -= 1
    # elif state == 'vertical':
    #     snake[2] = snake[1]
    #     snake[1] = snake[0]
    #     sanke[0][1] -= 1
    else:
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][0] -= 1

def d_down_cb():
    state = snake_state(snake)
    snake_old = snake[:]
    if state == 'level':
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][0] += 1
    # elif state == 'vertical':
    #     snake[2] = snake[1]
    #     snake[1] = snake[0]
    #     sanke[0][1] -= 1
    else:
        snake[2] = snake_old[1]
        snake[1] = snake_old[0]
        snake[0][0] += 1

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True



    while running:
        pygame.time.delay(50) # 50ms
        screen_show(screen)
        update_apple_position()

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
        # print snake
    pygame.quit()

if __name__ == '__main__':
    main()
