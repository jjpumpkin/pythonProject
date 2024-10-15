import threading
import tkinter as tk
import time
def long_task():
    time.sleep(5)
    label.config(text="작업 완료")

def task():
    threading.Thread(target=long_task).start()

app =tk.Tk()
label = tk.Label(app, text='작업중...')
label.pack()

btn =tk.Button(app, text="시작", command=long_task)
btn.pack()

app.mainloop()