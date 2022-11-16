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

running = True #게임 진행 중 표시
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #3. 게임 캐릭터 위치 정의

    #4. 충돌 처리

    #5. 화면에 그리기
    pygame.time.delay(2000) #2초 정도 대기 (ms)

pygame.quit()