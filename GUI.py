from tkinter import *
import json
from collections import namedtuple
from cooccurrence import cooccurrence_classifier
from sentiment_classifier import sent_classifier
from LM import preprocess, generate_sent
from Generator import corpus_generation
from jsonTest import process_text
from controller import combine_classifiers

comment = namedtuple('comment', 'content, likes')

#tkinter doesn't have certain emojis, so when it does comments it might skip some of the emojis
class classifier:
    
    prev_id = ''
    cooccur = None
    sent = None

    def __init__(self, master, video_dict):

        ## First frame contains the intro and the textboxes 
        frame_id = Frame(master)
        frame_id.pack()         

        lab = Label(frame_id, text = "Which comment would get more likes?")
        lab.pack()

        lab_id = Label(frame_id, text = "Input your video ID")
        lab_id.pack(side = LEFT)

        e_id = Entry(frame_id)
        e_id.insert(END, 'cLdxuaxaQwc')
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
            if e_id.get() != self.prev_id:
                self.sent = sent_classifier(video_dict, e_id.get())
                self.cooccur = cooccurrence_classifier(video_dict, e_id.get())
                self.prev_id = e_id.get()
                print(e_id.get())
                
            choice = combine_classifiers(e1.get(), e2.get(), self.sent, self.cooccur, video_dict, e_id.get())
            #choice = cooccurrence_test(video_dict, e_id.get(), self.cooccur, e1.get(), e2.get())            
            string = "Based on our SCIENTIFIC CALCULATION " + str(choice) + " is better"
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
            category = e3.get()
            corpus_generation(process_text(category))
            corpus = preprocess()
            final_text = [generate_sent(5, corpus)for i in range(100)]
            with open('comment_generated.json', 'w') as f:
                json.dump(final_text, f)
            text = ""
            for e in final_text:
                text += str(e)+ '\n'
            message.set(text) 

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
    
    with open('video_dict.json') as video:
        video_dict_raw = json.load(video)
    video_dict = {}
    for key in video_dict_raw:
            # if key in ['TPnuT2TLvLQ', '_qb4_uvYSG0', 'YYwB63YslbA', 'CiHV9oFXFzY', 'j-JOG2mUt0c']:
            video_dict[key] = []
            for com_thing in video_dict_raw[key]:
                try:
                    int(com_thing[1])
                    video_dict[key].append(comment(str(com_thing[0]), int(com_thing[1])))
                except ValueError:
                    1+1
                    
    root = Tk()  
    input_raw = input("classify or generate: ")
    print('aabb')
    if str(input_raw) == 'generate':
        app = generator()
    elif str(input_raw) == 'classify':
        app = classifier(root, video_dict) 
    else:
        while str(input_raw) != 'generate' and str(input_raw) != 'classify':
            input_raw = input("classify or generate: ")
            if str(input_raw) == 'generate':
                app = generator()
            elif str(input_raw) == 'classify':
                app = classifier(root, video_dict)  
    root.mainloop()
    root.destroy()
