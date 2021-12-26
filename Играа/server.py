import random
import socket
import pygame

FPS = 100
W_ROOM, H_ROOM = 4000, 4000
W_SERVER_WINDOW, H_SERVER_WINDOW = 300, 300

colours = {
    '0': (255, 255, 0),
    '1': (255, 0, 0),
    '2': (0, 255, 0),
    '3': (0, 0, 255),
    '4': (0, 255, 255),
    '5': (128, 0, 128)
}


def find(s):
    otkr = None
    for i in range(len(s)):
        if s[i] == '<':
            otkr = i
        if s[i] == '>' and otkr!= None:
            zakr = i
            res = s[otkr+1:zakr]
            list(map(int, res.split(',')))
            return res
    return ''


class Player():
    def __init__(self, conn, addr, x, y, r, color):
        self.conn = conn
        self.addr = addr
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.error = 0
        self.abs_speed = 1
        self.speed_x = 0
        self.speed_y = 0

    def change_speed(self, V):
        if (V[0] == 0) and (V[1] == 0):
            self.speed_x = 0
            self.speed_y = 0
        else:
            lenv = (V[0]**2+V[1]**2) ** 0.5
            V = (V[0]/lenv, V[1]/lenv)
            V = (V[0]*self.abs_speed, V[1]*self.abs_speed)
            self.speed_x, self.speed_y = V[0], V[1]

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y


main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 6665))
main_socket.setblocking(False)
main_socket.listen(5)

pygame.init()
screen = pygame.display.set_mode((W_SERVER_WINDOW, H_SERVER_WINDOW))
clock = pygame.time.Clock()

players = []
server_works = True
while server_works:
    clock.tick(FPS)
    try:
        new_socket, addr = main_socket.accept()
        print('Подключился', addr)
        main_socket.setblocking(False)
        new_player = Player(new_socket, addr, random.randint(0, W_ROOM), random.randint(0, H_ROOM),
                            50, str(random.randint(0, 5)))
        players.append(new_player)
    except:
        pass
    for player in players:
        try:
            data = player.conn.recv(1024).decode()
            data = find(data)
            print(data)
            player.change_speed(data)
            player.update()
        except:
            pass
        player.update()
    for player in players:
        try:
            player.conn.send('Новое состояние игры'.encode())
            player.error = 0
        except:
            player.error += 1

    for player in players:
        if player.error == 500:
            player.conn.close()
            players.remove(player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            server_works = False
    screen.fill((0, 0, 0))
    for player in players:
        x = round(player.x * W_SERVER_WINDOW/W_ROOM)
        y = round(player.y * H_SERVER_WINDOW / H_ROOM)
        r = round(player.r * W_SERVER_WINDOW/W_ROOM)
        c = colours[player.color]
        pygame.draw.circle(screen, c, (x, y), r)
    pygame.display.update()
pygame.quit()
main_socket.close()
