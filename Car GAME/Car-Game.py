import pygame
import os
import random
pygame.init()

AUD_TEMA = pygame.mixer.Sound(os.path.join('Aud', 'theme.mp3'))
AUD_ERROR = pygame.mixer.Sound(os.path.join('Aud', 'error.mp3'))
AUD_SELECT = pygame.mixer.Sound(os.path.join('Aud', 'select.mp3'))
AUD_START = pygame.mixer.Sound(os.path.join('Aud', 'Start.mp3'))
AUD_CONTAGEM  = pygame.mixer.Sound(os.path.join('Aud', 'contagem.mp3'))
AUD_GAMEOVER = pygame.mixer.Sound(os.path.join('Aud', 'gameover.mp3'))

AUD_TEMA.set_volume(0.2)
AUD_ERROR.set_volume(200)
AUD_SELECT.set_volume(200)
AUD_START.set_volume(200)
AUD_CONTAGEM.set_volume(200)
AUD_GAMEOVER.set_volume(200)

IMAGEM_ESTRADA = pygame.transform.scale(pygame.image.load(os.path.join('images', 'estrada.png')), (500, 500))
IMAGEM_SETAS = pygame.transform.scale(pygame.image.load(os.path.join('images', 'setas.png')), (500, 500))
IMAGEM_TITULO = pygame.transform.scale(pygame.image.load(os.path.join('images', 'titulo.png')), (500, 500))
IMAGEM_SELECAO = pygame.transform.scale(pygame.image.load(os.path.join('images', 'selecao.png')), (63, 98))
IMAGEM_GO = pygame.transform.scale(pygame.image.load(os.path.join('images', 'GO.png')), (500, 500))
IMAGEM_1 = pygame.transform.scale(pygame.image.load(os.path.join('images', '1.png')), (500, 500))
IMAGEM_2 = pygame.transform.scale(pygame.image.load(os.path.join('images', '2.png')), (500, 500))
IMAGEM_3 = pygame.transform.scale(pygame.image.load(os.path.join('images', '3.png')), (500, 500))
IMAGEM_SOSETAS = pygame.transform.scale(pygame.image.load(os.path.join('images', 'sosetas.png')), (500, 500))
IMAGEM_EXPLOSAO = pygame.transform.scale(pygame.image.load(os.path.join('images', 'explosao.png')), (120, 120))

#Cálculo Seleção x = carrox - 8.1 y = carroy - 15
#Posição Inicial Carro1: x=228.5 y=400

IMAGENS_CARROS = [
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro1.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro2.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro3.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro4.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro5.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro6.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro7.png')), (45, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro8.png')), (45, 70))
]
#Width Carro = 45
#Pista1: x=103, Pista2: x=186, Pista3: x=269, Pista4: x=352

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('Fixedsys', 50)

def ir_para(ix, iy, dx, dy, vel):
    if ix != dx:
        if ix > dx:
            ix -= vel
        elif ix < dx:
            ix += vel
    elif iy != dy:
        if iy > dy:
            iy -= vel
        elif iy < dy:
            iy += vel
    return [ix, iy]

class Selecao:
    IMAGE = IMAGEM_SELECAO

    def __init__(self, x, y):
        self.x = x - 9.1
        self.y = y - 15

    def mover(self, direcaox, direcaoy):
        if (352 > self.x + direcaox > 20) and (350 > self.y + direcaoy > 150):
            self.x += direcaox
            self.y += direcaoy
            AUD_SELECT.play()
        else:
            AUD_ERROR.play()

    def mover_ate(self, x, y, vel):
        cod = ir_para(self.x, self.y, x, y, vel)
        self.x = cod[0]
        self.y = cod[1]

    def desenhar(self, tela):
        tela.blit(self.IMAGE, (self.x, self.y))

