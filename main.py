from tkinter import *
from constants import *
import math

def count_down(count):
    count_min = math.floor(count / 60 )
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'

    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)

def start_timer():
    count_down(25 * 60)

window = Tk()
window.title('Countdown')
window.config(padx=10 , pady=10, bg=SNOW_WHITE)


canvas = Canvas(width=600, height=600, bg=SNOW_WHITE, highlightthickness= 0)

clock_img = PhotoImage(file='clock.png')
clock_img = clock_img.subsample(2,2)
canvas.create_image(300, 300, image=clock_img)

timer = canvas.create_text(300, 325, text='00:00', font= FONT_COUNTDOWN)

canvas.create_text(300,230, text='Timer', font= FONT_TEXT, fill= PASTEL_TURQUOISE)

canvas.create_text(300,430, text='🗹', font= FONT_TICK, fill= GREEN )

start_button = Button(canvas, text='Start', command= start_timer, font= FONT_BUTTON_START, fg= DEEP_TEAL_BLUE)
start_button.place(x=180, y=410)

reset_button = Button(canvas, text='Reset', font= FONT_BUTTON_START, fg= DEEP_TEAL_BLUE)
reset_button.place(x=370, y=410)



canvas.pack()

window.mainloop()
