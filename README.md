# Python으로 간단한 게임 만들기 프로젝트🕹
## Word Cup Game 🎮

제작자 : 강민석, 김영찬, 김원준, 김유진, 이수연

## 1. 게임 제작의 목적
초등학교 저학년이 학습적으로도 발달할 수 있도록 학습적인 측면을 고려하여 사자성어 맞추기, 동물 맞추기, 끝말잇기를 통합해 “Word Cup”이라는 이름으로 게임을 제작했습니다.
게임은 총 세 파트로 나뉘어져 있으며, 사자성어, 동물 맞추기, 끝말잇기 파트로 이루어져 있습니다.

## 2. 사자성어 게임 소개
🙍‍♂️ 제작자 : 김영찬 
### 2-1 사자성어 자료 추출
사자성어를 이용하기 쉽게 정리 해놓은 엑셀, 텍스트 파일이 없어서 Google 문서의 텍스트 추출 기능을 활용하여 PDF 파일의 내용을 추출해 사자성어, 한자, 뜻으로 분류하였습니다!
  
### 2-2 사자성어 게임 구성
사자성어 게임은 랜덤으로 질문이 나오고 플레이어가 답하는 식으로 구성하였습니다. 묻고 답하는 과정에서 푼 문제수가 30문제가 되면 출제를 멈추고, 랭크을 기록하여 플레이어 간의 순위를 비교할 수 있도록 하였습니다. 점수 배점은 (맞힌 문제수) * 10 + 플레이한 시간 입니다.

### 2-3 사자성어 게임 코드 설명
사자성어, 주제별퀴즈, 끝말잇기 세 가지 게임을 Word Cup! 이라는 하나로 모으고, 이벤트와 가시성을 높이기 위해 Tkinter를 활용하여 메인화면을 만들고, 새로운 프레임을 만들어 각각 게임이 대응되어 전환할 수 있도록 했습니다.
<br>
사자성어, 한자, 뜻풀이 자료의 데이터 양이 크기 때문에 `idiomdic.py`라는 새로운 파일을 제작하였습니다. 
`Tkinter의 위젯`을 사용하였고, 각 class 는 화면의 시작, 소개, 플레이 부분을 위해 만들어졌다. 

문제는 총 30문제이고, 30문제가 됬을 때, 총 소요시간을 계산하기 위해 끝났을 때의 시간에서 start를 뺀 timeuse를 저장하였다. 또한 Entry창에 Enter을 누르면 플레이어의 이름을 받는 새로운 Entry창이 생성되어 랭킹을 기록할 수 있도록 def record(event)을 만들었습니다.

