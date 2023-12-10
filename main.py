#!/usr/bin/python3
""" the Snowflakes Surprises Game """
import pygame
import time
import sys
import random
from models.snowflake import Snowflake
from models.player import Player

pygame.init()

# the icon and the caption
pygame.display.set_caption("Snowflakes Surprises")
icon = pygame.image.load("data/assets/snowflake120px.png")
pygame.display.set_icon(icon)

# initialzing the screen
screen_info = pygame.display.Info()
SW, SH = screen_info.current_w, screen_info.current_h # curr screen size
IW, IH = 800, 600                                     # Initial height/width
WS, HS = SW / IW, SH / IH                             # Height/width scale
screen = pygame.display.set_mode((IW, IH))
font = pygame.font.Font(None, 36)

# The snowflakes
all_sprites = pygame.sprite.Group()
snowflakes = pygame.sprite.Group()

# The Player
player = Player(IW, IH)
player.move(0)
player.draw(screen)

for _ in range(50):
    snowflake = Snowflake(IW, IH)
    snowflake.update(player)
    all_sprites.add(snowflake)
    snowflakes.add(snowflake)

def main():
    global screen
    # the intro screen
    game_intro()

    running = True
    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                screen = handle_resize(event)
            elif event.type == pygame.QUIT:
                running = False
        for snowflake in snowflakes:
            snowflake.update(player)

        player.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


def handle_resize(event):
    """ handle resizing the screen """
    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    return screen


def game_intro():
    global screen

    intro = True

    while intro:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    intro = False

        icon_rect = icon.get_rect(center=(IW // 2, IH // 2.5))
        screen.blit(icon, icon_rect)

        text_img = font.render("Please press enter to start", True, "white")
        text_rect = text_img.get_rect(center=(IW // 2, IH * 2 // 3))
        screen.blit(text_img, text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
