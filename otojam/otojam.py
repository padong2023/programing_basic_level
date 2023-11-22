import pygame, math, time, os, random                   # 필요한 모듈 추가

pygame.init()

w= 1600
h = w*(9/16)

screen = pygame.display.set_mode((w, h))        # screen이란 변수에 화면 창의 정보 저장

clock = pygame.time.Clock()

# bool의 형태로 main과 ingame 변수 선언
main = True
ingame = True

 # 키 입력 감지 리스트
keys = [0, 0, 0, 0]                            
keyset = [0, 0, 0, 0] 

# 프레임 구하느 코드
maxframe = 60
fps = 0

# 노트 위치 계산을 위치 타이머 코드
gst = time.time()

Time = time.time() - gst

# 노트 소환 함수
ty = 0          # 노트의 y
tst = Time           # 노트 소환 시간

t1=[]
t2=[]
t3=[]
t4=[]

speed = 2           # 노트 속도 2단계

#########################폰트 기본 설정########################
Cpath = os.path.dirname(__file__)
Fpath = os.path.join(Cpath, "font")

rate = "Let's play!"

ingame_font_rate = pygame.font.Font(os.path.join(Fpath, "KCC-Ganpan.ttf"), int(w/23))
rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))

############################################################

################ 노트 랜덤 생성을 위한 것들 ###################
def sum_note(n):
    ty = 0
    tst = Time + 2
    if n == 1:
        t1.append([ty, tst])
    if n == 2:
        t2.append([ty, tst])
    if n == 3:
        t3.append([ty, tst])
    if n == 4:
        t4.append([ty, tst])



notesumt = 0

a = 0
aa = 0
##############################################################

spin = 0        # 디자인 용

##############################################################
###################### 판정 코드 ##############################

combo = 0 
combo_effect = 0            # 텍스트 사이즈 변경
combo_effect2 = 0           # 텍스트 사이즈 변경
miss_anim = 0   
last_combo = 0              

combo_time = Time + 1      #텍스트가 표시될 시간 설정

rate_data = [0, 0, 0, 0]

def rating(n):
    global combo, miss_anim, last_combo, combo_effect, combo_effect2, combo_time, rate
    if abs((h/12)*9 - rate_data[n-1] < 950*speed*(h/900) and (h/12)*9 - rate_data[n-1] >= 200*speed*(h/900)):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1 
        combo_effect2 = 1.3
        rate = "WORST"
    if abs((h/12)*9 - rate_data[n-1]) < 200*speed*(h/900) and abs((h/12)*9 - rate_data[n-1]) >= 100*speed*(h/900):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1 
        combo_effect2 = 1.3
        rate = "BAD"
    if abs((h/12)*9 - rate_data[n-1]) < 100*speed*(h/900) and abs((h/12)*9 - rate_data[n-1]) >= 50*speed*(h/900):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1 
        combo_effect2 = 1.3
        rate = "GOOD"
    if abs((h/12)*9 - rate_data[n-1]) < 50*speed*(h/900) and abs((h/12)*9 - rate_data[n-1]) >= 15*speed*(h/900):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1 
        combo_effect2 = 1.3
        rate = "GREAT"
    if abs((h/12)*9 - rate_data[n-1]) < 15*speed*(h/900) and abs(h/12)*9 - rate_data[n-1] >= 0*speed*(h/900):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1 
        combo_effect2 = 1.3
        rate = "PERFECT"

