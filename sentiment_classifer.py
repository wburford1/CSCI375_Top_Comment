import json
from collections import namedtuple
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
#from nltk import pos_tag

with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

SentSentiment = namedtuple('SentSentiment', 'sentence, score')
WordSentiment = namedtuple('WordSentiment', 'word, score')

def not_int(s):
    try: 
        int(s)
        return False
    except ValueError:
        return True

def sent_sentiment(dict):
    sent_dict = {}
    sid = SentimentIntensityAnalyzer()
    for k in dict.keys():
        for i in dict[k]: 
            if not_int(i[1]): i[1] = 0
        top = sorted(dict[k], key = lambda x: int(x[1]), reverse = True)[:10]
        list = []
        for i in top:
            ss = sid.polarity_scores(i[0])
            # ss is a dictionary of compound, pos, neu, and neg sentence sentiment scores
            list.append(SentSentiment(i, ss['compound']))
        sent_dict[k] = list
    return sent_dict

print(sent_sentiment(video_dict))


#sentence = "Iphone6 camera is awesome for low light "
#tagged = pos_tag(word_tokenize(sentence))
#print(tagged)
