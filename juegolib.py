import pygame

VERDE=[0,255,0]
NEGRO=[0,0,0]
ROJO=[255,0,0]
GRIS=[137,137,137]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
AZUL=[0,0,255]

class icono(pygame.sprite.Sprite):
    id=0
    def __init__(self): #archivo
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(VERDE)
        self.click = False

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
        self.var_x=5
        self.var_y=0
        self.vida= 500

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        elif self.rect.x <= 48:
            self.var_x = 0
            self.var_y = -5
        elif self.rect.x >= 318:
            self.var_x=0
            self.var_y= -5
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        surface.blit(self.image,self.rect)

class atk2(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(NEGRO)
        self.click = False
        self.var_x=0
        self.var_y=0

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

class atk3(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(AZUL)
        self.click = False
        self.var_x=0
        self.var_y=0

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

class atk4(pygame.sprite.Sprite):
    id=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,32])
        self.rect=self.image.get_rect()
        self.image.fill(ROJO)
        self.click = False
        self.var_x=0
        self.var_y=0

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)
