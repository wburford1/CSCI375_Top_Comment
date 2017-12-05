import json
import numpy as np
from collections import namedtuple
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
#from nltk import pos_tag

with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

#SentSentiment = namedtuple('SentSentiment', 'sentence, score')

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
            list.append(ss['compound'])
        sent_dict[k] = np.mean(list)
    return sent_dict

def compare_sent(video_id, dict, sent1, sent2):
    sent_score = dict[video_id]
    sid = SentimentIntensityAnalyzer()
    ss1 = abs(sid.polarity_scores(sent1)['compound'] - sent_score)
    ss2 = abs(sid.polarity_scores(sent2)['compound'] - sent_score)
    if ss1 < ss2: return 1
    else: return 2

print(compare_sent('3WEvgqcP8mg', sent_sentiment(video_dict), 'this is terrible', 'this is great sentence'))

#sentence = "Iphone6 camera is awesome for low light "
#tagged = pos_tag(word_tokenize(sentence))
#print(tagged)
