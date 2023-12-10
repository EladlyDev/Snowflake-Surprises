#!/usr/bin/python3
""" this module contains the snowflake class """
import pygame
import random
import time


class Snowflake(pygame.sprite.Sprite):
    def __init__(self, SW, SH):
        super().__init__()

        self.size = random.randint(5, 20)
        self.score = random.randint(1, 10)
        self.rotation_angel = random.uniform(0, 360)

        self.SW = SW
        self.SH = SH
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.size / 2, self.size / 2), self.size / 2)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SW - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -1)

        self.speed = random.randint(2, 5)

        self.type = "normal"

    def update(self, player):
        self.rect.y += self.speed
        self.rotation_angel += 1

        if (pygame.sprite.collide_rect(self, player) and
        self.rect.centery < player.rect.centery):
            player.score += self.score
            self.reset()
        if self.rect.y > self.SH:
            self.type = "normal"
            self.reset()

    def reset(self):
        self.rect.y = random.randint(-self.rect.height, -1)
        self.rect.x = random.randint(0, self.SW - self.rect.width)

        if random.random() < 0.2:  # 2% chance to change size on each update
            self.type = random.choices(['normal', 'big', 'fire'],
                                       weights=[0, 1, 99])[0]

        # Adjust size based on whether it's big or small
        color = (255, 255, 255)
        if self.type == 'big':
            self.size = random.randint(40, 60)
            self.score = random.randint(100, 300) # increase the score
            color = (255, 255, 255)  # White
        elif self.type == 'fire':
            color = (255, 0, 0)  # Red
            self.size = 15
            self.score = -random.randint(100, 300)   # harm the score
        else:                        # normal
            self.size = random.randint(5, 20)
            self.score = int(random.random() * self.size)
            self.speed = random.randint(2, 5)


        # Update the image with the new size
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        rotated_image = pygame.transform.rotate(self.image, self.rotation_angel)
        self.image.blit(rotated_image, (0, 0))
        pygame.draw.circle(self.image, color, (self.size // 2, self.size // 2), self.size // 2)
