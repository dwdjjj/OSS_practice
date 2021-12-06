import pygame

pygame.init() #초기화

#화면 크기 설정
size = [500, 700]
screen = pygame.display.set_mode(size)

title = "Game 1"
pygame.display.set_caption(title)

#게임 내 설정
clock = pygame.time.Clock()
running = True
while running:
  # FPS
  clock.tick(60)
  
  # 입력 감지
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
      
      
#게임 종료      
pygame.quit()

