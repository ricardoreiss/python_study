import pygame, random

pygame.init()

PLAYER1 = pygame.transform.scale(pygame.image.load('player_left.jpg'), (20, 120))
PLAYER2 = pygame.transform.scale(pygame.image.load('player_right.jpg'), (20, 120))
BALL = pygame.transform.scale(pygame.image.load('Ball.png'), (30, 30))
FONTE_PONTOS = pygame.font.SysFont('monospace', 80, bold=True)

class Player:
    def __init__(self, x, y, player):
        self.imagem = player
        self.x = x
        self.y = y
        self.state = {'UP': False, 'DOWN': False}

    def move(self):
        if self.state['UP']:
            if self.y > 0:
                self.y -= 10
        if self.state['DOWN']:
            if self.y < (500 - 120):
                self.y += 10

    def desenhar(self):
        tela.blit(self.imagem, (self.x, self.y))


class Ball:
    def __init__(self, x, y):
        self.imagem = BALL
        self.x = x
        self.y = y
        self.direX = 0
        self.direY = 0

    def move(self):
        self.x += self.direX
        self.y -= self.direY

    def desenhar(self):
        tela.blit(self.imagem, (self.x, self.y))

    def colidir(self, player):
        col = False
        ball_mask = pygame.mask.from_surface(self.imagem)
        player_mask = pygame.mask.from_surface(player.imagem)
        distancia = (round(self.x - player.x), round(self.y - player.y))
        ponto = player_mask.overlap(ball_mask, distancia)
        if ponto:
            col = True

        return col


WIDTH = 900
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping-Pong                                 '
'                                                                    Play Game(w,s,setas)                    '
'                                     Restart Game(r)')
relogio = pygame.time.Clock()

def fundo():
    tela.fill(BLACK)
    pygame.draw.line(tela, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5)


p1_points = 0
p2_points = 0
ball = False
game = False
while True:
    relogio.tick(60)
    fundo()
    texto1 = (FONTE_PONTOS.render(f'{p1_points}', 0, WHITE))
    texto2 = (FONTE_PONTOS.render(f'{p2_points}', 0, WHITE))
    tela.blit(texto1, (225 - (texto1.get_width()/2), 10))
    tela.blit(texto2, (675 - (texto2.get_width() / 2), 10))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        if evento.type == pygame.KEYDOWN:
            key = evento.key
            if key == pygame.K_r:
                p1_points = 0
                p2_points = 0
                game = False
            if not game:
                if key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_w or key == pygame.K_s:
                    game = True
                    ball.direX = random.choice([12, -12])
                    ball.direY = random.choice([5, -5])
            if game:
                if key == pygame.K_UP:
                    player2.state['UP'] = True
                if key == pygame.K_DOWN:
                    player2.state['DOWN'] = True
                if key == pygame.K_w:
                    player1.state['UP'] = True
                if key == pygame.K_s:
                    player1.state['DOWN'] = True
        if evento.type == pygame.KEYUP:
            key = evento.key
            if evento.key == pygame.K_UP:
                player2.state['UP'] = False
            if evento.key == pygame.K_DOWN:
                player2.state['DOWN'] = False
            if key == pygame.K_w:
                player1.state['UP'] = False
            if key == pygame.K_s:
                player1.state['DOWN'] = False

    if ball:
        player1.move()
        player2.move()
        ball.desenhar()
        player1.desenhar()
        player2.desenhar()
        ball.move()
    if game:
        if ball.colidir(player1) or ball.colidir(player2):
            ball.direX = -ball.direX
        if ball.y <= 0 or (ball.y + 30) >= 500:
            ball.direY = -ball.direY
        if ball.x <= -30:
            p2_points += 1
            game = False
        if ball.x >= 900:
            p1_points += 1
            game = False

    if not game:
        player1 = Player(15, HEIGHT // 2 - 60, PLAYER1)
        player2 = Player(WIDTH - 20 - 15, HEIGHT // 2 - 60, PLAYER2)
        ball = Ball((WIDTH // 2) - 15, (HEIGHT // 2) - 15)

    pygame.display.update()
