#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, name, speed, x, y ):
        super().__init__()
        self.image = transform.scale(image.load(name),(50, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# ! sdsddsdsdsdsdsdsd
# TODO sdsddsdsddsdds
class Player(GameSprite):
    def update(self):
        
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x == 550:
            self.direction = "left"
        if self.rect.x == 300:
            self.direction = "right"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#создать окно
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
#создать объект фон
background = transform.scale(image.load('background.jpg'),(700, 500))

sprite1 = Player('hero.png', 10, 100, 100)
sprite2 = Enemy('cyborg.png', 5, 550, 250)
sprite3 = GameSprite('treasure.png', 0, 550, 400)
wall = Wall(0, 100, 0, 200, 0, 25, 250)
wall1 = Wall(0, 100, 0, 330, 250, 25, 250)
wall2 = Wall(0, 100, 0, 450, 0, 25, 250)

fps = 60
clock = time.Clock()
game = True
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
font.init()
font = font.Font(None, 70)
while game:
    window.blit(background, (0, 0))
    sprite1.reset()
    sprite2.reset()
    sprite3.reset()
    wall.draw_wall()
    wall1.draw_wall()
    wall2.draw_wall()
    keys = key.get_pressed()
    sprite1.update()
    sprite2.update()
    if sprite.collide_rect(sprite1, wall) or sprite.collide_rect(sprite1, wall1) or sprite.collide_rect(sprite1, wall2):
        sprite1.rect.x = 100
        sprite1.rect.y = 100
    if sprite.collide_rect(sprite1, sprite2):
        lose_label = font.render('You lose!', True, (0, 0, 0))
        window.blit(lose_label, (200, 250))
        display.update()
        time.delay(3000)
        game = False
    
    if sprite.collide_rect(sprite1, sprite3):
        win_label = font.render('You win!', True, (255, 215, 0))
        window.blit(win_label, (200, 250))
        display.update()
        time.delay(3000)
        game = False
    for e in event.get():
            if e.type == QUIT:
                game = False
    display.update()
    clock.tick(fps)