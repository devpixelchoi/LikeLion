from tkinter import *       # tkinter 일종의 모듈 클래스
import pandas as pd
import os       # 폴더를 만들고 삭제.... 현재 폴더 위치.
# global data

print(os.getcwd())      # getcwd : get current working directory

# 파일불러오기
dat = pd.read_excel("./NOTAM_Decoder.xlsx")       #, encoding='utf-8')
print(dat)
# 기능추가
# 제출 버튼을 클릭했을 때, 동작 기능.

def click(event=None):
    print("Clicked")
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
label1 = Label(window, text = "CONTRACTIONS(Capital Letters Only) : ")
label1.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=30, bg="light yellow")
entry.grid(row=1, column=0, sticky=W)

# 03 제출버튼 추가
btn = Button(window, width=7, height=2, text = "Enter", command=click)
btn.grid(row=2, column=0, sticky=W)


# 04 설명 레이블 - 의미
label2 = Label(window, width=50, bg="light blue" ,text = "Answer : ")
label2.grid(row=3,column=0) #, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=20, wrap=WORD, background="light pink")
output.grid(row=4, column=0, columnspan=3, sticky=W)

# result = Entry(window, width=50, bg = "light pink")
# result.grid(row=4, column=0, sticky=W)

# 메인 반복문 실행
window.bind("<Return>", click)
window.mainloop()
