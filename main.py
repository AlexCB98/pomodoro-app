from tkinter import *
from constants import *

window = Tk()
window.title('Countdown')
window.config(padx=10 , pady=10, bg=SNOW_WHITE)


canvas = Canvas(width=600, height=600, bg=SNOW_WHITE, highlightthickness= 0)
clock_img = PhotoImage(file='clock.png')
clock_img = clock_img.subsample(2,2)
canvas.create_image(300, 300, image=clock_img)
canvas.create_text(300, 325, text='00:00', font= FONT)
canvas.pack()






window.mainloop()