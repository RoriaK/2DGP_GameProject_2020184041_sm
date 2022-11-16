import random
import pygame
##########################################################3
#기본 초기화(반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
background_width = 800 #배경 가로
background_height = 600 #배경 세로
screen = pygame.display.set_mode((background_width, background_height)) #화면 설정

#게임 화면 설정
pygame.display.set_caption("sm_game") #게임 이름

#FPS
clock = pygame.time.Clock()
#######################################################################

#1.사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
#배경 만들기
background = pygame.image.load("background.png")

#캐릭터 만들기
minimon = pygame.image.load("minimon.png")
minimon_size = minimon.get_rect().size
minimon_width = minimon_size[0] #첫 번째 값
minimon_height = minimon_size[1] #두 번째 값
minimon_x_position = (background_width / 2) - (minimon_width/2)
minimon_y_position = background_height - minimon_height

#(캐릭터 움직이기) 이동 위치
to_x = 0
# to_y = 0
minimon_speed = 10

#적군 만들기
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #첫 번째 값
enemy_height = enemy_size[1] #두 번째 값
enemy_x_position = random.randint(0, background_width - enemy_width)
enemy_y_position = 0
enemy_speed = 10


running = True #게임 진행 중 표시
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= minimon_speed
            elif event.key == pygame.K_RIGHT:
                to_x += minimon_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #3. 게임 캐릭터 위치 정의
    minimon_x_position += to_x
    # minimon_y_position += to_y

    if minimon_x_position <0:
        minimon_x_position = 0
    elif minimon_x_position > background_width - minimon_width:
        minimon_x_position = background_width - minimon_width

    enemy_y_position += enemy_speed

    if enemy_y_position > background_height:
        enemy_y_position = 0
        enemy_x_position = random.randint(0, background_width - enemy_width)

    # if minimon_y_position <0:
    #     minimon_y_position = 0
    # elif minimon_y_position > background_height - minimon_height:
    #     minimon_y_position = background_height - minimon_height

    #4. 충돌 처리
    minimon_rect = minimon.get_rect()
    minimon_rect.left = minimon_x_position
    minimon_rect.top = minimon_y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    if minimon_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    #5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(minimon, (minimon_x_position, minimon_y_position))
    screen.blit(enemy, (enemy_x_position, enemy_y_position))


    pygame.display.update()

pygame.quit()