import socket
import pygame


W_Window, H_Window = 1080, 720
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(("localhost", 6665))
pygame.init()
screen = pygame.display.set_mode((W_Window, H_Window))
pygame.display.set_caption("Царь горы")

old_V = (0, 0)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        V = (pos[0]-W_Window//2, pos[1]-H_Window//2)
        if V[0] ** 2 + V[1]**2 <= 50**2:
            V = (0, 0)
        if V != old_V:
            old_V = V
            message = '<'+str(V[0])+','+str(V[1])+'>'
            sock.send(message.encode())
    data = sock.recv(1024).decode()
    screen.fill((255, 155, 21, 0))
    pygame.draw.circle(screen, (255, 0, 0), (W_Window//2, H_Window//2), 50)
    pygame.display.update()
pygame.quit()
