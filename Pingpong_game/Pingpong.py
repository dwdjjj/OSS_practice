import turtle, pygame, sys
from pygame.locals import *
#import from순으로는 X

# 화면 구성
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
# font = pygame.font.SysFont(None, 30)


screen = turtle.Screen()
screen.title('Pingpong game in python')
screen.bgcolor('black')
screen.setup(WINDOWWIDTH, WINDOWHEIGHT)
screen.tracer(0)
# 좌 판때기
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color('red')
paddle_l.shapesize(stretch_wid = 6,stretch_len =1);
paddle_l.penup()
paddle_l.goto(-350,0)
# 우 판때기
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color('blue')
paddle_r.shapesize(stretch_wid = 6,stretch_len =1);
paddle_r.penup()
paddle_r.goto(350,0)
# 터틀로 공만들기
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')

ball.penup()
ball.goto(0,0)
# 공움직이기
ball.dx = 2
ball.dy = 2

def paddle_l_up():
  y = paddle_l.ycor() 
  y += 24
  paddle_l.sety(y)

def paddle_l_down():
  y = paddle_l.ycor() 
  y -= 24
  paddle_l.sety(y)

def paddle_r_up():
  y = paddle_r.ycor() 
  y += 24
  paddle_r.sety(y)

def paddle_r_down():
  y = paddle_r.ycor() 
  y -= 24
  paddle_r.sety(y)

# 키입력
screen.listen()
screen.onkey(paddle_l_up,"w")
screen.onkey(paddle_l_down,"s")
screen.onkey(paddle_r_up,"Up")
screen.onkey(paddle_r_down,"Down")

def terminate():
    pygame.quit()
    sys.exit()
    
def waitPressKey():
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        terminate()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          terminate()
        return

# 메인 루프
while True:
    screen.update()
    score = 0

    # 공 이동시키기
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
    
    if ball.ycor() < - 290:
      ball.sety(-290)
      ball.dy *= -1
     
    if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
    if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1

     # 충돌 체크
    if ball.xcor() < -340 and ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() - 50:
        ball.dx *= -1
        score += 1

    elif ball.xcor() > 340 and ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50:
        ball.dx *= -1
        score += 1
    
    # drawText('Score: %s' % (score), font, windowSurface, 50, 0)