# Importing The Modules
import pygame
import sys
import random
from os import path

snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 1000
HEIGHT = 550
FPS = 15

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Blue_color = (179, 255, 224)

font_name = pygame.font.match_font('Comic Sans MS')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (100, 95))
        self.image.set_colorkey(Blue_color)
        self.rect = self.image.get_rect()
        self.radius = 28
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (WIDTH / 7, HEIGHT / 4)
        self.speed_y = random.randrange(6, 12)

    def update(self):
        self.rect.y += self.speed_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            jump_sound.play()
            self.rect.y -= 42
        if self.rect.top < -10:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('img/Flying_cycle_1.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_2.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_3.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_4.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_5.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_6.png').convert())
        self.sprites.append(pygame.image.load('img/Flying_cycle_7.png').convert())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .65 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.width)
        self.rect.x = random.randrange(1100, 1200)
        self.speed_x = random.randrange(8, 15)
        self.speed_y = random.randrange(-3, 3)

    def update(self):
        self.rect.x -= self.speed_x
        self.current_sprite += 1

        if self.rect.left < 0:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.x = random.randrange(1100, 1200)
            self.speed_y = random.randrange(2, 5)
            self.speed_y = random.randrange(-3, 3)

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.image.set_colorkey(Blue_color)


class Thunder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('img/Cloud img_1.png').convert())
        self.sprites.append(pygame.image.load('img/Cloud img_2.png').convert())
        self.sprites.append(pygame.image.load('img/Cloud img_4.png').convert())
        self.sprites.append(pygame.image.load('img/Cloud img_6.png').convert())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(Blue_color)
        self.radius = int(self.rect.width * .55 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.y = random.randrange(0, 350)
        self.rect.x = random.randrange(1100, 1200)
        self.speed_x = random.randrange(2, 7)
        self.speed_y = random.randrange(-3, 3)

    def update(self):
        self.rect.x -= self.speed_x
        self.current_sprite += 1

        if self.rect.left < 0:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.x = random.randrange(1100, 1200)
            self.speed_y = random.randrange(2, 5)
            self.speed_y = random.randrange(-3, 3)

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.image.set_colorkey(Blue_color)


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time - 4
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(500, 50))
    screen.blit(score_surf, score_rect)
    return current_time - 4


# General setup
pygame.init()
pygame.mixer.init()
start_time = 0
score = 0
test_font = pygame.font.Font('font/Pixel_type.ttf', 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Air Jumper')
clock = pygame.time.Clock()


def show_go_screen():
    screen.fill(BLACK)
    draw_text(screen, "Air Jumper", 78, WIDTH / 2, HEIGHT / 4 - 50)
    draw_text(screen, "• Space key to jump", 28, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "• Stay away from birds and clouds", 28, WIDTH / 2 + 93, HEIGHT / 2 + 50)
    draw_text(screen, "Press any key to begin ...", 23, WIDTH / 2, HEIGHT * 3 / 4)
    draw_text(screen, "By Ravindu Senevirathne", 19, WIDTH / 4 + 620, HEIGHT * 3 / 4 + 95)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Loading the Game graphics
background = pygame.image.load('img/Sky.jpg')
background_rect = background.get_rect()
player_img = pygame.image.load('img/Player.png')

# Loading all game sounds
jump_sound = pygame.mixer.Sound(path.join(snd_dir, 'jump_01 - Copy.mp3'))
pygame.mixer.music.load(path.join(snd_dir, 'Background_sound.mp3'))
pygame.mixer.music.set_volume(2)

pygame.mixer.music.play(loops=-1)

# Game loop
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        score = 0
        all_sprites = pygame.sprite.Group()
        moving_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)
        for i in range(3):
            enemy = Bird()
            moving_sprites.add(enemy)
            mobs.add(enemy)

        thunder = Thunder()
        moving_sprites.add(thunder)
        mobs.add(thunder)

        score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()
    moving_sprites.update()

    # Checking the collisions
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits or player.rect.bottom > 549 or player.rect.top < 0:
       running = False

    # Drawing
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    score = display_score()
    all_sprites.draw(screen)
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
