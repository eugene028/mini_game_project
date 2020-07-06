from animal import *
import random as rd
import time
from tkinter import *

#10문제 게임생성
animal_dic = [개, 고양이, 너구리, 호랑이, 햄스터, 다람쥐, 토끼, 고슴도치, 돼지, 거북이, 양, 사슴, 말, 캥거루, 원숭이, 참새, 까치
            , 개구리, 닭, 비둘기]
answer_li = rd.sample(animal_dic, 10)
que = ["첫", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열"]
#시간추출
start = time.time()
t = time.time() - start

#시간점수계산해주는 함수
def timeScore(time):
    realtime=round(time,0)
    return 120-realtime//5

#플레이어한테 보여주는 시간함수
def showTime(time):
    local_time=time.localtime(time)
    print("걸린 시간은", time.strftime(' %M:%S', local_time))