class Texto:
    def __init__(self, x, y, conteudo):
        self.x = x
        self.y = y
        self.conteudo = conteudo

    def mover_ate(self, x, y, vel):
        cod = ir_para(self.x, self.y, x, y, vel)
        self.x = cod[0]
        self.y = cod[1]

    def desenhar(self, tela):
        tela.blit(self.conteudo, (self.x, self.y))

class Cars:
    def __init__(self, x, y, conteudo):
        self.x = x
        self.y = y
        self.conteudo = conteudo
        self.velocidade = 5
        self.state = {'UP': False, 'DOWN': False, 'RIGHT': False, 'LEFT': False}
        self.laststate = "stop"
        self.laststate2 = "stop"

    def mover(self):
        if self.state['UP'] and self.laststate == 'up':
            if self.y - self.velocidade > 0:
                self.y -= self.velocidade
        if self.state['DOWN'] and self.laststate == 'down':
            if self.y + self.velocidade < (500 - IMAGENS_CARROS[0].get_height()):
                self.y += (self.velocidade + 5)
        if self.state['LEFT'] and self.laststate2 == 'left':
            if self.x - self.velocidade > 90:
                self.x -= self.velocidade
        if self.state['RIGHT'] and self.laststate2 == 'right':
            if self.x + self.velocidade < (500 - 90 - IMAGENS_CARROS[0].get_width()):
                self.x += self.velocidade


    def mover_ate(self, x, y, vel):
        cod = ir_para(self.x, self.y, x, y, vel)
        self.x = cod[0]
        self.y = cod[1]

    def desenhar(self, tela):
        tela.blit(self.conteudo, (self.x, self.y))

    def colidir(self, vias):
        col = False
        vias_mask = []
        car_mask = pygame.mask.from_surface(self.conteudo)
        for via in vias:
            via_mask = via.get_mask()
            vias_mask.append(via_mask)
            distancia = (round(self.x - via.x), round(self.y - via.y))
            ponto = car_mask.overlap(via_mask, distancia)
            if ponto:
                col = True
        return col

class Via:
    def __init__(self, x, carros, posi, n, vel):
        self.x = x
        self.lista = posi
        self.vel = vel
        self.n = n
        self.ale = -(random.choice([50, 100, 150, 200, 250, 300]))
        while True:
            if self.ale in self.lista:
                self.ale = -(random.choice([50, 100, 150, 200, 250, 300]))
            else:
                self.y = self.ale
                self.lista[self.n] = self.ale
                break
        self.veli = 5
        self.velf = 10
        self.carros = carros
        self.velo = random.randint(self.veli, self.velf)
        while True:
            if self.velo in self.vel:
                self.velo = -(random.choice([50, 150, 250, 350]))
            else:
                self.velocidade = self.velo
                self.lista[self.n] = self.velo
                break
        self.carro = random.choice(self.carros)

    def lancar_car(self):
        self.y += self.velocidade
        if self.y > 501:
            self.carro = random.choice(self.carros)
            self.ale = -(random.choice([50, 100, 150, 200, 250, 300]))
            while True:
                if self.ale in self.lista:
                    self.ale = -(random.choice([50, 100, 150, 200, 250, 300]))
                else:
                    self.y = self.ale
                    self.vel[self.n] = self.ale
                    break
            self.velo = random.randint(self.veli, self.velf)
            while True:
                if self.velo in self.vel:
                    self.velo = random.randint(self.veli, self.velf)
                else:
                    self.velocidade = self.velo
                    self.vel[self.n] = self.velo
                    break


    def desenhar(self, tela):
        tela.blit(self.carro, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.carro)

class Chao:
    VELOCIDADE = -7
    ALTURA = IMAGEM_ESTRADA.get_height()
    IMAGEM = IMAGEM_ESTRADA

    def __init__(self, x):
        self.x = x
        self.y1 = 0
        self.y2 = -self.ALTURA

    def mover(self):
        self.y1 -= self.VELOCIDADE
        self.y2 -= self.VELOCIDADE

        if self.y1 - self.ALTURA > 0:
            self.y1 = self.y2 - self.ALTURA
        if self.y2 - self.ALTURA > 0:
            self.y2 = self.y1 - self.ALTURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y1))
        tela.blit(self.IMAGEM, (self.x, self.y2))

