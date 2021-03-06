import tkinter
from tkinter import *       # tkinter 일종의 모듈 클래스
from tkinter import scrolledtext
import pandas as pd
import os       # 폴더를 만들고 삭제.... 현재 폴더 위치.
# global data

#print(os.getcwd())      # getcwd : get current working directory

# 파일불러오기
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 150)
dat = pd.read_excel("./NOTAM_Decoder.xlsx") #, encoding='utf-8')
# dat = pd.DataFrame(dat)
subset = dat.head(n=359)[['CONTRACTIONS','DECODE']]
print(dat)
# print(subset)
# 기능추가
# 제출 버튼을 클릭했을 때, 동작 기능.

def click(event=None):
   # print("Clicked")
    # pass
    word = entry.get()

    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 사용한다
    output.delete(0.0, END)

    try:
        def_word = dat.loc[dat["CONTRACTIONS"]==word.upper(), 'DECODE'].values[0]   # 입력값을 대문자로 변환
    except:
        def_word = "Couldn't find on list"
        # dat = window_add(dat)
    output.insert(END, def_word)


window = Tk()
window.title("NOTAM DECODER")

# 01 입력 상자 설명 레이블
label1 = Label(window, text = "CONTRACTIONS : ")
label1.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=75, bg="light yellow")
entry.grid(row=1, column=0, sticky=W)

# 03 제출버튼 추가
btn = Button(window, width=7, height=2, text = "Enter", command=click)
btn.grid(row=2, column=0, sticky=W)


# 04 설명 레이블 - 의미
label2 = Label(window, width=75, bg="light blue" ,text = "DECODE")
label2.grid(row=3,column=0) #, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=75, height=3, wrap=WORD, background="light pink")
output.grid(row=4, column=0, columnspan=2, sticky=W)
# 06 전체 리스트 출력
label3 = Label(window, width=75, bg="light blue" ,text = "List")
label3.grid(row=5, column=0) #, stickey=W, pady=10, padx=5)

scrollbar = tkinter.scrolledtext.ScrolledText(window, width=73, height=20, background="light green")
scrollbar.grid(row=6, column=0,  sticky=W)
scrollbar.insert(INSERT,subset)
scrollbar.configure(state='disabled')

#
# scrollbar = tkinter.scrolledtext.ScrolledText(window, background='light green')
# scrollbar.grid(row=6, column=0,width=40, height=30, sticky=W)
# scrollbar.insert(INSERT, subset)
# scrollbar.configure(state='disabled')



# result = Entry(window, width=50, bg = "light pink")
# result.grid(row=4, column=0, sticky=W)

# 메인 반복문 실행
window.bind("<Return>", click)
window.mainloop()