![image](https://user-images.githubusercontent.com/67894159/163305373-117c79ff-ffe6-458b-8057-66c0acd18ad8.png)
<게임 진행중>

![image](https://user-images.githubusercontent.com/67894159/163305387-74257b2d-300f-42ed-b1f8-e15ad03933dd.png)
<게임 종료 후 랭크 기록>

## 3. 동물 맞추기 게임 소개
🙍‍♀️🙎‍♀️제작자 : 김유진, 이수연
### 3-1 동물 맞추기 게임 구성
● 게임 형식 정하기
게임은 스무고개 형식으로 진행됩니다. 동물에 대한 부분적인 정보를 플레이어에게 제공한 후, 플레이어가 그 부분적인 정보들을 통해 추론하여 동물의 이름을 맞추는 형식입니다.

● 게임 형성하기
문제가 될 동물을 선정한다. 선정기준은 초등학생이 쉽게 알 수 있는 동물과 특징을 설명하기 쉬운 동물들로 선별하였습니다. `20마리의 동물`을 선택하게 되었고, 리스트는 다음과 같습니다.
[너구리, 호랑이, 햄스터, 개, 고양이, 다람쥐, 토끼, 고슴도치, 돼지, 거북이, 양, 사슴, 말, 캥거루, 원숭이, 참새, 까치, 개구리, 닭, 비둘기]
[종류, 생김새, 서식지, 먹이. 특징1, 특징2, 특징3] 으로 힌트를 구성하여 동물에 대한 정보를 제시합니다.

● 게임 설명 (규칙)
게임 플레이어가 게임 설명 화면에 있는 ‘게임 시작’ 버튼을 누른 순간, 타이머가 작동하며 게임이 시작합니다. 플레이어는 기본적으로 각 문제당 7점을 부여받게 됩니다. 왼쪽에는 각각의 힌트 종류가 있는 버튼이 존재합니다. 그 버튼을 누르면 점수가 1점씩 차감됩니다! 만약 힌트를 모두 보거나 문제를 틀리게 된다면 0점을 얻습니다. <br>
타이머는 시간점수 계산을 위한 것이며 플레이어가 게임을 시작한 후의 경과시간을 알려주기 위해 왼쪽 상단에 위치하고 있습니다. 
시간점수는 플레이 시간이 적을수록 큰 점수를 얻습니다. 플레이어에게 빠른 시간 내에 동물의 이름을 맞추도록 하여 게임에 대한 흥미도를 높이고자 했습니다.

### 3-2 동물 맞추기 게임 코드 설명
● setting, animal. py
게임을 시작하기 전 from setting import * 이라고 하여, setting 파일을 따로 만들어 이를 import 받도록 만들었다. setting.py에는 게임 실행에 필요한 함수들이 들어 있다. 
게임 문제를 생성해주는 animal_dic 리스트와 문제 이름을 정해주는 que 리스트, animal.py를 import하는 코드가 존재한다. 또한 timeScore(time)이라는 함수가 존재해, 시간점수를 계산해 주는 함수도 있다. 여기서 animal.py는 동물에 대한 정보를 dic의 형태로 저장해놓은 파일이다.

● 게임 시작 전 준비화면 (클래스명 Game2_1)
__init__(self, master) 코드를 통해 이 코드의 아래에 진행될 코드가 상위 클래스의 속성을 받아와 기본적으로 실행할 수 있도록 하였다. 또한 tk.Frame.__init__(self,master)을 통해 Frame별로 그 속성이 전달될 수 있도록 하였다. tk.Label(self,~)의 형식으로 프레임 내에 작성해야 할 내용들을 작성하였으며 tk.Button(self~)를 통해 다른 프레임으로 이동하도록 만들었다. 

Game2_1 클래스에는 ‘동물 맞추기 게임’에 대한 소개를 작성하였다. pack()을 통해 위치를 조정하고, 게임 플레이어가 설명을 다 읽으면 버튼을 눌러 게임을 시작할 수 있도록 하였다.
버튼을 누르면 특정 함수가 실행될 수 있도록 ‘command=’를 작성하였는데, 여기서 lambda함수를 활용하였다. lambda:master.switch_frame(Game2_2)를 통해, 상위 클래스 내에 존재하는 switch_frame 함수가 실행될 수 있도록 하였다. 이를 통해 Game2_2 프레임으로 넘어갈 수 있다. [그림 2]의 코드를 실행한 화면이다. 

● 게임 플레이 화면 (클래스명 Game2_2)
마찬가지로 __init__(self,master):을 통해 상위 클래스의 속성을 받아오도록 했다. 이는 중복되는 설명이므로 아래부터는 생략하도록 하겠다. 
self.score=7을 통해, 게임 내내 앞으로 계속 쓰일 점수에 대한 정의를 내렸다. 7점부터 시작하여 앞으로 힌트를 볼 때마다 점수가 깎일 것이다.
또한 ‘i’는 문제의 번호를 의미하여 먼저 ‘i=0’으로 시작하도록 하였고, 코드가 실행되면 타이머가 작동해야 하므로 self.start=time.time()을 입력했다,
Q_score=[]은 플레이어가 각 문제당 얻는 문제점수를 리스트에 추가할 수 있도록 빈 리스트를 생성한 것이다.


reset함수는 첫 문제를 제공하고 나서, ‘다음 문제’ 보기 버튼을 누르면 실행되는데, 플레이어가 전 문제에서 보았던 힌트들을 다시 없애고 다음 문제를 풀 수 있도록 한다.
문제 번호가 9번이 아닐 때까지, 다음과 같은 코드가 실행된다.
imf1.config(text=“”)를 통해 플레이어가 보았던 힌트들을 공백으로 대체한다. 
또한 answer.delete(0,END)를 통해 채점 결과를 지우고, self.i+=1을 통해 문제 번호가 증가되도록 하였다. la.config(~)는 다음 문제임을 안내하고, self.score=7을 통해 각 문제당 다시 7점부터 시작할 수 있도록 하였다.
gameScore.config()는 각 문제당 플레이어가 힌트를 볼 때마다 점수가 바뀌는 것을 볼 수 있게 한다.

다음 코드는 10문제를 풀게 되었을 때, 점수를 계산해주는 코드이다. 
Final_score은 Q_score라는 리스트에 모아놓았던 문제점수의 합을 구하고, time_score은 문제풀이를 시작했던 때와 끝날 때의 차를 구해준다.
이제 게임 실행의 바탕이 되는 코드들에 대한 설명이 끝났다.


다음으로 설명할 코드는 게임 진행에 필요한 코드이다.
먼저 플레이어가 힌트를 볼 수 있는 부분은 다음과 같이 처리해 두었다. 
![image](https://user-images.githubusercontent.com/67894159/163306640-f1855b34-647a-49ac-869a-8ef2e9611595.png)
<br>

게임 힌트 Label
![image](https://user-images.githubusercontent.com/67894159/163306651-0a5c77fc-6d3e-4545-a59b-a01c1048ab23.png)
먼저 힌트를 볼 수 없도록 공백으로 만들어 놓았다.
hintN(N=1,2,3…) 는 버튼을 위한 코드인데, 이 버튼을 누르면 힌트가 나타난다. 버튼에 있는 ‘command=openN’을 통해, 힌트를 볼 수 있는 것이다.<br>
openN 함수는 각각의 힌트를 보여주도록 한다. 이 함수가 작동하게 되면 score는 –1점이 되고, answer_li의 해당 정보를 가져올 수 있도록 한다. 그리고 공백이었던 imfN(N=1,2,3…)이 힌트로 바뀔 수 있도록 config를 사용하였다.<br>
또한, 게임 점수가 실시간으로 바뀌는 것을 볼 수 있도록 gameScore.config(~)를 사용하였다.

scoring()은 채점을 해 주는 함수이다.<br>
Entry를 통해 받은 정답이, answer_li에 해당하는 ‘답’과 같다면, 내가 입력한 정답을 지우고 ‘정답입니다’를 출력하며, 해당 점수를 Q_score의 리스트에 추가한다.<br>
만약 정답이 아니라면, Entry에 존재하는 답을 지우고, 올바른 정답을 알려준다. Q_score에 점수가 추가되지 않는다.<br>

tiktok 함수<br>
타이머를 위한 함수이다. 왼쪽 상단에 게임을 진행하는 동안 타이머가 나타나는데, 이 코드를 통해 플레이어는 게임 시간이 얼마나 경과되었는지 확인할 수 있다. 

### 아래는 게임 화면 캡쳐입니다.
![image](https://user-images.githubusercontent.com/67894159/163306988-b7b3be0f-56f2-45c6-86b8-42371647f633.png)

![image](https://user-images.githubusercontent.com/67894159/163306852-b7faedd7-88d2-4c67-aa4e-756e9638366e.png)
전반적인 게임 실행 화면 레이아웃 구성 

![image](https://user-images.githubusercontent.com/67894159/163306890-a1a49d5d-8bdc-4e23-83ad-3655648b0fa1.png)
게임이 끝났을 때의 모습

![image](https://user-images.githubusercontent.com/67894159/163307022-4044dcdc-f85d-4cac-882d-54fc0a95bd4e.png)
랭크 구현 모습

## 4. 끝말잇기 게임
🙍‍♂️🙍‍♂️ 제작자 : 강민석, 김원준
### 4-1 끝말잇기 게임 구성
● 게임 규칙
끝말잇기는 두 사람이 서로 단어를 주고 받는 게임입니다. 한 사람이 말한 단어의 끝 어절로 시작하며 실제로 존재하는 단어를 말해야지 점수를 얻을 수 있습니다. 

● 게임 진행 과정
끝말잇기 게임은 사용자가 엔트리에 ‘시작’을 입력하고 엔터키를 누르면 시작됩니다. 첫 단어는 컴퓨터가 사전에서 랜덤하게 뽑아 제시합니다. 사용자는 그 단어의 끝 어절로 시작하는 단어를 생각하여 엔트리에 입력한다. 이때, 
1. 만약 사용자의 단어가 사전에 존재하지 않는다면, 컴퓨터는 사용자의 점수를 증가시키지 않고 그대로 둔다. 그리고, 새로운 단어를 사전에서 랜덤하게 뽑아 출력한다. 
2. 만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 같다면, 컴퓨터는 사용자의 점수를 10점 증가시킨다. 그리고, 사용자가 제시한 단어의 끝 어절로 시작하는 단어 중 하나를 사전에서 랜덤하게 출력한다. 
3. 만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 다르며, 컴퓨터는 사용자의 점수를 증가시키지 않고 그대로 둔다. 그리고, 새로운 단어를 사전에서 랜덤하게 뽑아 출력한다. 
4. 만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 같지만, 이후 컴퓨터가 그 단어의 끝 어절로 시작하는 단어를 사전에서 찾을 수 없다면, 점수는 증가시키고, 단어는 사전 전체에서 랜덤하게 출력한다.
와 같은 규칙으로 컴퓨터가 두 번째 단어를 제시합니다. 이후 규칙은 1,2,3,4와 동일합니다. 사용자가 10번째 단어를 제시하면 그 순간 게임은 종료됩니다. 10개 중 n개를 맞추면 점수는 100점 만점에 10* n 점이 됩니다. 게임이 끝나고 자신의 랭킹이 궁금한 사용자가 이름입력 버튼을 누르고 새로 나오는 엔트리에 자신의 이름을 입력한 뒤 확인 버튼을 누르면, 이때까지의 랭킹이 표시됩니다.

### 4-2 끝말잇기 게임 코드 설명

끝말잇기는 사전에 나와 있는 단어를 바탕으로 합니다. 이 코드에서는 사전 속 모든 단어를 정리한 dictionary.xlsx의 내용을 pd.read_excel로 읽어와 내용을 df 변수에 저장했습니다.<br> 공백을 제거하기 위해 `df.fillna`를 이용하여 공백란을 ‘0’이란 문자로 채워주었습니다. 이후 `df.values.tolist`를 하면 df에 저장된 엑셀의 내용이 리스트화 됩니다. 하지만, 이는 이중 리스트라 이것을 `단일 리스트`로 만들어 줘야 합니다. 그래서, `sum(list_name, [])`을 이용해 단일 리스트를 만들었습니다. 이후 기존에 넣어두었던 ‘0’을 제거하기 위해 리스트를 오름차순으로 배열하고 이를 20691번째 인덱스부터 끝까지 슬라이싱했습니다. (0~20690번째 인덱스가 ‘0’이기 때문입니다)

끝말잇기 게임도 다른 게임과 마찬가지로 class 를 활용하여 화면을 전환하고 게임을 구돋시키게 되었습니다. 

if 문을 통해 위의 규칙 1,2,3,4를 적용시켰습니다. 이 함수는 사용자가 엔트리에 글자를 입력하고 엔터키를 누르면 실행됩니다. 사용자가 입력한 경우에 따라 4가지로 결과가 달라집니다. 만약 사용자의 단어가 사전에 존재하지 않는다면, 컴퓨터는 사용자의 점수를 증가시키지 않고 그대로 둡니다. 그리고, 새로운 단어를 사전에서 랜덤하게 뽑아 출력합니다. <br>
만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 같다면, 컴퓨터는 사용자의 점수를 10점 증가시킨다. 그리고, 사용자가 제시한 단어의 끝 어절로 시작하는 단어 중 하나를 사전에서 랜덤하게 출력합니다. 만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 다르며, 컴퓨터는 사용자의 점수를 증가시키지 않고 그대로 둡니다. 그리고, 새로운 단어를 사전에서 랜덤하게 뽑아 출력한다. 만약 사용자의 단어가 사전에 존재하고, 그 첫 어절이 컴퓨터의 끝 어절과 같지만, 이후 컴퓨터가 그 단어의 끝 어절로 시작하는 단어를 사전에서 찾을 수 없다면, 점수는 증가시키고, 단어는 사전 전체에서 랜덤하게 출력합니다.

끝말잇기 게임도 경과 시간을 보여주기 위해 `update_stopwatch` 함수를 정의했습니다. 게임 실행 횟수가 10회로 모두 채워지게 되면 스탑워치가 그때까지 걸린 시간을 반환했습니다.

또한 마찬가지로 랭크를 저장해야 하기 때문에, 랭킹 기능을 이용하였습니다.


 ### 🛠 구현 stack 🛠
 <div align="center">
    <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=python&logoColor=white"/> 
  </div>