tela = pygame.display.set_mode((500, 500))
relogio = pygame.time.Clock()
pygame.display.set_caption('Car GAME')
pygame.display.set_icon(pygame.image.load(os.path.join('images', 'carro1.png')))

best = 0
escala2 = 0
contagem = 0
again = True
while True:
    relogio.tick(30)
    if not again:

        estrada.mover()
        estrada.desenhar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if menu:
                    if evento.key == pygame.K_LEFT:
                        selecao.mover(-83, 0)
                    elif evento.key == pygame.K_RIGHT:
                        selecao.mover(83, 0)
                    elif evento.key == pygame.K_UP:
                        selecao.mover(0, -100)
                    elif evento.key == pygame.K_DOWN:
                        selecao.mover(0, 100)
                    elif evento.key == pygame.K_RETURN:
                        menu = False
                        AUD_START.play()
                        posi_carro1 = [round(selecao.x) + 8, selecao.y + 15]
                        for i, car in enumerate(carros):
                            if [car.x, car.y] == posi_carro1:
                                carro1 = Cars(228.5, 500, car.conteudo)
                                indexPOP = i

                if game:
                    if evento.key == pygame.K_LEFT:
                        carro1.laststate2 = 'left'
                        carro1.state['LEFT'] = True
                    if evento.key == pygame.K_RIGHT:
                        carro1.laststate2 = carro1.laststate
                        carro1.laststate2 = 'right'
                        carro1.state['RIGHT'] = True
                    if evento.key == pygame.K_UP:
                        carro1.laststate = 'up'
                        carro1.state['UP'] = True
                    if evento.key == pygame.K_DOWN:
                        carro1.laststate = 'down'
                        carro1.state['DOWN'] = True

                if restart > 100:
                    if evento.key == pygame.K_RETURN:
                        again = True

            if carro1:
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        carro1.state['LEFT'] = False
                    if evento.key == pygame.K_RIGHT:
                        carro1.state['RIGHT'] = False
                    if evento.key == pygame.K_UP:
                        carro1.state['UP'] = False
                    if evento.key == pygame.K_DOWN:
                        carro1.state['DOWN'] = False

        if not menu:
            estrada.VELOCIDADE = -7
            for carro in carros:
                carro.mover_ate(carro.x, -500, 10)
            selecao.mover_ate(selecao.x, -500, 10)
            titulo.mover_ate(500, titulo.y, 10)
            pontos.mover_ate(-500, pontos.y, 10)
            setas.mover_ate(500, titulo.y, 10)
            tempomenu += 1

        if tempomenu < 50:
            texto = FONTE_PONTOS.render(f"Your Best: {best}", 1, (255, 255, 255))
            for carro in carros:
                carro.desenhar(tela)
            if 15 >= contagem % 30 >= 0:
                selecao.desenhar(tela)
            titulo.desenhar(tela)
            pontos.conteudo = texto
            pontos.desenhar(tela)
            setas.desenhar(tela)

        elif 187 > tempomenu >= 50:
            if tempomenu < 51:
                IMAGENS_CARROS.pop(indexPOP)
                via1 = Via(103, IMAGENS_CARROS, posi_car, 0, vel_car)
                via2 = Via(186, IMAGENS_CARROS, posi_car, 1, vel_car)
                via3 = Via(269, IMAGENS_CARROS, posi_car, 2, vel_car)
                via4 = Via(352, IMAGENS_CARROS, posi_car, 3, vel_car)
            if carro1.y != 400:
                carro1.mover_ate(carro1.x, 400, 10)
                carro1.desenhar(tela)

            if carro1.y == 400:
                carro1.desenhar(tela)
                if 15 >= contagem % 30 >= 0:
                    tela.blit(IMAGEM_SOSETAS, (0, 0))
                if tempomenu == 59:
                    AUD_CONTAGEM.play()
                if 70 < tempomenu < 100:
                    tela.blit(IMAGEM_3, (0, 0))
                if 99 < tempomenu < 129:
                    tela.blit(IMAGEM_2, (0, 0))
                if 128 < tempomenu < 158:
                    tela.blit(IMAGEM_1, (0, 0))
                if 157 < tempomenu < 187:
                    tela.blit(IMAGEM_GO, (0, 0))
        if tempomenu == 187:
            contagem = 0
            game = True
            state = True
        if game:
            if carro1.colidir([via1, via2, via3, via4]):
                state = False
                estrada.VELOCIDADE = 0
                restart += 1
            if contagem % 30 == 0 and state:
                tempo += 1
                if tempo % 10 == 0:
                    for via in [via1, via2, via3, via4]:
                        via.veli += 1
                        via.velf += 1
                    estrada.VELOCIDADE -= 1
                    carro1.velocidade += 1

            texto = FONTE_PONTOS.render(str(tempo), 1, (255, 255, 255))
            tela.blit(texto, (500 - 10 - texto.get_width(), 10))
            if state:
                for via in [via1, via2, via3, via4]:
                    via.lista = posi_car
                    via.vel = vel_car
                    via.lancar_car()
                carro1.mover()
            for via in [via1, via2, via3, via4]:
                via.desenhar(tela)
            carro1.desenhar(tela)

            if not state:
                if restart == 1:
                    AUD_TEMA.stop()
                    AUD_GAMEOVER.play()
                tela.blit(IMAGEM_EXPLOSAO, (carro1.x - 32.5, carro1.y - 10))
                if restart > 90:
                    if escala != 500:
                        escala += 50
                        IMAGEM_RESTART = pygame.transform.scale(pygame.image.load(os.path.join('images', 'restart.png')), (escala, escala))
                    tela.blit(IMAGEM_RESTART, (0, 0))
                    if escala == 500:
                        texto = FONTE_PONTOS.render(f'Your TIME:{tempo}', 1, (255, 255, 255))
                        po = 500 - texto.get_width()
                        tela.blit(texto, (po / 2, 220))
                    if tempo > best:
                        best = tempo
    if again:
        if escala2 != 500:
            escala2 += 50
            IMAGEM = pygame.transform.scale(pygame.image.load(os.path.join('images', 'estrada.png')),
                                            (escala2, escala2))
        tela.blit(IMAGEM, (0, 0))
        if escala2 == 500:
            IMAGENS_CARROS = [
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro1.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro2.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro3.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro4.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro5.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro6.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro7.png')), (45, 70)),
                pygame.transform.scale(pygame.image.load(os.path.join('images', 'carro8.png')), (45, 70))
            ]
            selecao = Selecao(104, 200)
            estrada = Chao(0)
            titulo = Texto(0, 0, IMAGEM_TITULO)
            pontos = Texto(150, 150, None)
            setas = Texto(0, 0, IMAGEM_SETAS)

            indexPOP = None
            carro1 = False
            carros = [
                Cars(103, 300, IMAGENS_CARROS[0]),
                Cars(186, 300, IMAGENS_CARROS[1]),
                Cars(269, 300, IMAGENS_CARROS[2]),
                Cars(352, 300, IMAGENS_CARROS[3]),
                Cars(103, 200, IMAGENS_CARROS[4]),
                Cars(186, 200, IMAGENS_CARROS[5]),
                Cars(269, 200, IMAGENS_CARROS[6]),
                Cars(352, 200, IMAGENS_CARROS[7])
            ]
            AUD_TEMA.play(-1)
            game = False
            state = False
            contagem = 0
            tempo = 0
            posi_car = [0, 0, 0, 0]
            vel_car = [0, 0, 0, 0]
            tempomenu = 0
            restart = 0
            menu = True
            escala = 0
            escala2 = 0
            again = False
    contagem += 1
    pygame.display.update()