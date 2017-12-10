from tkinter import *
from sentiment_classifier import compare_sent

class classifier:

    def __init__(self, master):


        ## First frame contains the intro and the textboxes 
        frame_id = Frame(master)
        frame_id.pack()         

        lab = Label(frame_id, text = "Which comment would get more likes?")
        lab.pack()

        lab_id = Label(frame_id, text = "Input your video ID")
        lab_id.pack(side = LEFT)

        e_id = Entry(frame_id)
        e_id.insert(END, '3WEvgqcP8mg')
        e_id.pack(side = LEFT)

        frame = Frame(master)
        frame.pack()
        
        label = Label(frame, text = "Input your comments")
        label.pack()
        
        ## Entry allows the backend to receive user input
        e1 = Entry(frame)
        e1.pack(side = LEFT)

        e2 = Entry(frame)
        e2.pack(side = LEFT)
        
        ## Message displays which comment is better
        message = StringVar()
        Label(master, textvariable = message).pack()

        def compare():
            ## do things here
            choice = compare_sent(e_id.get(), e1.get(), e2.get())
            string = "Based on our SCIENTIFIC CALCULATION: " + str(choice) + " is better"
            message.set(string)
        
        ## This frame contains all the buttons
        frame_buttons = Frame(master)
        frame_buttons.pack()

        quit_button = Button(
            frame_buttons, text = "QUIT", fg = "red", command = frame_buttons.quit
            )
        quit_button.pack(side = LEFT)

        compare_button = Button(frame_buttons, text = "Compare", command = compare)
        compare_button.pack(side=LEFT)

class generator:

    def __init__(self, master):
        
        ## This frame contains title
        frame_title = Frame(master)
        frame_title.pack()

        title = Label(frame_title, text = "Title: ")
        title.pack(side = LEFT)

        e1 = Entry(frame_title)
        e1.pack(side = LEFT)

        ## This frame contains tags
        frame_tags = Frame(master)
        frame_tags.pack()
        
        tags = Label(frame_tags, text = "Tags: ")
        tags.pack(side = LEFT)

        e2 = Entry(frame_tags)
        e2.pack(side = LEFT)

        ## This frame contains category        
        frame_category = Frame(master)
        frame_category.pack()
      
        category = Label(frame_category, text = "Category: ")
        category.pack(side = LEFT)

        e3 = Entry(frame_category)
        e3.pack(side = LEFT)
        
        ## Message allows us to return the generated message
        message = StringVar()
        Label(master, textvariable = message).pack()

        def generate():
            ## do things here
            ## Use e1.get, e2.get to get user input
            ## Use set to set output
            message.set(e1.get())

        ## This frame contains the buttons
        frame_buttons = Frame(master)
        frame_buttons.pack()

        quit_button = Button(
            frame_buttons, text = "QUIT", fg = "red", command = frame_buttons.quit
            )
        quit_button.pack(side = LEFT)

        generate_button = Button(frame_buttons, text = "Generate", command = generate)
        generate_button.pack(side = LEFT)

if __name__ == '__main__':
    
    root = Tk()
    app = classifier(root)
    root.mainloop()
    root.destroy()

    root = Tk()
    app = generator(root)
    root.mainloop()
    root.destroy()
