#import libraries

import pygame

#define classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.part_of_image(0, 750, 59, 122)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.speedx = 0
        self.speedy = 0
        self.count_run_right = 0
        self.count_run_left = 0
    def change_image_right(self, x, y, w, h):
        self.image = spritesheet.part_of_image(x, y, w, h)
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.flip(self.image, False, False)
    def change_image_left(self, x, y, w, h):
        self.image = spritesheet.part_of_image(x, y, w, h)
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.flip(self.image, True, False)
    def update(self):
        self.speedx = 0
        self.speedy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.speedy -= 10
        elif key[pygame.K_DOWN]:
            self.speedy += 10
        elif key[pygame.K_RIGHT]:
            self.speedx += 3
            self.count_run_right += 1
            if self.count_run_right == 5:
                self.change_image_right(73, 750, 59, 122)
            if self.count_run_right == 10:
                self.change_image_right(140, 748, 66, 123)
            if self.count_run_right == 15:
                self.change_image_right(216, 748, 69, 123)
            if self.count_run_right == 20:
                self.change_image_right(306, 748, 64, 123)
            if self.count_run_right == 25:
                self.change_image_right(385, 748, 64, 123)
            if self.count_run_right == 30:
                self.change_image_right(0, 750, 59, 122)
                self.count_run_right = 0
        elif key[pygame.K_LEFT]:
            self.speedx -= 3
            self.count_run_left += 1
            if self.count_run_left == 5:
                self.change_image_left(73, 750, 59, 122)
            if self.count_run_left == 10:
                self.change_image_left(140, 748, 66, 123)
            if self.count_run_left == 15:
                self.change_image_left(216, 748, 69, 123)
            if self.count_run_left == 20:
                self.change_image_left(306, 748, 64, 123)
            if self.count_run_left == 25:
                self.change_image_left(385, 748, 64, 123)
            if self.count_run_left == 30:
                self.change_image_left(0, 750, 59, 122)
                self.count_run_left = 0
        elif not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.image = spritesheet.part_of_image(0, 905, 60, 140)
            self.image.set_colorkey(WHITE)
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 0
        if self.rect.bottom > HEIGHT - 120:
            self.rect.bottom = HEIGHT - 120
        if self.rect.top < 200:
            self.rect.top = 200
        if self.rect.right > WIDTH/3:
            self.rect.right = WIDTH/3
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + 100
        self.rect.y = HEIGHT - 400
        self.speedx = 10
        self.count_bullet_release = 0
    def update(self):
        self.count_bullet_release += 1
        if self.count_bullet_release == 20:
            bullet_enemy = Bullet_Enemy(self.rect.center, self.rect.bottom)
            bullets_enemy.add(bullet_enemy)
            all_sprites.add(bullet_enemy)
            self.count_bullet_release = 0
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.left = WIDTH

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explode.part_of_image(0, 0, 200, 190)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.counter = 0
    def update(self):
        self.counter += 1
        if self.counter == 3:
            self.image = explode.part_of_image(200, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 6:
            self.image = explode.part_of_image(400, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 9:
            self.image = explode.part_of_image(400, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 12:
            self.image = explode.part_of_image(600, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 15:
            self.image = explode.part_of_image(800, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 18:
            self.image = explode.part_of_image(1000, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 21:
            self.image = explode.part_of_image(1200, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
        if self.counter == 24:
            self.image = explode.part_of_image(1350, 0, 200, 190)
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.image.set_colorkey(BLACK)
            self.kill()

class Bullet_Enemy(pygame.sprite.Sprite):
    def __init__(self, center, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.part_of_image(573, 48, 28, 22)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.bottom = bottom
    def update(self):
        self.rect.y += 3
        if self.rect.top > HEIGHT:
            self.kill()

class SpriteSheet:
    def __init__(self, image):
        self.image_sprite = pygame.image.load(image).convert_alpha()
    def part_of_image(self, x, y, w, h):
        image_surface = pygame.Surface((w, h))
        image_surface.blit(self.image_sprite, (0, 0), (x, y, w, h))
        return image_surface

#intialize pygame

pygame.init()

#set up the game window

WIDTH = 800
HEIGHT = 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Police")

background = pygame.image.load("background.png")
spritesheet = SpriteSheet("police.png")
explode = SpriteSheet("explosion.png")

#define additional functions and procedures

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemy = Enemy()
enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites.add(enemy)

bullets_enemy = pygame.sprite.Group()
explosions = pygame.sprite.Group()

x = 0
y = 0

#start the main game loop

while True:
    clock.tick(30)

    #check for events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(WHITE)

    screen.blit(background, (x, y))

    #update sprites

    all_sprites.update()
    
    if player.speedx is not 0 and player.speedx > 0 and player.rect.right < WIDTH and x > -3800:
        x -= 3
    if player.speedx is not 0 and player.speedx < 0 and player.rect.left > 0:
        x += 1

    player_collide_with_bomb = pygame.sprite.spritecollide(player, bullets_enemy, True)

    for hit in player_collide_with_bomb:
        explosion = Explosion(hit.rect.center)
        explosions.add(explosion)
        all_sprites.add(explosion)
    
    #redraw window
        
    all_sprites.draw(screen)
    
    pygame.display.flip()

