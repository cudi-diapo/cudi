import os
import re
import sys
import time
import pygame
import random


class EnvCudi:
    def get_image(self):
        try:
            self.image = pygame.image.load(f"media/archillect{self.num}.jpg")
        except Exception as e:
            print(e)
            self.num = 0
            return
        width = self.image.get_width()
        height = self.image.get_height()
        if width >= height:
            self.ratio = width / height
            w = int(width * 2) % self.max_w
            rand = random.randint(int(width / 4), w if w > int(width / 2) else int(width * 0.8))
            self.image = pygame.transform.scale(self.image, (int(rand * self.ratio), int(rand)))
        else:
            self.ratio = height / width
            h = int(height * 2) % self.max_h
            rand = random.randint(int(height / 4),  h if h > int(height / 2) else int(height * 0.8))
            self.image = pygame.transform.scale(self.image, (int(rand), int(rand * self.ratio)))

    def __init__(self):
        self.on = True
        self.num = 0
        self.ratio = 1
        self.width = 1280
        self.height = 720
        self.image = None
        self.max_w = int(self.width * 0.80)
        self.max_h = int(self.height * 0.80)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption('cudi')
        while self.image is None:
            self.get_image()
        pygame.display.update()

    def event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.on = False
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.on = False
                    break


def process_aff(t_name, timer, num_min, num_max):
    print(f"Enter {t_name} - timer = {timer}")
    env = EnvCudi()
    time.sleep(5 if timer != 0 else 10)
    try:
        while env.on:
            env.screen.blit(env.image, (random.randint(-100, env.max_w), random.randint(-100, env.max_h)))

            wait_time = time.time()
            env.num = env.num + 1 if env.num < num_max else num_min
            env.get_image()
            env.event()
            try:
                if timer:
                    time.sleep(timer - (time.time() - wait_time))
            except ValueError as e:
                print(f"{e}\nImage downloading and drawing last more than a second: {time.time() - wait_time}")
            pygame.display.update()

            env.event()
            pygame.time.Clock().tick(timer)
    except pygame.error as e:
        print(e)
    pygame.quit()
    sys.exit(1)

