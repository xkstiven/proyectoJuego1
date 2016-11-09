import pygame
from juegolib import *
import os
#definicion colores
ANCHO = 400
ALTO = 600
VERDE=[0,255,0]
AZUL= [0,0,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
MORADO=[255,0,255]
AMARILLO=[255,255,0]
GRIS=[137,137,137]
BLANCO=[255,255,255]

def CargarFondo(archivo,ancho_corte,alto_corte):#carga una imagen y la dicide como una matriz
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho ,img_alto = imagen.get_size()
    #print img_alto , '' , img_ancho
    matriz_fondo=[]
    for fila in range(0,int(img_ancho/ancho_corte)):
        linea=[]
        for columna in range(0, int(img_alto/alto_corte)):
            cuadro = (fila*ancho_corte,columna*alto_corte,ancho_corte,alto_corte)
            linea.append(imagen.subsurface(cuadro))
        matriz_fondo.append(linea)
    return matriz_fondo

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar la pantalla en el SO
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])   # se crea la pantalla de jeugo
    fondo=pygame.image.load("imagenes/map.png")
    animal = CargarFondo('imagenes/atacantes.png',32,32)
    barrasup= pygame.image.load("imagenes/barra.png")
    barrainf= pygame.image.load("imagenes/barrainf.png")   # carga de imagenes
    pantalla.blit(barrainf,(0,530))
    pantalla.blit(fondo,(0,0))
    pantalla.blit(barrasup,(0,0))    # se imprimen las imagenes en la pantalla

    todos=pygame.sprite.Group()    # no es todos solo son los iconos
    torres=pygame.sprite.Group()     # grupos de sprites para las coliciones y los iconos
    iconos=pygame.sprite.Group()
    atacantes=pygame.sprite.Group()
    balas=pygame.sprite.Group()

    ico1=icono(3)   #se crea el primer icono y como parametro el costo de la tropa a crear
    ico1.image=pygame.image.load('imagenes/ico1.png')
    ico1.id=1
    ico1.rect.y=ALTO-54   # poicicion del icono
    ico1.rect.x=30
    todos.add(ico1)   # se agrega a los grupos
    iconos.add(ico1)

    ico1=icono(4)
    ico1.image=pygame.image.load('imagenes/ico2.png')
    ico1.id=2
    ico1.rect.y=ALTO-50
    ico1.rect.x=134
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono(4)
    ico1.image=pygame.image.load('imagenes/ico3.png')
    ico1.id=3
    ico1.rect.y=ALTO-50
    ico1.rect.x=234
    todos.add(ico1)
    iconos.add(ico1)

    ico1=icono(5)
    ico1.image=pygame.image.load('imagenes/ico4.png')
    ico1.id=4
    ico1.rect.y=ALTO-50
    ico1.rect.x=334
    todos.add(ico1)
    iconos.add(ico1)

    tor1=Torre()   # torre de defensa 1 izquierda
    tor1.rect.y= 120
    tor1.rect.x= 48
    torres.add(tor1)

    tor2=Torre()   # torre derecha
    tor2.rect.y= 120
    tor2.rect.x= 288
    torres.add(tor2)

    disparo=pygame.mixer.Sound("sonidos/silencer.ogg")   # cargan sonidos que se ejecutaran en ciertas acciones
    golpe=pygame.mixer.Sound("sonidos/hit10.ogg")
    tordown= pygame.mixer.Sound("sonidos/synt.ogg")
    moneda=pygame.mixer.Sound("sonidos/coin.ogg")

    temporizador = 20  # temporizador para crear elixir
    temporDis= 40    # temporizador para manejo de disparos
    elixir= 6   # elixir inicial
    max_tropas= 15   # maximo de tropas para el caso de perder el juego si se llega a cero
    cont=0
    reloj=pygame.time.Clock()   # reloj del jeugo
    fin=False
    while not fin:
        os.system("cls")  # limpia la pantalla en windows en linux cambiar por "clear"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.MOUSEBUTTONDOWN:   #evalua si hay una colicion con un icono
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        #print ("icono " + str(ic.id))
                        if ic.id ==1:   #  se hace un case para evaliar cual icono se presiono
                            if elixir >= ic.costo:
                                b = atk1()     # si ic.id == se crea objeto atk1 y se descuenta su costo
                                elixir -= ic.costo
                                temporizador=10
                                cont += 1
                                max_tropas -= 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==2:
                            if elixir >= ic.costo:
                                b = atk2()
                                elixir -= ic.costo
                                temporizador=10
                                cont += 1
                                max_tropas -= 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        elif ic.id ==3:
                            if elixir >= ic.costo:
                                b = atk3()
                                elixir -= ic.costo
                                temporizador=10
                                cont += 1
                                max_tropas -= 1
                                b.id = cont
                                b.rect.center = pygame.mouse.get_pos()
                        else:
                            if elixir >= ic.costo:
                                b = atk4()
                                elixir -= ic.costo
                                temporizador=10
                                cont += 1
                                max_tropas -= 1
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
                for bl in atacantes:   # cuando se suelta se evalua en que pocicion se solto el objeto
                    if bl.click == True:
                        bl.click = False

                        if bl.rect.x < 200:
                            bl.var_x *= -1
                            bl.dir=1

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
        if (temporizador==0 and elixir<10):  # se crea una gota de elixir cada 24 ciclos
            elixir += 1
            temporizador = 24

        if elixir >= 10:
            moneda.play()   # se reproduce una advertencia si el elixir es igual a 10 que es el limite de elicir

        if max_tropas <= 0:   #condicion de parada si se gastaron todas las tropas se pierde
            fin=True
            print ("GAME OVER")
            print ("YOU LOSE")


        for tor in torres:   # evalua si la vida de la torre es menor que 0 para quetarla de la lista y dejar de dibujarla
            if tor.vida <= 0:
                torres.remove(tor)
                tordown.play()
        '''if tor1.vida > 0:
            print("torre1=",tor1.vida)
        if tor2.vida > 0:
            print("torre2=",tor2.vida)'''
        print ("tropas restantes: ",max_tropas)
        if tor1.vida <= 0 and tor2.vida <=0:
            fin=True
            print ("WIN")


        if (temporDis <= 0):
            if tor1.vida >= 0:
                b1=Bala(tor1.rect.center[0]-8,(tor1.rect.center[1]+32))
                balas.add(b1)
            if tor2.vida >= 0:
                b2=Bala(tor2.rect.center[0]-8,(tor2.rect.center[1]+32))
                balas.add(b2)
            if tor1.vida > 0 or tor2.vida > 0:# si alguna de las torres puede disparas se reproduce el sonido
                disparo.play()
            temporDis= 25

        for bal in balas:
            if bal.rect.y >= 348:
                balas.remove(bal)

        n=0
        pantalla.blit(fondo,(0,0))
        pantalla.blit(barrasup,(0,0))
        pantalla.blit(barrainf,(0,530))
        #pygame.draw.rect(pantalla,GRIS,[0,530,400,600]) #espacio iconos
        #pygame.draw.rect(pantalla,NEGRO,[0,0,600,40])  # espacio tiempo y elixir (cantidad para comprar tropas)

        for atac in atacantes:
            atac.image = animal[atac.ind + atac.con][atac.dire]  # cambia la imagen del atacante para simular caminate
            coli = pygame.sprite.spritecollide(atac,torres,False)
            for elemento in coli:
                atac.var_x=0
                elemento.vida -= atac.dano
                atacantes.remove(atac)
            if atac.vida <= 0:
                golpe.play()
                atacantes.remove(atac)

        for bal in balas:
            coli = pygame.sprite.spritecollide(bal,atacantes,False)
            for elemento in coli:
                elemento.vida -= bal.dano
                balas.remove(bal)

        while n <= elixir-1:# ciclo para mostrar el elixir en la barra superir
            xposini=(n*40)+5
            pygame.draw.rect(pantalla,MORADO,[xposini,10,30,10])
            n += 1
        #pygame.draw.rect(pantalla,AZUL,[0,364,400,32])   #Rio central solo decorativo
        atacantes.update(pantalla)  # se actualiza el grupo de los atacantes
        if tor1.vida>0:    # funciones apra mostrar la barra de vida restante de la torre
            pygame.draw.rect(pantalla,ROJO,[48,117,64,3])
            pygame.draw.rect(pantalla,AZUL,[48,117,int(tor1.vida/47),3])
        if tor2.vida>0:
            pygame.draw.rect(pantalla,ROJO,[288,117,64,3])
            pygame.draw.rect(pantalla,AZUL,[288,117,int(tor2.vida/47),3])
        balas.update(pantalla)
        todos.update(pantalla)  # se actualizan los grupos y se dibujan
        torres.update(pantalla)
        #todos.draw(pantalla)
        pygame.display.update()
        reloj.tick(15)
        #print (elixir)
        temporizador -= 1
        temporDis -= 1
