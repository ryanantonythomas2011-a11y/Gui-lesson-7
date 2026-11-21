import time
from tkinter import*
from tkinter import messagebox

screen = Tk()
screen.geometry("400x200")

hour = StringVar()
min = StringVar()
sec = StringVar()

hour.set("00")
min.set("00")
sec.set("00")

hour_entry = Entry(screen,width=10,textvariable=hour)
hour_entry.place(x=100,y=100)
min_entry = Entry(screen,width=10,textvariable=min)
min_entry.place(x=200,y=100)
sec_entry = Entry(screen,width=10,textvariable=sec)
sec_entry.place(x=300,y=100)


def countdown():
    Countdown = int(hour.get())*3600 + int(min.get())*60 + int(sec.get())
    hour_entry.config(state="disabled")
    min_entry.config(state="disabled")
    sec_entry.config(state="disabled")
    time_button.config(state="disabled")
    while Countdown >= 0:
        m,s = divmod(Countdown,60)
        h = 00
        if m > 60:
            h,m = divmod(m,60)
        hour.set("{00:2d}".format(h))
        min.set("{00:2d}".format(m))
        sec.set("{00:2d}".format(s))
        screen.update()
        time.sleep(1)
        if Countdown == 0:
            messagebox.showinfo("Time Done","Time's Up")
        Countdown -= 1   


time_button = Button(screen,text="Start Timer",command=countdown)
time_button.place(x=200,y=150)

mainloop()


