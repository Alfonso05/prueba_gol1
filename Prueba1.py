from tkinter import*
##import vlc


##p = vlc.MediaPlayer("gol.mp3")
tk= Tk()

canvas =Canvas(tk,width=1000,heigh=700)
tk.title("ALFONSO HEREDIA")
canvas.pack()

imagen2=PhotoImage(file="arco1.gif")
canvas.create_image(600,0,anchor=NW,image=imagen2)

imagen3=PhotoImage(file="balon1.gif")
canvas.create_image(0,100,anchor=NW,image=imagen3)



def moverbalon (event):
    if event.keysym=='Right':
        canvas.move(2,3,0)
        

    elif event.keysym=='Left':
        canvas.move(2,-3,0)

canvas.bind_all('<KeyPress-Right>',moverbalon)
canvas.bind_all('<KeyPress-Left>',moverbalon)
imagen3.get(10,30)


tk = Label(tk, text="Press and Drag the mouse to draw")
tk.pack(side=BOTTOM)

tk.mainloop()