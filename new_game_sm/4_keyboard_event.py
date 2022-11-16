import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
background_width = 800 #배경 가로
background_height = 600 #배경 세로
screen = pygame.display.set_mode((background_width, background_height)) #화면 설정

#게임 화면 설정
pygame.display.set_caption("sm_game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("background.png")

#캐릭터 (스프라이트) 불러오기
minimon = pygame.image.load("minimon.png")
minimon_size = minimon.get_rect().size #이미지의 크기 구해오기
minimon_width = minimon_size[0] #캐릭터의 가로 크기
minimon_height = minimon_size[1] #캐릭터의 세로 크기
minimon_x_position = (background_width/2) - (minimon_width/2) #화면 가로 중앙에 위치 (가로)
minimon_y_position = background_height - minimon_height #화면 세로 가장 아래에 위치 (세로)

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임 진행 중 표시
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생 했는지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False #게임 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터가 왼쪽으로
                to_x -= 1
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += 1
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y -= 1
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y += 1

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0

    #게임 캐릭터 위치 정의
    minimon_x_position += to_x
    minimon_y_position += to_y

    # 가로 경계값 처리
    if minimon_x_position <0:
        minimon_x_position=0
    elif minimon_x_position > background_width - minimon_width:
        minimon_x_position=background_width - minimon_width

    #세로 경계값 처리
    if minimon_y_position <0:
        minimon_y_position=0
    elif minimon_y_position > background_height - minimon_height:
        minimon_y_position=background_height - minimon_height

    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(minimon, (minimon_x_position, minimon_y_position)) #캐릭터 그리기

    pygame.display.update() #게임 화면을 다시 그리기

#pygame 종료
pygame.quit()