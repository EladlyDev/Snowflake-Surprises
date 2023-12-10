#!/usr/bin/python3
""" This module contains the ``Player`` class """
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, SW, SH):
        super().__init__()

        self.score = 0
        self.SH = SH
        self.SW = SW

        self.width = 50         # idea: a magicflake to make the box bigger
        self.height = 50

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 128, 255), (0, 0, self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = SW // 2 - self.width // 2
        self.rect.y = SH - self.height - 10

    def move(self, dx):
        self.rect.x = max(0, min(self.SW - self.width, self.rect.x + dx))

    def draw(self, screen, snowflakes, font):
        for snowflake in snowflakes:
            screen.blit(snowflake.image, snowflake.rect)

        screen.blit(self.image, self.rect)

        score_text = font.render(f"Score: {self.score}", True, "white")
        screen.blit(score_text, (10, 10))
