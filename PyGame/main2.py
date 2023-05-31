import pygame
import random
from random import randint
from carR2 import carR
# Opening file with "record" and balance
file = open('record.txt', 'r')
data = file.readlines()
record = int(data[0])
balance = int(data[1])
file.close()
# Initializing the game / setting timer
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1500)
# Display settings
W = 1920
H = 1080
sc = pygame.display.set_mode((1920,1080), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("Highway")
pygame.display.set_icon(pygame.image.load('app.bmp'))
FPS = 60
clock = pygame.time.Clock()
# Text parameters
font = pygame.font.SysFont('Comic Sans MS', 50)
# Colors
white = (255, 255, 255)
red = (255, 0, 0); green = (0, 255, 0); blue = (0, 0, 255)
black = (0, 0, 0); grey = (192, 192, 192); ddGrey = (100, 100, 100)
# Uploading images
car1_surf = pygame.image.load("pcar1.png").convert_alpha()
car2_surf = pygame.image.load("pcar2.png").convert_alpha()
car_surf = car1_surf
car_rect = car_surf.get_rect(centerx=980, bottom=800)
road_surf = pygame.image.load("road.png")
road_surf = pygame.transform.scale(road_surf, (road_surf.get_width() // 1.5, road_surf.get_height() // 1.5))
road_surf = road_surf.convert_alpha()
send_surf = pygame.image.load("send.png").convert_alpha()
menu_surf = pygame.image.load("EndScreen.jpg").convert()
shop_surf = pygame.image.load("shop.png").convert_alpha()
# Data on cars-obstacles
cars_data = ({'path': 'car1.png'}, {'path': 'car2.png'}, {'path': 'car3.png'}, {'path': 'car4.png'})
cars_surf = [pygame.image.load(data['path']).convert_alpha() for data in cars_data]
cars = pygame.sprite.Group()
# Rendering landscape
def land():
    sc.blit(send_surf, (0, 0))
    sc.blit(road_surf, (620, landY-681))
    sc.blit(road_surf, (620, landY+1))
    sc.blit(road_surf, (620, landY+681))
# Rendering Player's car
def Pcar(xcar):
    global x
    x = 810 + xcar
    car_rect.x = 810 + xcar
    car_rect.y = 800
    sc.blit(car_surf, (x, 800))
# Rendering cars-obstacles
def createCar(group):
    indx = randint(0, len(cars_surf)-1)
    z = random.randrange(710, 1221, 170)
    speed = randint(3, 6)
    return carR(z, speed, cars_surf[indx], group)
# Checking the collision of the player's car and obstacles
def collideCars():
    global game_score; global key
    for car in cars:
        if pygame.Rect.colliderect(car.rect, car_rect):
            car.kill()
            key = 0
# End game screen
def gameOver(game_score):
    global record, balance, chose
    chose = 1
    file = open('record.txt', 'w')
    if record <= game_score:
        record = game_score
    file.write(str(record))
    file.write('\n')
    file.write(str(balance))
    file.close()
    # Rendering interface
    sc.blit(menu_surf, (0, 0))
    sc.blit(font.render(str('Авария'), True, ddGrey), (1330, 160))
    sc.blit(font.render(str('Ваш счёт'), True, ddGrey), (1130, 220))
    sc.blit(font.render(str(game_score), True, ddGrey), (1370, 220))
    sc.blit(font.render(str('Рекорд'), True, ddGrey), (1130, 270))
    sc.blit(font.render(str(record), True, ddGrey), (1320, 270))
    sc.blit(font.render(str('Баланс        Магазин - M'), True, ddGrey), (1130, 320))
    sc.blit(font.render(str(balance), True, ddGrey), (1320, 320))
    sc.blit(font.render(str('Играть ещё - G'), True, ddGrey), (1130, 370))
# Start game screen
def gameSTART():
    global car_surf, car_rect
    # Rendering interface
    sc.blit(menu_surf, (0, 0))
    sc.blit(font.render(str('Not Traffic Racer'), True, ddGrey), (1220, 160))
    sc.blit(font.render(str('A - влево D - вправо'), True, ddGrey), (1160, 230))
    sc.blit(font.render(str('Играть - G'), True, ddGrey), (1300, 300))
    sc.blit(font.render(str('Магазин - M'), True, ddGrey), (1280, 370))
# Score points
def gameSCORE(point):
    global score, game_score, balance
    score += point
    if score == 60:
        game_score += 1
        score = 0
        if (game_score % 10) == 0:
            balance += 1
# Shop interface
def gameShop():
    sc.blit(shop_surf, (0, 0))
    sc.blit(font.render(str('Магазин'), True, ddGrey), (870, 50))
    if lowBalanse == 0:
        sc.blit(font.render(str('Успешно'), True, ddGrey), (860, 150))
    elif lowBalanse == 1:
        sc.blit(font.render(str('Не достаточно средств'), True, ddGrey), (700, 150))
    sc.blit(font.render(str('Выбрано'), True, ddGrey), (840, 210))
    sc.blit(font.render(str(chose), True, ddGrey), (1090, 210))
    sc.blit(car1_surf, (300, 350))
    sc.blit(font.render(str('Выбрать'), True, ddGrey), (260, 650))
    sc.blit(font.render(str('Бесплатно'), True, ddGrey), (240, 720))
    sc.blit(font.render(str('1'), True, ddGrey), (350, 790))
    sc.blit(car2_surf, (790, 350))
    sc.blit(font.render(str('Взять в аренду'), True, ddGrey), (690, 650))
    sc.blit(font.render(str('Стоимость: 25'), True, ddGrey), (690, 720))
    sc.blit(font.render(str('2'), True, ddGrey), (840, 790))
    sc.blit(font.render(str('Назад - backspace'), True, ddGrey), (1450, 1000))
    sc.blit(font.render(str('Баланс'), True, ddGrey), (870, 900))
    sc.blit(font.render(str(balance), True, ddGrey), (1060, 900))
# Variables and initial render
xcar = 0; landY = 0; game_score = 0; score = 0
key = 2; x = 810; lowBalanse = 2; chose = 1
land(); createCar(cars); Pcar(0)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.USEREVENT:
            createCar(cars)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and x >= 810 and key == 1:
                xcar -= 170
            if event.key == pygame.K_d and x <= 980 and key == 1:
                xcar += 170
            if event.key == pygame.K_g and (key == 0 or key == 2):
                xcar = 0; landY = 0; game_score = 0; score = 0; x = 810; key = 1; lowBalanse = 2
                cars = pygame.sprite.Group()
                file = open('record.txt', 'r')
                data = file.readlines(); record = int(data[0]); balance = int(data[1])
                file.close()
            if event.key == pygame.K_m and (key == 0 or key == 2):
                key = 3
            if event.key == pygame.K_1 and key == 3:
                lowBalanse = 0
                chose = 1
                car_surf = car1_surf
                car_rect = car_surf.get_rect(centerx=980, bottom=800)
            if event.key == pygame.K_2 and key == 3 and balance >= 25:
                lowBalanse = 0
                chose = 2
                balance -= 25
                file = open('record.txt', 'w')
                file.write(str(record))
                file.write('\n')
                file.write(str(balance))
                file.close()
                car_surf = car2_surf
                car_rect = car_surf.get_rect(centerx=980, bottom=800)
            elif event.key == pygame.K_2 and key == 3 and balance < 25:
                lowBalanse = 1
            if event.key == pygame.K_BACKSPACE and key == 3:
                key = 2
                lowBalanse = 2

    if key == 1:

        if landY <= 681: landY += 11
        else: landY = 0

        land()
        sc.blit(font.render(str("Счёт"), True, black), (20, 10))
        sc.blit(font.render(str(game_score), True, black), (145, 10))
        Pcar(xcar)
        cars.draw(sc)
        cars.update(H)
        collideCars()
        gameSCORE(1)

    if key == 0:
        gameOver(game_score)
    if key == 2:
        gameSTART()
    if key == 3:
        gameShop()
    pygame.display.update()
pygame.quit()