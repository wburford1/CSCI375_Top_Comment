import json
import sys
from jsonTest import process_text
from LM import preprocess, generate_sent


with open('category_dict.json') as json_data:
    category_dict = json.load(json_data)

with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

def category_generator(name):
    category_corpus = []
    for i in range(len(category_dict[name])):
       	video = category_dict[name][i]
        try:
            category_corpus.append(video_dict[video[0]])
        except KeyError:
            print("no Comment")
    return category_corpus

def corpus_processing(category_corpus):
    corpus =[]
    for e in category_corpus:
        for a in e:
            corpus.append(a[0])
    return corpus

def corpus_generation(name):
    corpus = corpus_processing(category_generator(name))
    with open('category_corpus.txt', 'w') as f:
        for e in corpus:
            f.write(str(e) +'\n')

<<<<<<< HEAD
corpus_generation('24')
=======
if __name__ == '__main__':
    # requires a category name to be passed in as the first command line arguement
    # ex. 'entertainment'
    category_name = sys.argv[1]
    corpus_generation(process_text(category_name))
    corpus = preprocess()
    final_text = [generate_sent(5, corpus)for i in range(100)]
    with open('comment_generated.json', 'w') as f:
        json.dump(final_text, f)
>>>>>>> 7fccb3acdeefa2991f40cedcf0c0f75b39ed2e33
