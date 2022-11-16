import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
background_width = 480 #배경 가로
background_height = 640 #배경 세로
screen = pygame.display.set_mode((background_width, background_height)) #화면 설정

#게임 화면 설정
pygame.display.set_caption("sm_game") #게임 이름

#이벤트 루프
running = True #게임 진행 중 표시
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생 했는지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False #게임 진행중이 아님

#pygame 종료
pygame.quit()