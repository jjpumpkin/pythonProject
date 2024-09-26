from tkinter import *
from PIL import Image, ImageTk
# pip install pillow 이미지관련 라이브러리

def move_left(event):
    print('왼쪽')
    canvas.move('tiger',-20,0)
def move_right(event):
    print('오른쪽')
    canvas.move('tiger',20,0)
def move_down(event):
    print('아래쪽')
    canvas.move('tiger',0, 20)
def move_up(event):
    print('위쪽')
    canvas.move('tiger', 0, -20)
def move_space(event):
    jump_height =10
    canvas.update()
    canvas.after(20)
    # Move the ball upwards
    for _ in range(jump_height):
        canvas.move('tiger')




app =Tk()
canvas = Canvas(app,width=400,height=300)
canvas.pack()            #x1,y1,x2,y2 사각형에 원을 그림 좌상단과 우하단의 좌표
img =Image.open('../../python_base/ex_util/tiger.png')
img =img.resize((50, 50))
item = ImageTk.PhotoImage(img)
canvas.create_image(100,100, image=item, tag='tiger')
# item = canvas.create_oval(100,150,150,200,fill='red')
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Down>', move_down)
canvas.bind('<Up>', move_up)
canvas.bind('<space>', move_space)
canvas.focus_set()
app.mainloop()