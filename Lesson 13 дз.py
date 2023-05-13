import pygame
from Sprites import Ball
from random import randint



pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)



m = pygame.mixer.music.load("pic/coin.mp3")

BLACK = (0, 0, 0)
W, H = 1000, 570

ground3 = H-70

x = 0
y = 0
jump_force = 20
move = jump_force + 1


sc = pygame.display.set_mode((W, H))
balls = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 60
speed = 10

joda = pygame.image.load('pic/Joda.png')
j_rect = joda.get_rect(centerx=W//2, bottom=H-5)
ground = pygame.image.load('pic/line.png')
ground2 = pygame.image.load('pic/line.png')
g_rect = ground.get_rect(x = 0, bottom = H - 40)
g2_rect = ground.get_rect(x = 700,bottom = H - 40)
j_rect.bottom = ground3
bg = pygame.image.load('pic/bg_color2.webp')


balls_data = ({'path': 'Star.png', 'score': 100},
              {'path': 'Heart.png', 'score': 150},
              {'path': 'coin.png', 'score': 200})

balls_surf = [pygame.image.load('pic/'+data['path']).convert_alpha() for data in balls_data]


def createBall(group):
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(2, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

fail = 0
game_score = 0
def collideBalls():
    global game_score
    global fail
    for ball in balls:
        if j_rect.collidepoint(ball.rect.center):

            game_score += ball.score
            pygame.mixer.music.play(1, 0.5)
            ball.kill()

        elif g_rect.collidepoint(ball.rect.center) or g2_rect.collidepoint(ball.rect.center):
            fail += 1




createBall(balls)

clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground3 == j_rect.bottom:
                move = -jump_force

    if move <= jump_force:
        if j_rect.bottom + move < ground3:
            j_rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            j_rect.bottom = ground3
            move = jump_force + 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        j_rect.x -= speed
        if j_rect.x < 0:
            j_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        j_rect.x += speed
        if j_rect.x > W - j_rect.width:
            j_rect.x = W - j_rect.width

    if game_score >= 2000:
        print('Победа')
        break
    elif fail == 3:
        print('Вы проиграли')
        break

    collideBalls()
    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(ground, g_rect)
    sc.blit(ground2, g2_rect)
    sc.blit(joda, j_rect)


    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)



'''if ground(ball.rect.center):
    print('Вы проиграли')
    run = False
'''