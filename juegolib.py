import pygame

VERDE=[0,255,0]
NEGRO=[0,0,0]
ROJO=[255,0,0]
GRIS=[137,137,137]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
VERAZUL=[0,255,255]
AZUL=[0,0,255]

class icono(pygame.sprite.Sprite):
    id=0
    def __init__(self,cost): #archivo
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(VERDE)
        self.click = False
        self.costo=cost

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

class Torre(pygame.sprite.Sprite):
    def __init__(self): #archivo
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([64,64])
        self.rect=self.image.get_rect()
        self.image.fill(ROJO)
        self.vida=3000

    def update(self,surface):
        surface.blit(self.image,self.rect)

class atk1(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(AMARILLO)
        self.click = False
        self.costo= 3
        self.ind=0
        self.con=0
        self.dire=2
        self.var_x=5
        self.var_y=0
        self.vida= 500
        self.daño= 200

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        elif self.rect.x <= 64:
            self.var_x = 0
            self.var_y = -5
            self.dire= 3
        elif self.rect.x >= 304:
            self.var_x=0
            self.var_y= -5
            self.dire= 3
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con<2 :
            self.con+=1
        else:
            self.con=0
        surface.blit(self.image,self.rect)

class atk2(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(NEGRO)
        self.click = False
        self.costo= 3
        self.ind=3
        self.dire=2
        self.con=0
        self.var_x=5
        self.var_y=0
        self.vida= 500
        self.daño= 200

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        elif self.rect.x <= 64:
            self.var_x = 0
            self.var_y = -5
            self.dire= 3
        elif self.rect.x >= 304:
            self.var_x=0
            self.var_y= -5
            self.dire= 3
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con<2 :
            self.con+=1
        else:
            self.con=0
        surface.blit(self.image,self.rect)

class atk3(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(AZUL)
        self.click = False
        self.costo= 3
        self.ind=6
        self.dire=2
        self.con=0
        self.var_x=5
        self.var_y=0
        self.vida= 500
        self.daño= 200

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        elif self.rect.x <= 64:
            self.var_x = 0
            self.var_y = -5
            self.dire= 3
        elif self.rect.x >= 304:
            self.var_x=0
            self.var_y= -5
            self.dire= 3
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con<2 :
            self.con+=1
        else:
            self.con=0
        surface.blit(self.image,self.rect)

class atk4(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(ROJO)
        self.click = False
        self.costo= 3
        self.var_x=5
        self.ind=9
        self.con=0
        self.dire=2
        self.var_y=0
        self.vida= 500
        self.daño= 200

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        elif self.rect.x <= 64:
            self.var_x = 0
            self.var_y = -5
            self.dire= 3
        elif self.rect.x >= 304:
            self.var_x=0
            self.var_y= -5
            self.dire= 3
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con<2 :
            self.con+=1
        else:
            self.con=0
        surface.blit(self.image,self.rect)

class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([16,16])
        self.rect=self.image.get_rect()
        self.image.fill(VERAZUL)
        self.rect.x=x
        self.rect.y=y
        self.var_y=5
        self.daño= 200

    def update(self,surface):
        self.rect.y += self.var_y
        surface.blit(self.image,self.rect)
