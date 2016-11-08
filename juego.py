import pygame
from juegolib import *
import os

ANCHO = 400
ALTO = 600
VERDE=[0,255,0]
AZUL= [0,0,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
MORADO=[255,0,255]
GRIS=[137,137,137]
BLANCO=[255,255,255]

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    todos=pygame.sprite.Group()
    torres=pygame.sprite.Group()
    iconos=pygame.sprite.Group()
    atacantes=pygame.sprite.Group()
    balas=pygame.sprite.Group()

    ico1=icono(3)
    ico1.id=1
    ico1.rect.y=ALTO-50
    ico1.rect.x=34
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono(3)
    ico1.id=2
    ico1.rect.y=ALTO-50
    ico1.rect.x=134
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono(3)
    ico1.id=3
    ico1.rect.y=ALTO-50
    ico1.rect.x=234
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono(3)
    ico1.id=4
    ico1.rect.y=ALTO-50
    ico1.rect.x=334
    todos.add(ico1)
    iconos.add(ico1)

    tor1=Torre()
    tor1.rect.y= 120
    tor1.rect.x= 48
    torres.add(tor1)

    tor2=Torre()
    tor2.rect.y= 120
    tor2.rect.x= 288
    torres.add(tor2)

    print (tor1.rect.center)
    print (tor2.rect.center)
    temporizador = 20
    temporDis= 40
    elixir= 5
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
                            if elixir >= ic.costo:
                                b = atk1()
                                elixir -= b.costo
                                cont += 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==2:
                            if elixir >= ic.costo:
                                b = atk2()
                                elixir -= b.costo
                                cont += 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==3:
                            if elixir >= ic.costo:
                                b = atk3()
                                elixir -= b.costo
                                cont += 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        else:
                            if elixir >= ic.costo:
                                b = atk4()
                                elixir -= b.costo
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

                        #todos.add(b)
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

                        if bl.rect.y < 395:
                            bl.rect.y = 396
                        if bl.rect.x < 60:
                            bl.rect.x = 150
                        if bl.rect.x > 308:
                            bl.rect.x = 250
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
        if (temporizador==0 and elixir<10):
            elixir += 1
            temporizador = 30
        if (temporDis <= 0):
            if tor1.vida >= 0:
                b1=Bala(tor1.rect.center[0]-8,(tor1.rect.center[1]+32))
                balas.add(b1)
            if tor2.vida >= 0:
                b2=Bala(tor2.rect.center[0]-8,(tor2.rect.center[1]+32))
                balas.add(b2)
            temporDis= 25

        for bal in balas:
            if bal.rect.y >= 348:
                balas.remove(bal)

        n=0
        pantalla.fill(BLANCO)
        pygame.draw.rect(pantalla,GRIS,[0,530,400,600]) #espacio iconos
        pygame.draw.rect(pantalla,NEGRO,[0,0,600,40])  # espacio tiempo y elixir (cantidad para comprar tropas)

        for atac in atacantes:
            coli = pygame.sprite.spritecollide(atac,torres,False)
            for elemento in coli:
                atac.var_x=0
                elemento.vida -= atac.daño
                atacantes.remove(atac)
            if atac.vida <= 0:
                atacantes.remove(atac)

        for bal in balas:
            coli = pygame.sprite.spritecollide(bal,atacantes,False)
            for elemento in coli:
                elemento.vida -= bal.daño
                balas.remove(bal)

        while n <= elixir-1:
            xposini=(n*40)+5
            pygame.draw.rect(pantalla,MORADO,[xposini,10,30,10])
            n += 1
        pygame.draw.rect(pantalla,AZUL,[0,364,400,32])   #Rio central solo decorativo
        atacantes.update(pantalla)
        balas.update(pantalla)
        todos.update(pantalla)
        torres.update(pantalla)
        #todos.draw(pantalla)
        pygame.display.update()
        reloj.tick(15)
        #print (elixir)
        temporizador -= 1
        temporDis -= 1
