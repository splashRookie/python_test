import pygame
import sys
def run_game():
    screen = pygame.display.set_mode([900,580])
    background = pygame.image.load('./share.png').convert()
    Mario = pygame.image.load('./button_highlight.png').convert()
    offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0,pygame.K_UP:0,pygame.K_DOWN:0}

    while True:

        screen.blit(background, (0, 0))
        screen.blit(Mario, (30, 50))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in offset:
                    offset[event.key] = 3
            if event.type == pygame.KEYUP:
                if event.key in offset:
                    offset[event.key] = 0


        pygame.display.update()

run_game()