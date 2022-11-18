import game_framework
import pygame
import Main_sm

running = True
image = True
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

logo_time = 0.0

def enter():
    global image
    image = pygame.image.load('logo.png')
    pass

def exit():
    global image
    del image
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_framework.quit()

        if event.type == pygame.KEYDOWN and pygame.K_SPACE:
            game_framework.change_state(Main_sm)

def update():
    pass

def draw():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, image.get_rect())
    pygame.display.flip()
    pass

