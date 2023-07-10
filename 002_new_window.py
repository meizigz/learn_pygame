
import pygame
import sys
pygame.init()
wnd=pygame.display.set_mode((800,800))
while True:
    e=pygame.event.get()
    for i in e:
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()