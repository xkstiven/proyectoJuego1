import pygame
from juegolib import *
import os

ANCHO = 400
ALTO = 600
VERDE=[0,255,0]
AZUL= [0,0,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
GRIS=[137,137,137]
BLANCO=[255,255,255]

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    todos=pygame.sprite.Group()
    iconos=pygame.sprite.Group()
    atacantes=pygame.sprite.Group()

    ico1=icono()
    ico1.id=1
    ico1.rect.y=ALTO-50
    ico1.rect.x=34
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono()
    ico1.id=2
    ico1.rect.y=ALTO-50
    ico1.rect.x=134
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono()
    ico1.id=3
    ico1.rect.y=ALTO-50
    ico1.rect.x=234
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono()
    ico1.id=4
    ico1.rect.y=ALTO-50
    ico1.rect.x=334
    todos.add(ico1)
    iconos.add(ico1)

    tor1=Torre()
    tor1.rect.y= 120
    tor1.rect.x= 48
    todos.add(tor1)

    tor2=Torre()
    tor2.rect.y= 120
    tor2.rect.x= 288
    todos.add(tor2)

    cont=0
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                if b.rect.collidepoint(event.pos):
                    b.click = True
                '''
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print ("icono " + str(ic.id))
                        if ic.id ==1:
                            b = atk1()
                            cont += 1
                            b.id = cont
                            b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==2:
                            b = atk2()
                            cont += 1
                            b.id = cont
                            b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==3:
                            b = atk3()
                            cont += 1
                            b.id = cont
                            b.rect.center = pygame.mouse.get_pos()
                        else:
                            b = atk4()
                            cont += 1
                            b.id = cont
                            b.rect.center = pygame.mouse.get_pos()


                        col = True
                        while col:
                            col = False
                            colision = pygame.sprite.spritecollide(b,atacantes,False)
                            for bl in colision:
                                if b.id != bl.id:
                                    b.rect.left = bl.rect.right
                                    col = True

                        todos.add(b)
                        atacantes.add(b)

                for bl in atacantes:
                    if bl.rect.collidepoint(event.pos):
                        bl.click = True

            if event.type == pygame.MOUSEBUTTONUP:
                for bl in atacantes:
                    if bl.click == True:
                        bl.click = False
                        
                        if bl.rect.x < 200:
                            bl.var_x *= -1

                        if bl.rect.y < 364:
                            bl.rect.y = 365
                        col = True
                        while col:
                            col = False
                            colision = pygame.sprite.spritecollide(bl,atacantes,False)
                            for e in colision:
                                if bl.id != e.id:
                                    bl.rect.left = e.rect.right
                                    if bl.rect.x > ANCHO:
                                        bl.rect.x = ANCHO/2
                                    col = True

        pantalla.fill(BLANCO)
        pygame.draw.rect(pantalla,GRIS,[0,530,400,600]) #espacio iconos
        pygame.draw.rect(pantalla,NEGRO,[0,0,600,40])  # espacio tiempo y elixir (cantidad para comprar tropas)
        pygame.draw.rect(pantalla,AZUL,[0,332,400,32])   #Rio central solo decorativo
        todos.update(pantalla)
        todos.draw(pantalla)
        pygame.display.update()
        reloj.tick(15)
