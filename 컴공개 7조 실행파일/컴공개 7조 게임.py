import tkinter as tk
from tkinter.font import *
from setting import *
import pandas as pd
from tkinter import ttk
import idiomdic as i
import openpyxl
import random as rd
import time

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("Word Cup!")
        self.geometry("1000x700")
        self.resizable(0, 0)
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#사전의 단어를 리스트화 시킨다.
path3_1 = 'dictionary.xlsx'
df = pd.read_excel(path3_1)
df = df.fillna('0')
word0 = df.values.tolist()
word = sum(word0,[])
word.sort()
word = word[20691:]



class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Word Cup!", font=Font(family="궁서체", size="100")).pack(side="top", fill="x", pady=50)
        tk.Button(self, text="사자성어게임", height=5, width=20, command=lambda: master.switch_frame(Game1_1)).pack(pady=5)
        tk.Button(self, text="동물맞추기게임", height=5, width=20,
                  command=lambda: master.switch_frame(Game2_1)).pack(pady=5)
        tk.Button(self, text="끝말잇기게임",command=lambda:master.switch_frame(Game3), height=5, width=20).pack(pady=5)

class Game1_1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='사자성어게임', font=Font(family="맑은 고딕", size=20, weight="bold")).pack(pady=30)
        tk.Label(self, text="<게임설명>\n\n\
                    1.사자성어의 뜻풀이에 해당하는 질문에 맞는 사자성어를 입력하세요.\n\n\
                    2.문제를 풀다가 푼 문제수가 30일 때 엔터키를 누르면 랭크입력창이 생성됩니다.\n\n\
                    3.입력창에서 랭크에 기록할 이름을 입력하면 랭킹이 기록되고 표시됩니다.\n\n\
                    4.점수는 \'맞힌 문제수*10-플레이한 시간\'입니다.", bd="3", relief="solid", justify="left",
                 font=Font(family="맑은 고딕", size=12)).pack(pady=90, ipady=40)

        tk.Button(self, text="게임 시작하기", width=15,
                  command=lambda: master.switch_frame(Game1_2)).pack(pady=60)

class Game1_2(tk.Frame):
    def __init__(self, master):
        font = tkinter.font.Font(family="맑은 고딕", size=14)
        global game3q, game3a, game3s, game3m, save, game3correct, game3name, game3rank, timeuse
        tk.Frame.__init__(self, master)
        title3 = tk.Label(self, text='사자성어', font=font)
        title3.pack(side='top', anchor='center')
        tk.Button(self, text="메뉴로 돌아가기", font=tkinter.font.Font(family="맑은 고딕", size=10),
                  command=lambda: master.switch_frame(StartPage)).pack(side='top', anchor='e')
        start = time.time()

        def record(event):
            global game3q, game3a, game3s, game3m, save, game3correct, game3name, game3rank, timeuse
            path = 'idiomdata.csv'
            df = pd.read_csv(path, index_col=[0])
            new_df = pd.DataFrame(
                [{'Name': game3name.get(), 'Score': game3correct.cget('text') * 10 - round(timeuse, 3)}])
            df = pd.concat([df, new_df], ignore_index=True)
            df = df.sort_values(by='Score', ascending=False)
            whoareyou = df['Name'] == game3name.get()
            who = df[whoareyou]
            game3rank.configure(text=who)
            df.to_csv(path)

        def idiom(event):
            global game3q, game3a, game3s, game3m, save, game3correct, game3name, game3rank, timeuse
            Game3q = game3q.cget('text')
            Game3a = game3a.get()
            if game3count.cget('text') < 30:
                if Game3a in i.list1 and i.list1.index(Game3a) == i.list3.index(Game3q):
                    game3s.configure(text=i.list2[save])
                    game3m.configure(text=Game3q)
                    del i.list2[i.list1.index(Game3a)]
                    del i.list3[i.list1.index(Game3a)]
                    i.list1.remove(Game3a)
                    game3count.configure(text=game3count.cget('text') + 1)
                    game3correct.configure(text=game3correct.cget('text') + 1)
                    game3q.configure(text=rd.choice(i.list3))
                    Game3q = game3q.cget('text')
                    save = i.list3.index(Game3q)
                    game3a.delete(0, 4)

                elif Game3a not in i.list1 or i.list1.index(Game3a) != i.list3.index(Game3q):
                    game3s.configure(text=i.list2[save])
                    game3m.configure(text=Game3q)
                    game3count.configure(text=game3count.cget('text') + 1)
                    game3q.configure(text=rd.choice(i.list3))
                    Game3q = game3q.cget('text')
                    save = i.list3.index(Game3q)
                    game3a.delete(0, 4)

            elif game3count.cget('text') == 30:
                timeuse = time.time() - start
                score = game3correct.cget('text')
                game3line.configure(font = font, text = '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                plzname = tk.Label(self, text='랭킹에 등록할 이름을 입력하세요', height=3,
                                   font=tkinter.font.Font(family="맑은 고딕", size=12))
                plzname.pack()
                game3name = tk.Entry(self)
                game3name.pack()
                name = game3name.get()
                game3name.bind('<Return>', record)
                game3rank = tk.Label(self, text='', font=font)
                game3rank.pack()

        game3q = tk.Label(self, text=rd.choice(i.list3), font=font, width=100, height=5)
        game3q.pack()
        save = i.list3.index(game3q.cget('text'))
        game3a = tk.Entry(self, width=100)
        game3a.pack()
        game3sm = tk.Label(self, text = '<설명>', font=font, height=3)
        game3sm.pack()
        game3s = tk.Label(self, text='', font=font, height=5)
        game3s.pack()
        game3m = tk.Label(self, text='', font=font, width=100)
        game3m.pack()
        game3line = tk.Label(self, text = '')
        game3line.pack()
        game3a.bind('<Return>', idiom)
        kcount = tk.Label(self, text='푼 문제수 :', font=tkinter.font.Font(family="맑은 고딕", size=10))
        kcount.place(x=10, y=10)
        game3count = tk.Label(self, text=0, font=tkinter.font.Font(family="맑은 고딕", size=10))
        game3count.place(x=120, y=10)
        kcorrect = tk.Label(self, text='맞은 문제수 :', font=tkinter.font.Font(family="맑은 고딕", size=10))
        kcorrect.place(x=10, y=30)
        game3correct = tk.Label(self, text=0, font=tkinter.font.Font(family="맑은 고딕", size=10))
        game3correct.place(x=120, y=30)

