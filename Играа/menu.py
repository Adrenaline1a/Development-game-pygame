import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class Login(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Login"
        self.DISPLAY_W, self.DISPLAY_H = 720, 720
        self.bg = pygame.image.load('fone/-1.png')
        self.loginx, self.loginy = self.mid_w, self.mid_h + 30
        self.regx, self.regy = self.mid_w, self.mid_h + 50
        self.quitx, self.quity = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.loginx + self.offset, self.loginy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.bg, (0, 0))
            self.game.draw_text('Select the login method', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Login", 20, self.loginx, self.loginy)
            self.game.draw_text("Registration", 20, self.regx, self.regy)
            self.game.draw_text("Quit", 20, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Login':
                self.cursor_rect.midtop = (self.regx + self.offset, self.regy)
                self.state = 'Registration'
            elif self.state == 'Registration':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.loginx + self.offset, self.loginy)
                self.state = 'Login'
        elif self.game.UP_KEY:
            if self.state == 'Login':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Registration':
                self.cursor_rect.midtop = (self.loginx + self.offset, self.loginy)
                self.state = 'Login'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.regx + self.offset, self.regy)
                self.state = 'Registration'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Login':
                self.game.curr_menu = self.game.registration
            elif self.state == 'Registration':
                self.game.curr_menu = self.game.registration
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Quit", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Quit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.MainMenu
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            quit()


class Logg(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.inp = game.text
        self.loggx, self.loggy = self.mid_w, self.mid_h + 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Регистрация', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Логин: ", 20, self.loggx, self.loggy)
            self.update()
            self.draw()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

    def update(self):
        width = max(200, self.game.txt_surface.get_width()+10)
        self.game.rect.w = width

    def draw(self):
        self.game.display.blit(self.game.txt_surface, (self.game.rect.x+5, self.game.rect.y+5))
        pygame.draw.rect(self.game.display, self.game.color, self.game.rect, 2)
        self.game.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                           login  TEXT,
                           password TEXT 
                            )""")
        self.game.conn.commit()
        self.game.cursor.execute(f"SELECT login FROM users WHERE login = '{self.inp}'")
        if self.game.cursor.fetchone() is None:
            self.game.cursor.execute(f"INSERT INTO users VALUES (?, ?)", (self.inp, self.inp))
            self.game.conn.commit()
        else:
            self.game.draw_text("Такая запись уже есть", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/3)
