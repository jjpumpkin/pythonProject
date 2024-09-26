from tkinter import *
from PIL import Image, ImageTk
# pip install pillow 이미지관련 라이브러리
def move_left(event):
    print('왼쪽')
    canvas.move(item,-20,0)
def move_right(event):
    print('오른쪽')
    canvas.move(item,20,0)
def move_down(event):
    print('아래쪽')
    canvas.move(item,0, 20)
def move_up(event):
    print('위쪽')
    canvas.move(item, 0, -20)
app =Tk()
canvas = Canvas(app,width=400,height=300)
canvas.pack()            #x1,y1,x2,y2 사각형에 원을 그림 좌상단과 우하단의 좌표
item = canvas.create_oval(100,150,150,200,fill='red')
app.bind('<Left>', move_left)
app.bind('<Right>', move_right)
app.bind('<Down>', move_down)
app.bind('<Up>', move_up)
app.mainloop()