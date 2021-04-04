from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.header = Label(win, text='Scraping From Social Media')
        self.lbl1 = Label(win, text='Twitter Username: ')
        self.lbl2 = Label(win, text='Facebook Page: ')
        self.lbl3 = Label(win, text='Status')
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        # self.btn1 = Button(win, text='download Tweets')
        # self.btn2 = Button(win, text='download Posts')
        self.header.place(x=120, y=10)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='download Tweets', command=self.add)
        self.b2 = Button(win, text='download Posts')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=250, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        result = "Success"
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        result = "Success"
        self.t3.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
