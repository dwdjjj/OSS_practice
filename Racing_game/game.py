import pygame, random, sys ,os,time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 50
ENEMYMINSIZE = 10
ENEMYMAXSIZE = 40
ENEMYMINSPEED = 7
ENEMYMAXSPEED = 7
ADDNEWENEMYRATE = 6
PLAYERMOVERATE = 4
count=3

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def playerHasHitEnemy(playerRect, Enemys):
    for b in Enemys:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, True, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# 셋팅
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Racing game!!')
pygame.mouse.set_visible(False)

# 폰트설정
print(pygame.font.get_fonts())
font = pygame.font.SysFont(None, 30, True, True)

# 사운드세팅
gameOverSound = pygame.mixer.Sound('Racing_game/music/crash.wav')
pygame.mixer.music.load('Racing_game/music/car.wav')
laugh = pygame.mixer.Sound('Racing_game/music/laugh.wav')


# 이미지 로드
playerImage = pygame.image.load('Racing_game/image/playercar.png')

EnemyCar1 = pygame.image.load('Racing_game/image/EnemyCar1.png')
EnemyCar2 = pygame.image.load('Racing_game/image/EnemyCar2.png')
EnemyCar3 = pygame.image.load('Racing_game/image/EnemyCar3.png')
playerRect = playerImage.get_rect()
sample = [EnemyCar1, EnemyCar2, EnemyCar3]
wallLeft = pygame.image.load('Racing_game/image/left.png')
wallRight = pygame.image.load('Racing_game/image/right.png')


# 시작화면
drawText('Please press Any key for Start game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+30)
pygame.display.update()
waitForPlayerToPressKey()
zero=0
if not os.path.exists("Racing_game/data/save.dat"):
    f=open("Racing_game/data/save.dat",'w')
    f.write(str(zero))
    f.close()   
v=open("Racing_game/data/save.dat",'r')
topScore = int(v.readline())
v.close()
while (count>0):
    
    Enemys = []
    score = 0
    playerRect.topleft = ((WINDOWWIDTH / 2) - 100, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    con = False
    EnemyAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    # 메인 게임루프
    while True:
        score += 1

        for event in pygame.event.get():
            
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
            
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()
            

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            

        # 위에서부터 나올 장애물 차량들
        if not con:
            EnemyAddCounter += 1
        if EnemyAddCounter == ADDNEWENEMYRATE:
            EnemyAddCounter = 0
            EnemySize =30 
            newEnemy = {'rect': pygame.Rect(random.randint(140, 485), 0 - EnemySize, 23, 47),
                        'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                        'surface':pygame.transform.scale(random.choice(sample), (23, 47)),
                        }
            Enemys.append(newEnemy)
            sideLeft= {'rect': pygame.Rect(0,0,126,600),
                       'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                       'surface':pygame.transform.scale(wallLeft, (126, 599)),
                       }
            Enemys.append(sideLeft)
            sideRight= {'rect': pygame.Rect(497,0,303,600),
                       'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                       'surface':pygame.transform.scale(wallRight, (303, 599)),
                       }
            Enemys.append(sideRight)
            
            

        # 캐릭터 무빙
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        for b in Enemys:
            b['rect'].move_ip(0, b['speed'])

         
        for b in Enemys[:]:
            if b['rect'].top > WINDOWHEIGHT:
                Enemys.remove(b)

        # 화면채우기
        windowSurface.fill(BACKGROUNDCOLOR)

        # 점수판그리기
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface,128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface,128, 40)
        
        windowSurface.blit(playerImage, playerRect)

        
        for b in Enemys:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # 충돌시
        if playerHasHitEnemy(playerRect, Enemys):
            if score > topScore:
                g=open("Racing_game/data/save.dat",'w')
                g.write(str(score))
                g.close()
                topScore = score
            break

        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    count=count-1
    gameOverSound.play()
    time.sleep(1)
    if (count==0):
     laugh.play()
     drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
     drawText('Please press any keys to restart.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
     pygame.display.update()
     time.sleep(2)
     waitForPlayerToPressKey()
     count=3
     gameOverSound.stop()
