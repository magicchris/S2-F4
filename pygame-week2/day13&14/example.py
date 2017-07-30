# -*- coding: utf-8 -*-
import pygame
WIDTH = 640
HEIGHT = 480

def screen_show(screen):
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 100)
    text = font.render("XXXXXX", True, [255,0,0])
    screen.blit(text, [0,100])
    img = pygame.image.load("beach_ball.png")
    screen.blit(img, [0, 0])    
    pygame.display.flip()


def w_down_cb():
    pass

def s_down_cb():
    pass

def a_down_cb():
    pass

def d_down_cb():
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True

    while running:
        pygame.time.delay(200) # 50ms
        screen_show(screen)

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
