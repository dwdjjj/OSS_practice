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

# 배경 // 이미지 불러오기 pygame.image.load로
background = pygame.image.load('pygame_basic/bg.png')

# 토끼
rabbit = pygame.image.load('pygame_basic/rabbit.jpeg')
rabbit_size = rabbit.get_rect().size # 이미지 크기 구하기
rabbit_width = rabbit_size[0]
rabbit_height = rabbit_size[1]
rabbit_x_pos = (s_width / 2) - (rabbit_width / 2)
rabbit_y_pos = s_height - rabbit_height

# 적
enemy = pygame.image.load('pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size # 이미지 크기 구하기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (s_width / 2) - (enemy_width / 2)
enemy_y_pos = (s_height / 2) - (enemy_height / 2)


#좌표
to_x = 0
to_y = 0
# 이동속도
rabbit_speed = 0.5

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (종류, 크기)

#시간
total_time = 10 
start_ticks = pygame.time.get_ticks() # 현재시간을 스타트 시간으로


# 루프
running = True
while running:
  # FPS : 프레임마다 캐릭터가 움직이는 값이 달라져야함, 프레임에 따라 게임 자체의 속도마저 달라지면 안됨!
  dt = clock.tick(60)
  
  # 입력 감지
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.KEYDOWN: # 키를 누를 때
      if event.key == pygame.K_LEFT:
        to_x -= rabbit_speed
      elif event.key == pygame.K_RIGHT:
        to_x += rabbit_speed
      elif event.key == pygame.K_UP:
        to_y += rabbit_speed
      elif event.key == pygame.K_DOWN:
        to_y -= rabbit_speed
        
    if event.type == pygame.KEYUP: # 방향키 떼면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
        
  rabbit_x_pos += to_x * dt
  rabbit_y_pos -= to_y * dt
  
  if rabbit_x_pos < 0:
    rabbit_x_pos = 0
  elif rabbit_x_pos > s_width - rabbit_width:
    rabbit_x_pos = s_width - rabbit_width
    
  if rabbit_y_pos < 0:
    rabbit_y_pos = 0
  elif rabbit_y_pos > s_height - rabbit_height:
    rabbit_y_pos = s_height - rabbit_height
     
  # 충돌 처리 rect정보 업데이트
  rabbit_rect = rabbit.get_rect()
  rabbit_rect.left = rabbit_x_pos
  rabbit_rect.top = rabbit_y_pos
  
  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos
  
  # 충돌 처리
  if rabbit_rect.colliderect(enemy_rect):
    print("충돌!")
    running = False
  
  screen.fill((255, 255, 255)) #흰 배경
  #screen.blit(background, (0, 0))
  screen.blit(rabbit, (rabbit_x_pos, rabbit_y_pos))
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
  
  #타이머, 경과 시간 => ms를 s로 표시
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
  
  timer = game_font.render(str(int(total_time-elapsed_time)), True, (0, 0, 0))
  # render 함수는 시간, antialias(True), 글자색상 들어감
  screen.blit(timer, (10, 10))
  
  if total_time - elapsed_time <= 0:
    print("Time is up")
    running = False
  
  pygame.display.update() # 게임화면 다시그리기
      
pygame.time.delay(2000) # 살짝 대기하기      
      
#게임 종료      
pygame.quit()

