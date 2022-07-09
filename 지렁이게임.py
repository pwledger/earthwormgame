# 파이썬으로 간단한 게임 만들고 github 에 올려 보자

# pygame: 파이썬으로 간단한 고전 게임을 만들수 있는 오픈 소스 입니다.
 
# pip install pygame  설치 해야지 모듈이 있습니다


import sys
import pygame
from  pygame.locals import QUIT , Rect , KEYDOWN ,\
    K_LEFT , K_RIGHT , K_UP , K_DOWN 


pygame.init()
pygame.key.set_repeat(5,5)
배경 = pygame.display.set_mode((600,600))  # 화면 크기
클럭 = pygame.time.Clock()

earthworms = [[10,10]]

def 지렁이그리기():
    for i in earthworms:
        pygame.draw.rect(배경 , (0,255,0), (i[0]*30,i[1]*30,30,30))

def 라인그리기():
    for x in range(0,20):
        pygame.draw.line(배경 , (255,255,255) , (x*30,0) , (x*30,600) , 3)
        pygame.draw.line(배경 , (255,255,255) , (0,x*30) , (600,x*30) , 3)
   
def main():
    key = K_DOWN
    while True:
        배경.fill((0,0,0))  # 배경색에 대한 변경
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        if key == K_DOWN:
            head = [earthworms[0][0] , earthworms[0][1] +1]
        elif key == K_UP:
            head = [earthworms[0][0] , earthworms[0][1] -1]
        elif key == K_LEFT:
            head = [earthworms[0][0] -1 , earthworms[0][1]]
        elif key == K_RIGHT:
            head = [earthworms[0][0]+1 , earthworms[0][1]]

        earthworms.insert(0,head)
        earthworms.pop()
         
        라인그리기()
        지렁이그리기()
        pygame.display.update()
        클럭.tick(5)

main()