class Game2_1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="동물 맞추기게임", font=Font(family="맑은 고딕", size=20, weight="bold")).pack(pady=30)
        tk.Label(self, text="**이 게임은 총 10개의 라운드가 있으며 매 라운드마다 힌트를 보고 동물을 맞추는 게임입니다.**",
                 font=Font(family="맑음고딕", size=10)).pack()
        tk.Label(self, text="<게임방법>\n\n\
                    1.힌트는 총 7개이며 원하는 힌트버튼을 누를 때마다 게임점수가 1점씩 깎이면서 힌트를 볼 수 있습니다.\n\n\
                    2.힌트를 보고 정답을 알았다면 입력창에 동물이름을 입력하고 확인버튼을 누릅니다.\n\n\
                    3.정답이라면 얻음점수를 가져가고 틀렸다면 그 라운드는 0점입니다.\n\n\
                    4.다음버튼을 눌러 다음라운드도 똑같이 진행하세요.", bd="3", relief="solid", justify="left",
                 font=Font(family="맑은 고딕", size=12)).pack(pady=90, ipady=40)

        tk.Button(self, text="게임 시작하기", width=15,command=lambda: master.switch_frame(Game2_2)).pack(pady=40)


class Game2_2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.score = 7
        self.i = 0
        self.start = time.time()
        Q_score = []

        def reset():
            if self.i != 9:
                imf1.config(text="")
                imf2.config(text="")
                imf3.config(text="")
                imf4.config(text="")
                imf5.config(text="")
                imf6.config(text="")
                imf7.config(text="")
                answer.delete(0, END)
                self.i += 1
                la.config(text="<%s 번째 문제> 어떤동물일까요? " % que[self.i],
                          font=Font(family="맑은 고딕", size=15, weight='bold'))
                self.score = 7
                gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score),
                                 font=Font(family="맑은 고딕", size=15))

            else:
                global Final_score
                Final_score = sum(Q_score)
                global time_score
                time_score = time.time() - self.start
                master.switch_frame(EndGame)

        def open1():
            self.score -= 1
            imf1.config(text=answer_li[self.i]["종류"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open2():
            self.score -= 1
            imf2.config(text=answer_li[self.i]["생김새"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open3():
            self.score -= 1
            imf3.config(text=answer_li[self.i]["서식지"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open4():

            self.score -= 1
            imf4.config(text=answer_li[self.i]["먹이"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open5():

            self.score -= 1
            imf5.config(text=answer_li[self.i]["특징1"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open6():

            self.score -= 1
            imf6.config(text=answer_li[self.i]["특징2"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def open7():

            self.score -= 1
            imf7.config(text=answer_li[self.i]["특징3"])
            gameScore.config(text="%s번째 게임점수\n %d점" % (que[self.i], self.score))

        def scoring():

            if answer.get() == answer_li[self.i]["답"]:
                answer.delete(0, END)
                answer.insert(0, "정답입니다.")
                Q_score.append(self.score)

            else:
                answer.delete(0, END)
                answer.insert(0, "틀렸습니다. 답은 %s입니다." % answer_li[self.i]["답"])

        def tiktok():
            localtime = time.localtime(time.time() - self.start)
            now = time.strftime(" %M:%S", localtime)
            clock.config(text=str(now))
            self.after(1000, tiktok)

        clock = tk.Label(self, text="00:00", font=Font(family="궁서", size=25), fg="red", bg="yellow", width=7, height=2)
        clock.grid(row=0, column=0, padx=10, pady=10)
        tiktok()

        title = tk.Label(self, text="동물맞추기게임", font=Font(family="맑음고딕", size=30, weight="bold"))
        title.grid(row=0, column=1, sticky="E", padx=20, pady=20)
        menu = tk.Button(self, text="메뉴로 돌아가기", font=Font(family="맑음고딕", size=13),
                         command=lambda: master.switch_frame(StartPage))
        menu.grid(row=0, column=2, sticky="E", padx=50)
        la = tk.Label(self, text="<%s 번째 문제> 어떤동물일까요? " % que[self.i],
                      font=Font(family="맑은고딕", size=15, weight='bold'))
        la.grid(row=1, column=0, columnspan=2, sticky="W", pady=30, padx=30)

        hint1 = tk.Button(self, text="종류", command=open1, font=Font(family="맑은고딕", size=15))
        hint1.grid(row=2, column=0, pady=5)
        hint2 = tk.Button(self, text="생김새", command=open2, font=Font(family="맑은고딕", size=15))
        hint2.grid(row=3, column=0, pady=5)
        hint3 = tk.Button(self, text="서식지", command=open3, font=Font(family="맑은고딕", size=15))
        hint3.grid(row=4, column=0, pady=5)
        hint4 = tk.Button(self, text="먹이", command=open4, font=Font(family="맑은고딕", size=15))
        hint4.grid(row=5, column=0, pady=5)
        hint5 = tk.Button(self, text="특징1", command=open5, font=Font(family="맑은고딕", size=15))
        hint5.grid(row=6, column=0, pady=5)
        hint6 = tk.Button(self, text="특징2", command=open6, font=Font(family="맑은고딕", size=15))
        hint6.grid(row=7, column=0, pady=5)
        hint7 = tk.Button(self, text="특징3", command=open7, font=Font(family="맑은고딕", size=15))
        hint7.grid(row=8, column=0, pady=5)

        imf1 = tk.Label(self, text="", width=120)
        imf1.grid(row=2, column=1, columnspan=2)
        imf2 = tk.Label(self, text="", width=120)
        imf2.grid(row=3, column=1, columnspan=2)
        imf3 = tk.Label(self, text="", width=120)
        imf3.grid(row=4, column=1, columnspan=2)
        imf4 = tk.Label(self, text="", width=120)
        imf4.grid(row=5, column=1, columnspan=2)
        imf5 = tk.Label(self, text="", width=120)
        imf5.grid(row=6, column=1, columnspan=2)
        imf6 = tk.Label(self, text="", width=120)
        imf6.grid(row=7, column=1, columnspan=2)
        imf7 = tk.Label(self, text="", width=120)
        imf7.grid(row=8, column=1, columnspan=2)

        gameScore = tk.Label(self, text="%s번째 게임점수\n %d점" % (que[self.i], self.score),
                             font=Font(family="맑은고딕", size=15))
        gameScore.grid(row=9, column=0, pady=30)
        answer = tk.Entry(self, bg='white', width=20)
        answer.grid(row=9, column=1, ipadx=20, ipady=7)
        submit = tk.Button(self, text="확인", command=scoring, font=Font(family="맑은고딕", size=20))
        submit.grid(row=9, column=2, pady=30)
        next = Button(self, command=reset, text="다음문제", width=20)
        next.grid(row=10, column=2)


class EndGame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="게임이 끝났습니다", font=Font(family="맑음고딕", size=30, weight="bold")).grid(row=0, column=1,
                                                                                                pady=30)
        tk.Label(self, text="당신의 문제점수는 {}점입니다.\n당신의 시간점수는 {}점입니다.".format(Final_score, timeScore(time_score)),
                 font=Font(family="맑음고딕", size=20)).grid(row=1, column=1, pady=30)
        tk.Button(self, text="메인 화면으로 돌아가기", height=3, width=20,
                  command=lambda: master.switch_frame(StartPage)).grid(row=2, column=0, pady=30)
        tk.Button(self, text="랭크 입력하기", height=3, width=20, command=lambda: master.switch_frame(WriteRank)).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 pady=30)
        tk.Button(self, text="랭크 보기", height=3, width=20, command=lambda: master.switch_frame(ShowRank)).grid(row=2,
                                                                                                              column=2,
                                                                                                              pady=30)


class ShowRank(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="랭크입니다!",font=Font(family="맑은 고딕",
                                               size=30, weight="bold")).grid(row=0, column=0)
        tk.Label(self, text="이름",font=Font(family="맑은 고딕", size=15)).grid(row=1, column=0)
        tk.Label(self, text="점수",font=Font(family="맑은 고딕", size=15)).grid(row=1, column=1)
        path = 'animal_rank.xlsx'
        df = pd.read_excel(path)
        df = df.sort_values('점수', ascending=False)

        def change(event, row, col):
            value = event.widget.get()
            df.iloc[row, col] = value

        rows, cols = df.shape

        for r in range(rows):
            for c in range(cols):
                e = tk.Entry(self)
                e.insert(0, df.iloc[r, c])
                e.grid(row=r + 3, column=c)
                e.bind('<Return>', lambda event, y=r, x=c: change(event, y, x))
                e.bind('<KP_Enter>', lambda event, y=r, x=c: change(event, y, x))
        tk.Button(self, text="메인화면으로 돌아가기", font=Font(family="맑음고딕", size=15),
                  command=lambda: master.switch_frame(StartPage)).grid(row=r + 4, column=0, pady=4)


class WriteRank(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def submit_fields():
            path = 'animal_rank.xlsx'
            df1 = pd.read_excel(path)
            SeriesA = df1['이름']
            SeriesB = df1['점수']
            A = pd.Series(entry1.get())
            B = pd.Series(Final_score + timeScore(time_score))
            SeriesA = SeriesA.append(A)
            SeriesB = SeriesB.append(B)
            df2 = pd.DataFrame({"이름": SeriesA, "점수": SeriesB})
            df2.to_excel(path, index=False)
            entry1.delete(0, END)

        tk.Label(self, text="랭크를 입력하세요", font=Font(family="맑은 고딕", size=20,
                                                   weight="bold")).grid(row=0, column=1)
        tk.Label(self, text="이름", font=Font(family="맑은 고딕", size=15)).grid(row=1, column=0, pady=30)
        tk.Label(self, text="최종점수는 {}점".format(Final_score + timeScore(time_score)),
                 font=Font(family="맑은 고딕", size=15)).grid(row=2, column=0, pady=30)

        entry1 = tk.Entry(self)

        entry1.grid(row=1, column=2)

        tk.Button(self, text="메인화면으로 돌아가기",
                  command=lambda: master.switch_frame(StartPage)).grid(row=3, column=0,pady=4)
        tk.Button(self, text="입력하기", command=submit_fields).grid(row=3, column=1, pady=4)
        tk.Button(self, text="랭크보기", command=lambda: master.switch_frame(ShowRank)).grid(row=3, column=2,
                                                                                         pady=4)


a = 0
yes = 0
no = 0

minutes = 0
seconds = 0
c = rd.choice(word)
c_1 = c

class Game3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def enter(event):
            global a
            global yes
            global no
            global c
            global c_1
            user = user_1.get()
            if yes + no + a < 10:
                if a == 0:
                    a = a + 1
                    user_1.delete(0, tk.END)
                    c = rd.choice(word)
                    c_announce.config(text="컴퓨터: {}".format(c))
                    update_stopwatch()
                elif user in word:
                    if c[-1] == user[0]:
                        yes = yes + 1
                        c_next = list(filter(lambda s: s.startswith((user[-1])), word))
                        if c_next == []:
                            user_1.delete(0, tk.END)
                            word.remove(c)
                            word.remove(user)
                            c = rd.choice(word)
                            c_announce.config(text='끝말로 시작하는 단어가 없습니다. 컴퓨터: {}'.format(c))
                        else:
                            user_1.delete(0, tk.END)
                            word.remove(c)
                            word.remove(user)
                            c = rd.choice(c_next)
                            c_announce.config(text='컴퓨터: {}'.format(c))
                    else:
                        user_1.delete(0, tk.END)
                        word.remove(c)
                        word.remove(user)
                        c = rd.choice(word)
                        c_announce.config(text='끝 어절과 맞지 않습니다. 컴퓨터: {}'.format(c))
                else:
                    no = no + 1
                    user_1.delete(0, tk.END)
                    word.remove(c)
                    c = rd.choice(word)
                    c_announce.config(text='사전에 없는 단어입니다. 컴퓨터: {}'.format(c))

            elif yes + no + a == 10:
                if user in word:
                    if c[-1] == user[0]:
                        yes = yes + 1
                        user_1.delete(0, tk.END)
                        c_announce.config(text='게임 종료. 아래에 결과가 출력됩니다.')
                        status.config(text='점수는 100점 만점에 {} 점입니다.'.format(yes * 10))
                        used_time.config(text='{}분{}초 소요'.format(minutes, seconds))
                        tk.Label(self, text='<결과>', font=Font(family="맑은 고딕", size=15)).pack()
                        tk.Button(self, text='이름 입력', command=input_name, font=Font(family="맑은 고딕", size=15)).pack()
                    else:
                        no = no + 1
                        user_1.delete(0, tk.END)
                        c_announce.config(text='게임종료. 아래에 결과가 출력됩니다')
                        status.config(text='점수100점 만점에 {} 점입니다.'.format(yes * 10))
                        used_time.config(text='{}분{}초 소요'.format(minutes, seconds))
                        tk.Label(self, text='<결과>', font=Font(family="맑은 고딕", size=15)).pack()
                        tk.Button(self, text='이름 입력', command=input_name, font=Font(family="맑은 고딕", size=15)).pack()
                else:
                    no = no + 1
                    user_1.delete(0, tk.END)
                    c_announce.config(text='게임종료. 아래에 결과가 출력됩니다.')
                    status.config(text='점수는 100점 만점에 {} 점입니다.'.format(yes * 10))
                    used_time.config(text='{}분{}초 소요'.format(minutes, seconds))
                    tk.Label(self, text='<결과>', font=Font(family="맑은 고딕", size=15)).pack()
                    tk.Button(self, text='이름 입력', command=input_name, font=Font(family="맑은 고딕", size=15)).pack()

        def update_stopwatch():
            global minutes
            global seconds
            if seconds < 59:
                seconds += 1
            elif seconds == 59:
                seconds = 0
                minutes += 1
            time_string = "{:02d}:{:02d}".format(minutes, seconds)
            stopwatch.config(text=time_string, font=Font(family="맑은 고딕", size=15))
            self.after(1000, update_stopwatch)
            if yes + no == 10:
                return

        def input_name():
            global name
            name = tk.Entry(self, font=Font(family="맑은 고딕", size=15))
            name.pack()
            tk.Button(self, text='확인', font=Font(family="맑은 고딕", size=15), command=rank_naming).pack()

        def rank_naming():
            global a
            global yes
            global no
            global x
            path3_2 = 'ranking.xlsx'
            df1 = pd.read_excel(path3_2)
            SeriesA = df1['이름']
            SeriesB = df1['점수']
            x = str(name.get())
            y = 10 * yes
            A = pd.Series(x)
            B = pd.Series(y)
            SeriesA = SeriesA.append(A)
            SeriesB = SeriesB.append(B)
            df2 = pd.DataFrame({"이름": SeriesA, "점수": SeriesB})
            df2.to_excel(path3_2, index=False)
            path3_2 = 'ranking.xlsx'
            df5 = pd.read_excel(path3_2)
            df5 = df5.sort_values("점수", ascending=False)
            df5 = df5.reset_index(drop=True)
            tk.Label(self, text=df5, font=Font(family='맑은 고딕', size=15)).pack()

        c_announce = tk.Label(self, text='\'시작\'을 입력하세요', font=Font(family="맑은 고딕", size=15))
        c_announce.pack()

        status = tk.Label(self, font=Font(family="맑은 고딕", size=15))
        status.pack()

        stopwatch = tk.Label(self)
        stopwatch.pack()

        used_time = tk.Label(self, font=Font(family="맑은 고딕", size=15))
        used_time.pack()

        user_1 = tk.Entry(self, font=Font(family="맑은 고딕", size=15))
        user_1.pack()
        user_1.bind('<Return>', enter)

        tk.Button(self, text="메인 화면으로 돌아가기",command = lambda : master.switch_frame(StartPage)).pack()






if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()