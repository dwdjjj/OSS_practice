import pygame, random, time

pygame.init()

# sound
dingdong = pygame.mixer.Sound('Bugcatch/dingdong.wav')
fsigh = pygame.mixer.Sound('Bugcatch/fsigh.wav')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
large_font = pygame.font.SysFont(None, 65)
small_font = pygame.font.SysFont(None, 35)
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) 

done = False
clock = pygame.time.Clock() 

def runGame():
    global done
    score = 0
    start_time = int(time.time())
    remain_time = 0
    game_over = 0

    bug_image = pygame.image.load('Bugcatch/bug.png')
    bug_image = pygame.transform.scale(bug_image, (60, 80))
    bugs = []
    for i in range(3):
        bug = pygame.Rect(bug_image.get_rect())
        bug.left = random.randint(0, screen_width)
        bug.top = random.randint(0, screen_height)
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        bugs.append((bug, dx, dy))

    while not done: 
        clock.tick(35)
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
                print(event.pos[0], event.pos[1])
                for (bug, dx, dy) in bugs:
                    if bug.collidepoint(event.pos):
                        print(bug)
                        bugs.remove((bug, dx, dy))
                        bug = pygame.Rect(bug_image.get_rect())
                        bug.left = random.randint(0, screen_width)
                        bug.top = random.randint(0, screen_height)
                        dx = random.randint(-10, 10)
                        dy = random.randint(-10, 10)
                        bugs.append((bug, dx, dy))
                        score += 1
                        dingdong.play()
                        

        if game_over == 0:
            for (bug, dx, dy) in bugs:
                bug.left += dx
                bug.top += dy

            remain_time = 60 - (int(time.time()) - start_time)

            if remain_time <= 0:
                game_over = 1

        for (bug, dx, dy) in bugs:
            screen.blit(bug_image, bug)

        for (bug, dx, dy) in bugs:
            if not bug.colliderect(screen.get_rect()):
                bugs.remove((bug, dx, dy))
                bug = pygame.Rect(bug_image.get_rect())
                bug.left = random.randint(0, screen_width)
                bug.top = random.randint(0, screen_height)
                dx = random.randint(-9, 9)
                dy = random.randint(-9, 9)
                bugs.append((bug, dx, dy))

        score_image = small_font.render('Score: {}'.format(score), True, WHITE)
        screen.blit(score_image, (10, 10))

        remain_time_image = small_font.render('Timer: {}'.format(remain_time)+'s', True, WHITE)
        screen.blit(remain_time_image, (screen_width - 10 - remain_time_image.get_width(), 10))

        if game_over == 1:
            game_over_image = large_font.render('GameOver', True, RED)
            fsigh.play()
            screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2, screen_height // 2 - game_over_image.get_height() // 2))
            fsigh.stop()

        pygame.display.update()

runGame()
pygame.quit()


