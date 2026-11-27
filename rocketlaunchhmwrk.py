
from tkinter import *

screen = Tk()
screen.geometry("400x250")
screen.title("Rocket Launch")

count = 10

timer = StringVar()
status = StringVar()

timer.set("10")
status.set("Preparing...")

timer_label = Label(screen, textvariable=timer, font=("Arial", 30))
timer_label.place(x=175, y=20)

status_label = Label(screen, textvariable=status, font=("Arial", 15))
status_label.place(x=120, y=90)

def countdown():
    global count

    timer.set(str(count))

    if count > 5:
        status.set("Engine Start")

    elif count <= 5 and count > 0:
        status.set("Ignition Sequence...")

    elif count == 0:
        status.set("BLASTOFF!!")
        return

    count -= 1
    screen.after(1000, countdown)


def launch():
    launch_button.config(state="disabled")
    countdown()


launch_button = Button(screen, text="Launch", command=launch)
launch_button.place(x=175, y=150)

mainloop()
