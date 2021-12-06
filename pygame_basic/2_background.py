import pygame

pygame.init() #초기화

#화면 크기 설정
size = [500, 700]
screen = pygame.display.set_mode(size)

title = "Game 1"
pygame.display.set_caption(title)

# 이미지
background = pygame.image.load('pygame_basic/bg.png')
rabbit = pygame.image.load('pygame_basic/rabbit.jpeg')
rabbit_size = rabbit.get_rect().size # 이미지 크기 구하기
rabbit_width = rabbit_size[0]
rabbit_height = rabbit_size[1]
rabbit_x_pos = size[0] / 2
rabbit_y_pos = size[1] - rabbit_height


#게임 내 설정
clock = pygame.time.Clock()

# 루프
running = True
while running:
  # FPS
  clock.tick(60)
  
  # 입력 감지
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
      
  screen.fill((255, 255, 255)) #흰 배경
  #screen.blit(background, (0, 0))
  
  screen.blit(rabbit, (rabbit_x_pos, rabbit_y_pos))
  
  pygame.display.update() # 게임화면 다시그리기
      
      
      
#게임 종료      
pygame.quit()

