############ 점프 게임 구현 순서############
# 네모가 점프해서 장애물을 피해가는 게임
##########################################
#1. 뼈대 구성 (완성)
#2. 네모 클래스 만들기 (플레이어) (완성)
#3. 장애물 클래스 만들기 (완성)
#4. 네모가 장애물을 피해가면 끝. (완성)
#   -. 충돌 처리
#   -. 점수 (화면표시)
#5. 못피하면? 게임오버 (완성)
#   -. 게임오버 되면,, 재시작.. (화면표시)
##########################################

# 제가 주로 쓰는 ....ㅋ
from turtle import color
from xml.dom.expatbuilder import ParseEscape
import pygame
import sys
import random
 
# 초기화
pygame.init()

screen_width = 640
screen_height = 200 #작게 만들어 보겠습니다.

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("점프하는 네모 ? ㅋ")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width,height), pygame.SRCALPHA).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vel = 0
        self.clicked = False  #마우스로 점프할꺼에요
        self.jump_cnt = 0 #3단 점프까지 적용 해 볼게요.

    def update(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            if self.jump_cnt < 3: #3회까지만..
                self.vel = -15
                self.jump_cnt += 1
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.vel += 1     #1씩 아래로 떨어지게 만듭니다.
        if self.vel > 10: # 10 이상 안넘어가도록.. 막습니다.
            self.vel = 10
        #바닥이 어디죠?ㅋㅋ 화면 제일 밑으로 하겟습니다.
        if self.rect.bottom <= screen_height :
            self.rect.y += int(self.vel) #일단 떨어지게 하고....
            if self.rect.y >= screen_height - self.rect.height: #네모 윗 부분이...바닥에서 네모칸만큼 올라온곳.......
                self.rect.y = screen_height - self.rect.height
                self.jump_cnt = 0 #바닥에 착지했으니까... 점프횟수 초기화

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width,height), pygame.SRCALPHA).convert_alpha()
        #세모로 만들어 보겠습니다. (꼭지점. 왼쪽밑, 오른쪽 밑)
        pt = [(width/2, 0), (0,height),(width,height)]
        pygame.draw.polygon(self.image, color, pt)
        self.rect = self.image.get_rect()
        self.vel = 5
        self.rect.x = screen_width #오른쪽에서 플레이어쪽으로 이동합니다.
        self.rect.y = screen_height - self.rect.height

    def update(self):
        self.rect.x -= int(self.vel)
    
    def check_screen_out(self): #화면 밖으로 나가면 점수 획득.. 및.... 객체를 삭제 해야 합니다.
        result = False
        if self.rect.x < 0:
            result = True
        return result

def show_gameover():
    global game_over
    game_over = True

    font = pygame.font.SysFont("헤드라인", 60)
    over_text = font.render(f"Game Over", True, (50,50,255))
    screen.blit(over_text, (int(screen_width/2 -  over_text.get_width()/2), int(screen_height/3)))

    font = pygame.font.SysFont("헤드라인", 30)
    over_text = font.render(f"please, space key..", True, (200,200,255))
    screen.blit(over_text, (int(screen_width/2 -  over_text.get_width()/2), int(screen_height/4*2)))

def restart_game():
    global game_over, score
    game_over = False
    obstacles.empty()
    score = 0

def show_score():
    font = pygame.font.SysFont("헤드라인", 30)
    score_text = font.render(f"Score : {score}", True, (255,255,255))
    screen.blit(score_text, (0,0))

player = pygame.sprite.Group()
player.add(Player(30,30,white))

obstacles = pygame.sprite.Group()

game_over = False
score = 0
clock = pygame.time.Clock()
fps = 60
t_tick = -1
while True:
    clock.tick(fps)
    t_tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_SPACE] and game_over:
        restart_game()

    #장애물 생성
    if game_over == True:
        show_gameover()
    else:
        if t_tick % random.randint(20,50) == 0:
            t_tick = 0
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            obstacles.add(Obstacle(30,30,color))

        #충돌 처리
        if pygame.sprite.groupcollide(player, obstacles, False, False) :
            show_gameover()

        #장애물이 왼쪽 밖으로 넘어간 것 체크
        del_obstacle = []
        for o in obstacles:
            if o.check_screen_out():
                score += 1
                del_obstacle.append(o)
        #장애물 삭제
        for d in del_obstacle:
            obstacles.remove(d)

        screen.fill(black)
        show_score()

        player.update()
        player.draw(screen)

        obstacles.update()
        obstacles.draw(screen)


    pygame.display.update()
