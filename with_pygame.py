import pygame
import numpy as np
pygame.init()

SCREEN_WIGHT = 800 ; SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIGHT,SCREEN_HEIGHT))

print("\nПоворат точки x,y.")
x = int(input("x: "))
y = int(input("y: "))

print("\nОтносительно a,b.")
a = int(input("a: "))
b = int(input("b: "))

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

run = True

while run :
    screen.fill(white)
    pygame.draw.circle(screen,black,(x,y),4)
    pygame.draw.circle(screen,black,(a,b),4)
    
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_ESCAPE]:
        theta = np.pi
        new_x = (x-a)*np.cos(theta)-(y-b)*np.sin(theta)+a
        new_y = (x-a)*np.sin(theta)+(y-b)*np.cos(theta)+b
        print(new_x,new_y)
        pygame.draw.circle(screen,"green",(new_x,new_y),4)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

    pygame.display.update()

pygame.quit()