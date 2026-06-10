from tkinter import *
from constants import *
import math

reps = 0

def count_down(count):
    count_min = math.floor(count / 60 )
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_countdown, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '🗹'
            canvas.itemconfig(check_mark, text= marks)

def start_timer():
    global reps
    reps += 1

    work_time   = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break  = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(timer_title, text='Long break')
        count_down(long_break)
    elif reps % 2 == 0:
        canvas.itemconfig(timer_title, text='Short break')
        count_down(short_break)
    else:
        canvas.itemconfig(timer_title, text='Work time')
        count_down(work_time)


window = Tk()
window.title('Countdown')
window.config(padx=10 , pady=10, bg=SNOW_WHITE)

canvas = Canvas(width=600, height=600, bg=SNOW_WHITE, highlightthickness= 0)

clock_img = PhotoImage(file='clock.png')
clock_img = clock_img.subsample(2,2)
canvas.create_image(300, 300, image=clock_img)

timer_countdown = canvas.create_text(300, 325, text='00:00', font= FONT_COUNTDOWN)

timer_title = canvas.create_text(300,230, text='Timer', font= FONT_TEXT, fill= PASTEL_TURQUOISE)

check_mark = canvas.create_text(300,430, font= FONT_MARK, fill= GREEN )

start_button = Button(canvas, text='Start', command= start_timer, font= FONT_BUTTON_START, fg= DEEP_TEAL_BLUE)
start_button.place(x=180, y=410)

reset_button = Button(canvas, text='Reset', font= FONT_BUTTON_START, fg= DEEP_TEAL_BLUE)
reset_button.place(x=370, y=410)



canvas.pack()

window.mainloop()
