#!/usr/bin/python3
""" this module contains the snowflake class """
import pygame
import random


class Snowflake(pygame.sprite.Sprite):
    def __init__(self, SW, SH):
        super().__init__()

        self.size = random.randint(5, 20)

        self.SW = SW
        self.SH = SH
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.size / 2, self.size / 2), self.size / 2)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SW - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -1)

        self.speed = random.randint(2, 5)

        self.type = "normal"
    def update(self):
        self.rect.y += self.speed

        # Randomly determine if it's a big snowflake when resetting
        if self.type != "normal":
            self.type = "normal"
        if random.random() < 0.03:  # 1% chance to change size on each update
            self.type = random.choice(['normal', 'big', 'fire', 'heavy', 'light'])

        if pygame.sprite.collide_rect(self, player):
            self.reset()
            player.score += self.score
        elif self.rect.y > self.SH:
            self.reset()

    def reset(self):
        self.rect.y = random.randint(-self.rect.height, -1)
        self.rect.x = random.randint(0, self.SW - self.rect.width)


        # Adjust size based on whether it's big or small
        color = (255, 255, 255)
        if self.type == 'big':
            self.size = random.randint(40, 60)
            self.score = random.randint(50, 100) # increase the score
            color = (255, 255, 255)  # White
        elif self.type == 'fire':
            color = (255, 0, 0)  # Red
            self.size = 15
            self.score = -100   # harm the score
        elif self.type == 'heavy':
            self.size = 15
            color = (100, 100, 100)  # Dark gray
            pass                     # increase the speed
        elif self.type == 'light':
            self.size = 15
            color = (204, 204, 255)  # Light gray
            pass                     # reduce the speed
        else:                        # normal
            self.size = random.randint(5, 20)
            self.score = random.randint(1, 10)
            self.speed = random.randint(2, 5)


        # Update the image with the new size
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (self.size // 2, self.size // 2), self.size // 2)

        self.speed = random.randint(2, 5)
