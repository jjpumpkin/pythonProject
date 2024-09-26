from tkinter import *


app =Tk()
app.geometry("400x300")
app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

entry =Entry(app, width=50)
entry.grid(row=0 ,column=0, padx=10 ,pady=10)
entry.bind("<Return>", )

text =Text(app)
text.grid(row=1, column=0, columnspan=2) # 2칸차지
btn =Button(app, text='추가', )
btn.grid(row=0 ,column=1, padx=10, pady=10)


btn2 =Button(app, text='삭제', )
btn2.grid(row=0, column=2)
app.mainloop()
