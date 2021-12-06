import pygame

pygame.init() #초기화(반드시 해야함!)

#화면 크기 설정
s_width = 500
s_height = 700
screen = pygame.display.set_mode((s_width, s_height))

title = "Game 1"
pygame.display.set_caption(title)

#게임 내 설정 clock => fps
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화(배경, 캐릭터이미지, 좌표, 속도, 폰트 등등)

# 루프
running = True
while running:
  
  dt = clock.tick(60)
  
  # 2. 이벤트 처리(입력 감지) 키보드나 마우스
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # 3. 게임 캐릭터 위치 정의
  
  # 4. 충돌 처리
    
  # 5. 화면에 그리기
  
  pygame.display.update() # 게임화면 다시그리기
      
#게임 종료      
pygame.quit()

