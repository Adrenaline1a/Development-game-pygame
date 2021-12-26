import pygame
from menu import *
import sqlite3
import Game1 as Gm


class Game():
    def __init__(self, text=''):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 720, 720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.COLOR_INACTIVE = pygame.Color(255, 11, 22, 0)
        self.COLOR_ACTIVE = pygame.Color(155, 122, 0, 0)
        self.FONT = pygame.font.Font(None, 32)
        self.input_box = (self.DISPLAY_W/3*1.67, self.DISPLAY_H/2, 140, 32)
        self.rect = pygame.Rect(self.input_box)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(self.text, True, self.color)
        self.active = False
        self.conn = sqlite3.connect("Game_BD.db")
        self.cursor = self.conn.cursor()
        #self.main_menu = Login(self)
        self.main_menu = MainMenu(self)
        self.MainMenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.registration = Logg(self)
        self.gaming = Gm.main()
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if self.active:
                    if event.key == pygame.K_PLUS:
                        Logg(self)
                        self.text += ''
                    elif event.key == pygame.K_MINUS:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = self.FONT.render(self.text, True, self.color)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