# 게임 main 코드----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while main:
    while ingame:

        if len(t1) > 0:
            rate_data[0] = t1[0][0]
        if len(t2) > 0:
            rate_data[1] = t2[0][0]
        if len(t3) > 0:
            rate_data[2] = t3[0][0]
        if len(t4) > 0:
            rate_data[3] = t4[0][0]


        # 노트가 랜덤한 위치에 자동으로 생성 
        if Time > 0.2 * notesumt:
            notesumt += 1
            while a == aa:
                a = random.randint(1, 4)
            sum_note(a)
            aa = a


        Time = time.time() - gst

        fps == clock.get_fps()        # 시간에 따른 프레임 확인

        ingame_font_combo = pygame.font.Font(os.path.join(Fpath, "KCC-Ganpan.ttf"), int((w/38)*combo_effect2))
        combo_text = ingame_font_combo.render(str(combo), False, (255, 255, 255))

        rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))
        rate_text = pygame.transform.scale(rate_text, (int(w/110*len(rate)*combo_effect2), int((w/58*combo_effect*combo_effect2))))

        ingame_font_miss = pygame.font.Font(os.path.join(Fpath,"KCC-Ganpan.ttf"), int((w/38)*miss_anim))
        miss_text = ingame_font_miss.render(str(last_combo), False, (255, 0, 0))

        if fps == 0:
            fps == maxframe


        for event in pygame.event.get():            # 이벤트 감지 코드
            if event.type == pygame.QUIT:           # 게임 나가기 이벤트 감지
                pygame.quit()
            if event.type == pygame.KEYDOWN:        # 키 입력 이벤트 감지 코드(누를 떄)
                if event.key == pygame.K_a:         # 키입력 A
                    keyset[0] = 1
                    if len(t1) > 0 :
                        if t1[0][0] > h/3:
                            rating(1)
                            del t1[0]

                if event.key == pygame.K_s:         # 키입력 S
                    keyset[1] = 1
                    if len(t2) > 0 :
                        if t2[0][0] > h/3:
                            rating(2)
                            del t2[0]

                if event.key == pygame.K_k:         # 키입력 K
                    keyset[2] = 1
                    if len(t3) > 0 :
                        if t3[0][0] > h/3:
                            rating(3)
                            del t3[0]

                if event.key == pygame.K_l:         # 키입력 L
                    keyset[3] = 1
                    if len(t4) > 0 :
                        if t4[0][0] > h/3:
                            rating(4)
                            del t4[0]


            if event.type == pygame.KEYUP:        # 키 입력 이벤트 감지 코드(안 누를 때)
                if event.key == pygame.K_a:         # 키입력 A
                    keyset[0] = 0
                if event.key == pygame.K_s:         # 키입력 S
                    keyset[1] = 0
                if event.key == pygame.K_k:         # 키입력 K
                    keyset[2] = 0
                if event.key == pygame.K_l:         # 키입력 L
                    keyset[3] = 0
    # 화면----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        screen.fill((0, 0, 0))          # 화면 색깔 채우기 RGB값으로 넣기


        if fps == 0:
            fps = 60
        # 움직임에 가감속을 넣어주는 코드(거의 감속 기능)
        keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (3 *( maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))


        # 텍스트 움직임을 정해주는 코드
        if Time > combo_time:
            combo_effect += (0 - combo_effect) / (7 * (maxframe/fps))
        if Time < combo_time:
            combo_effect += (1 - combo_effect) / (7 * (maxframe/fps))

        combo_effect2 += (2 - combo_effect2) / (7 * (maxframe/fps))

        miss_anim += (4 - miss_anim) / (14 * (maxframe/fps))
    

        pygame.draw.rect(screen, (0, 0, 0), (w/2 - w/8, -int(w/100), w/4, h + int(w/50)))    # 화면 background
        

    # keydown 시에 이펙트 스타일 및 위치 선정-----------------------------------------------------------------------------------------------------------------------------------------------------------
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7) * i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/8 + w/32 - (w/32)*keys[0], (h/12)*9 - (h/30)*keys[0]*i, w/16*keys[0], (h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7) * i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/16 + w/32 - (w/32)*keys[1], (h/12)*9 - (h/30)*keys[1]*i, w/16*keys[1], (h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7) * i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/32 - (w/32)*keys[2], (h/12)*9 - (h/30)*keys[2]*i, w/16*keys[2], (h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7) * i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/16 + w/32 - (w/32)*keys[3], (h/12)*9 - (h/30)*keys[3]*i, w/16*keys[3], (h/35)/i))
        
        
        
    # note------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        for tile_data in t1:
            tile_data[0] = 0 - (h/12)*9 + (Time - tile_data[1])*350*speed*(h/900)               # (h/12*9) -> 판정선 위치 기준 // (Time - tile_data[1])*350 -> (현재시간 - 노트소환시간) * 350 위치로 이동, 시간이 지날수록 이부분의 차이가 커지므로 노트의 위치가 내려가게 됨
            pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                #### 미스판정 추가####
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1 
                combo_effect2 = 1.3
                rate = "MISS"
                ######################
                t1.remove(tile_data)

        for tile_data in t2:
            tile_data[0] = 0 - (h/12)*9 + (Time - tile_data[1])*350*speed*(h/900)               
            pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                #### 미스판정 추가####
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1 
                combo_effect2 = 1.3
                rate = "MISS"
                ######################
                t2.remove(tile_data)

        for tile_data in t3:
            tile_data[0] = 0 - (h/12)*9 + (Time - tile_data[1])*350*speed*(h/900)               
            pygame.draw.rect(screen, (255, 255, 255), (w/2, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                #### 미스판정 추가####
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1 
                combo_effect2 = 1.3
                rate = "MISS"
                ######################
                t3.remove(tile_data)

        for tile_data in t4:
            tile_data[0] = 0 - (h/12)*9 + (Time - tile_data[1])*350*speed*(h/900)               
            pygame.draw.rect(screen, (255, 255, 255), (w/2 + w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                #### 미스판정 추가####
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1 
                combo_effect2 = 1.3
                rate = "MISS"
                ######################
                t4.remove(tile_data)



    # blinder----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, -int(w/100), w/4, h + int(w/50)), int(w/100)) # 화면 line

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, (h/12)*9, w/4, h/2))
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, (h/12)*9, w/4, h/2), int(h/100))

        

    # key design---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        pygame.draw.rect(screen, (255 - 100 * keys[0],255 - 100 * keys[0], 255 - 100 * keys[0]), (w / 2 - w / 9, (h / 24) * 19 + (h / 48) * keys[0], w / 27, h / 8), int(h / 150))
        pygame.draw.rect(screen, (255 - 100 * keys[3],255 - 100 * keys[3], 255 - 100 * keys[3]), (w / 2 + w / 13.5, (h / 24) * 19 + (h / 48) * keys[3], w / 27, h / 8), int(h / 150))

        pygame.draw.circle(screen, (150, 150, 150), (w / 2, (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.line(screen, (150, 150, 150), (w / 2 - math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 - math.cos(spin) * 25 * (w / 1600)), (w / 2 + math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 + math.cos(spin) * 25 * (w / 1600)), int(w / 400))
        spin += (speed / 20 * (maxframe / fps))


        pygame.draw.rect(screen, (255 - 100 * keys[1], 255 - 100 * keys[1], 255 - 100 * keys[1]), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8))
        pygame.draw.rect(screen, (0,0, 0), (w / 2 - w / 18, (h / 48) * 43 + (h / 48) * (keys[1] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8), int(h / 150))

        pygame.draw.rect(screen, (255 - 100 * keys[2], 255 - 100 * keys[2], 255 - 100 * keys[2]), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8))
        pygame.draw.rect(screen, (0, 0, 0), (w / 2 + w / 58, (h / 48) * 43 + (h / 48) * (keys[2] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8), int(h / 150))

    # 폰트 그리기

        miss_text.set_alpha(255 - (255/4)*miss_anim)
        
        screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/12)*4 - combo_text.get_height()/2))
        screen.blit(rate_text, (w/2 - rate_text.get_width()/2, (h/12)*8 - rate_text.get_height()/2))
        screen.blit(miss_text, (w/2 - rate_text.get_width()/2, (h/12)*4 - rate_text.get_height()/2))        

        pygame.display.flip()

        clock.tick(maxframe)

main = False            # 화면 나가기를 위한 값 변환 
ingame = False          # 화면 나가기를 위한 값 변환 