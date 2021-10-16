from tkinter import *
import time
import os
from urllib.request import urlopen

url = { 
    1: 'https://i.imgur.com/Qr3AgtE.png',
    2: 'https://i.imgur.com/Iuf54DW.png',
    3: 'https://i.imgur.com/7CaUrq7.png',
    12: 'https://i.imgur.com/YNMhr43.png',
    4: 'https://i.imgur.com/4cxio4Z.png',
    5: 'https://i.imgur.com/Jx50jKp.png',
    6: 'https://i.imgur.com/UKLcP7Z.png',
    10: 'https://i.imgur.com/jXUMNIo.png',
    11: 'https://i.imgur.com/XQa9tW8.png',
    7: 'https://i.imgur.com/U6Zj1mR.png',
    8: 'https://i.imgur.com/onZKU6h.png',
    9: 'https://i.imgur.com/L44rlQd.png'}
    

def main():

    window1 = Tk()
    window1.resizable(0, 0)
    window1.geometry('200x200+600+517')
    canvas_1 = Canvas(window1, width=200, height=200)
    canvas_1.pack()
    img1 = PhotoImage(file='img_heart_from_windows\im2.png')
    canvas_1.create_image(1, 1, anchor=NW, image=img1)

    window2 = Toplevel() 
    window2.resizable(0, 0)
    window2.geometry('200x200+400+417')
    canvas_2 = Canvas(window2, width=200, height=200)
    canvas_2.pack()
    img2 = PhotoImage(file='img_heart_from_windows\im3.png')
    canvas_2.create_image(1, 1, anchor=NW, image=img2)

    window3 = Toplevel() 
    window3.resizable(0, 0)
    window3.geometry('200x200+200+317')
    canvas_3 = Canvas(window3, width=200, height=200)
    canvas_3.pack()
    img3 = PhotoImage(file='img_heart_from_windows\im4.png')
    canvas_3.create_image(1, 1, anchor=NW, image=img3)

    window4 = Toplevel() 
    window4.resizable(0, 0)
    window4.geometry('200x200+300+117')
    canvas_4 = Canvas(window4, width=200, height=200)
    canvas_4.pack()
    img4 = PhotoImage(file='img_heart_from_windows\im5.png')
    canvas_4.create_image(1, 1, anchor=NW, image=img4)

    window5 = Toplevel() 
    window5.resizable(0, 0)
    window5.geometry('200x100+500+117')
    canvas_5 = Canvas(window5, width=200, height=100)
    canvas_5.pack()
    img5 = PhotoImage(file='img_heart_from_windows\im6.png')
    canvas_5.create_image(1, 1, anchor=NW, image=img5)

    window6 = Toplevel() 
    window6.resizable(0, 0)
    window6.geometry('200x200+700+117')
    canvas_6 = Canvas(window6, width=200, height=200)
    canvas_6.pack()
    img6 = PhotoImage(file='img_heart_from_windows\im7.png')
    canvas_6.create_image(1, 1, anchor=NW, image=img6)

    window7 = Toplevel() 
    window7.resizable(0, 0)
    window7.geometry('200x100+900+117')
    canvas_7 = Canvas(window7, width=200, height=100)
    canvas_7.pack()
    img7 = PhotoImage(file='img_heart_from_windows\im8.png')
    canvas_7.create_image(1, 1, anchor=NW, image=img7)

    window8 = Toplevel() 
    window8.resizable(0, 0)
    window8.geometry('200x200+1100+117')
    canvas_8 = Canvas(window8, width=200, height=200)
    canvas_8.pack()
    img8 = PhotoImage(file='img_heart_from_windows\im9.png')
    canvas_8.create_image(1, 1, anchor=NW, image=img8)

    window9 = Toplevel() 
    window9.resizable(0, 0)
    window9.geometry('200x200+1200+317')
    canvas_9 = Canvas(window9, width=200, height=200)
    canvas_9.pack()
    img9 = PhotoImage(file='img_heart_from_windows\im10.png')
    canvas_9.create_image(1, 1, anchor=NW, image=img9)

    window10 = Toplevel() 
    window10.resizable(0, 0)
    window10.geometry('200x200+1000+427')
    canvas_10 = Canvas(window10, width=200, height=200)
    canvas_10.pack()
    img10 = PhotoImage(file='img_heart_from_windows\im11.png')
    canvas_10.create_image(1, 1, anchor=NW, image=img10)

    window11 = Toplevel() 
    window11.resizable(0, 0)
    window11.geometry('200x200+800+517')
    canvas_11 = Canvas(window11, width=200, height=200)
    canvas_11.pack()
    img11 = PhotoImage(file='img_heart_from_windows\im12.png')
    canvas_11.create_image(1, 1, anchor=NW, image=img11)

    window12 = Toplevel() 
    window12.resizable(0, 0)
    window12.geometry('200x100+700+717')
    canvas_12 = Canvas(window12, width=200, height=100)
    canvas_12.pack()
    img12 = PhotoImage(file='img_heart_from_windows\im1.png')
    canvas_12.create_image(1, 1, anchor=NW, image=img12)


    window12.mainloop()
    window1.mainloop()
    window2.mainloop()
    window3.mainloop()
    window4.mainloop()
    window5.mainloop()
    window6.mainloop()
    window7.mainloop()
    window8.mainloop()
    window9.mainloop()
    window10.mainloop()
    window11.mainloop()



check_file = os.path.exists('img_heart_from_windows')
if check_file != True:
    os.mkdir('img_heart_from_windows')
    for i in range(1, 13, 1):
        with open(f'img_heart_from_windows\im{i}.png', 'wb') as img:
            img.write(urlopen(url[i]).read())
    main()
else:
    main()
    













