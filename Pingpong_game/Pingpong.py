#Simple Pythong 3 , ping pong game
# turtle module for biginners
import turtle
# 화면 구성
wn = turtle.Screen()
wn.title('Pong by Anvarbey.muminov@gmail.com')
wn.bgcolor('black')
wn.setup(width = 800, height =600)
wn.tracer(0)
# 좌 판때기
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5,stretch_len =2);
paddle_a.penup()
paddle_a.goto(-350,0)
# 우 판때기
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5,stretch_len =2);
paddle_b.penup()
paddle_b.goto(350,0)
# 터틀로 공만들기
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')

ball.penup()
ball.goto(0,0)
# 공움직이기
ball.dx = 1
ball.dy = 1

def paddle_a_up():
  y = paddle_a.ycor() 
  y += 24
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor() 
  y -= 24
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor() 
  y += 24
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor() 
  y -= 24
  paddle_b.sety(y)

# 키입력
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")




# 메인 루프
while True:
    wn.update()

    # 공 이동시키기
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    # 화면 체크
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
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
       

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
       