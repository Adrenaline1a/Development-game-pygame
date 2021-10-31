import pygame as pg
from pygame.sprite import Group


class Knight(pg.sprite.Sprite):
    def __init__(self, screen):
        super(Knight, self).__init__()
        self.screen = screen
        self.image = pg.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 1100
        self.center = float(self.rect.x)
        self.rect.bottom = self.screen_rect.bottom
        self.mleft = 0
        self.attack = 1
        self.hp = 10
        self.dead = False

    def output(self):
        if self.hp > 0:
            self.screen.blit(self.image, self.rect)

    def update(self):
        if self.mleft and self.rect.left > 0:
            self.rect.x -= 0.5
    def test(self):
        print('hi')

class Monster:
    """Создание основных параметров персножа"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pg.image.load("images/pixil-frame-0_1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 0
        self.center = float(self.rect.x)
        self.rect.bottom = self.screen_rect.bottom + 50
        self.mright = 0
        self.hp = 5

    """Отрисовка персонажа"""
    def output(self):
        self.screen.blit(self.image, self.rect)

    """Перемещение персонажа"""
    def update(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        self.rect.x = self.center


"""События: движение, выход"""


def controls(screen, evil, bullet):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            new_bullet = Bullet(screen, evil)
            bullet.add(new_bullet)


class Bullet(pg.sprite.Sprite):
    """Пуля"""
    def __init__(self, screen, evil):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ball_radius = 5
        self.ball_rect = int(self.ball_radius * 2)
        self.rect = pg.Rect(0, 0, self.ball_rect, self.ball_rect)
        self.color = (0, 0, 0)
        self.speed = 5
        self.rect.centery = evil.rect.centery + 20
        self.rect.centerx = evil.rect.centerx + 35
        self.x = float(self.rect.x)
        self.attack = 2

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect, self.ball_radius)


def windowUpdate(screen, evil, bg_color, bullet, hero):
    screen.fill(bg_color)
    for bullets in bullet.sprites():
        bullets.draw_bullet()
    evil.output()
    hero.output()
    pg.display.flip()


def bullet_update(bullet, hero, test_group):
    bullet.update()
    for bullets in bullet.copy():
        if bullets.rect.right >= 1100:
            bullets.remove(bullet)
    collisions = pg.sprite.groupcollide(test_group, bullet, False, True)
    if collisions:
        hero.hp -= bullets.attack
        print(hero.hp)
        if hero.hp == 0:
            hero.remove(test_group)
            del hero


def main():
    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("Evolution")
    bg_color = (255, 255, 0)
    evil = Monster(screen)
    hero = Knight(screen)
    test_group = Group()
    test_group.add(hero)
    bullet = Group()
    while True:
        pg.time.delay(15)
        hero.mleft -= 0.5
        controls(screen, evil, bullet)
        hero.update()
        evil.update()
        bullet_update(bullet, hero, test_group)
        windowUpdate(screen, evil, bg_color, bullet, hero)


main()
