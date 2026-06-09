from tkinter import *
from constants import *

window = Tk()
window.title('Countdown')
window.config(padx=10 , pady=10, bg=SNOW_WHITE)


canvas = Canvas(width=600, height=600, bg=SNOW_WHITE, highlightthickness= 0)

clock_img = PhotoImage(file='clock.png')
clock_img = clock_img.subsample(2,2)
canvas.create_image(300, 300, image=clock_img)

canvas.create_text(300, 325, text='00:00', font= FONT_COUNTDOWN)

canvas.create_text(300,230, text='Timer', font= FONT_TEXT, fill= PASTEL_TURQUOISE)

start_button = Button(canvas, text='Start', font=FONT_BUTTON_START, fg= DEEP_TEAL_BLUE)
start_button.place(x=180, y=410)


canvas.pack()

window.mainloop()
