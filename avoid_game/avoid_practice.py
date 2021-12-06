import pygame
import random

pygame.init() #초기화(반드시 해야함!)

#화면 크기 설정
s_width = 500
s_height = 700
screen = pygame.display.set_mode((s_width, s_height))

title = "Avoid bomb?!"
pygame.display.set_caption(title)

#게임 내 설정 clock => fps
clock = pygame.time.Clock()

bg = pygame.image.load('pygame_basic/bg.png')

dog = pygame.image.load('avoid_game/dog.jpg')
dog_size = dog.get_rect().size
dog_w = dog_size[0]
dog_h = dog_size[1]
dog_x_pos = (s_width / 2) - (dog_w / 2)
dog_y_pos = s_height - dog_h

ddong = pygame.image.load('avoid_game/ddong.png')
ddong_size = ddong.get_rect().size # 이미지 크기 구하기
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, s_width - ddong_width)
ddong_y_pos = (s_height / 2) - (ddong_height / 2)

to_x = 0
dog_speed = 7
ddong_speed = 7.2
# 루프
running = True
while running:
  
  dt = clock.tick(60)
  
  # 2. 이벤트 처리(입력 감지) 키보드나 마우스
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= dog_speed
      elif event.key == pygame.K_RIGHT:
        to_x += dog_speed
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
  # 3. 게임 캐릭터 위치 정의
  dog_x_pos += to_x
  
  if dog_x_pos <0:
    dog_x_pos = 0
  elif dog_x_pos > s_width - dog_w:
    dog_x_pos = s_width - dog_w
    
  ddong_y_pos += ddong_speed
  
  if ddong_y_pos > s_height:
    ddong_y_pos = 0
    ddong_x_pos = random.randint(0, s_width - ddong_width)
  # 4. 충돌 처리
  dog_rect = dog.get_rect()
  dog_rect.left = dog_x_pos
  dog_rect.top = dog_y_pos
  
  ddong_rect = ddong.get_rect()
  ddong_rect.left = ddong_x_pos
  ddong_rect.top = ddong_y_pos
  
  if dog_rect.colliderect(ddong_rect):
    print("부딪혔습니다!")
    running = False
  # 5. 화면에 그리기
  #screen.blit(bg, (0, 0))
  screen.fill((255,255,255))
  screen.blit(dog, (dog_x_pos, dog_y_pos))
  screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
  pygame.display.update() # 게임화면 다시그리기
  
      
#게임 종료      
pygame.quit()

