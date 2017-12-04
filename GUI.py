from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        
        label = Label(frame, text = "Which comment is better?")
        label.pack()

        e1 = Entry(frame)
        e1.pack(side = LEFT)

        e2 = Entry(frame)
        e2.pack(side = LEFT)

        def compare():
        ## do things here
            print(e1.get())
            print(e2.get())
            print "The first one is better"


        frame_buttons = Frame(master)
        frame_buttons.pack()

        quit_button = Button(
            frame_buttons, text = "QUIT", fg = "red", command = frame_buttons.quit
            )
        quit_button.pack(side = LEFT)

        compare_button = Button(frame_buttons, text = "Compare", command = compare)
        compare_button.pack(side=LEFT)


root = Tk()

app = App(root)

root.mainloop()
root.destroy()
