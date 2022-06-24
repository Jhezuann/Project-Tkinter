from turtle import pos, width
import pygame
import random
import sys

#constantes
ANCHO=800
ALTO=600

NEGRO=(0,0,0)

#Carecteristica del jugador
size_jug=50
pos_jug=[ANCHO / 2, ALTO - size_jug *2]

ROJO=(250,0,0)

#Enemigo
size_Enemigo=50
pos_Enemigo=[random.randint(0, ANCHO - size_Enemigo),0]
AZUL=(0,0,250)


#ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))

game_over=False
clock=pygame.time.Clock()

#funciones
def detectarColision(pos_jug, pos_Enemigo):
    jx=pos_jug[0]
    jy=pos_jug[1]

    ex=pos_Enemigo[0]
    ey=pos_Enemigo[1]

    if (ex >= jx and ex <(jx + size_jug)) or (jx >= ex and jx < (ex + size_Enemigo)):
        if (ey >= jy and ey <(jy + size_jug)) or (jy >= ey and jy < (ey + size_Enemigo)):
            return True
        return False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            x=pos_jug[0]
            if event.key==pygame.K_LEFT:
                x -= size_jug
            if event.key==pygame.K_RIGHT:
                x += size_jug
            
            pos_jug[0] = x
    
    ventana.fill(NEGRO)
    if pos_Enemigo[1] >= 0 and pos_Enemigo[1] < ALTO:
        pos_Enemigo[1] += 20
    else:
        pos_Enemigo[0]=random.randint(0, ANCHO - size_Enemigo)
        pos_Enemigo[1] = 0

    #colisiones
    if detectarColision(pos_jug, pos_Enemigo):
        game_over=True
        

    #Enemigo
    pygame.draw.rect(ventana, AZUL, (pos_Enemigo[0], pos_Enemigo[1], size_Enemigo, size_Enemigo))

    #Jugador
    pygame.draw.rect(ventana, ROJO, (pos_jug[0], pos_jug[1], size_jug, size_jug))

    clock.tick(30)
    pygame.display.update()
