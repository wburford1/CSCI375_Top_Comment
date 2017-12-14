import json

with open('category_dict.json') as json_data:
    category_dict = json.load(json_data)


with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

def category_generator(name):
    category_corpus = []
    for i in range(len(category_dict)):  
       	video = category_dict[name][i][0]
        try:
            category_corpus.append(video_dict[video])
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


