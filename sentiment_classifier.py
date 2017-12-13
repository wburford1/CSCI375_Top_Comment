import json
import numpy as np
from collections import namedtuple
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
from text.classifiers import NaiveBayesClassifier

with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

#FeatureVector = namedtuple('FeatureVector', 'sent_difference, which_comment')

def not_int(s):
    try: 
        int(s)
        return False
    except ValueError:
        return True

def SentimentClassifier(sent):
#    sent_dict = {}
    sid = SentimentIntensityAnalyzer()
#    for k in dict.keys():
#        for i in dict[k]: 
#            if not_int(i[1]): i[1] = 0
#        top = sorted(dict[k], key = lambda x: int(x[1]), reverse = True)
    dict = {}
    for s in sent:
        ss1 = sid.polarity_scores(s[0])['compound']
        ss2 = sid.polarity_scores(s[1])['compound']
        likes = s[2]
        difference = abs(ss1 - ss2)
        dict[difference] = likes
    classifier = nltk.NaiveBayesClassifier.train(dict)
    classifier.show_most_informative_features()
    return classifier

def test(classifier, sent1, sent2):
    sid = SentimentIntensityAnalyzer()
    ss1 = abs(sid.polarity_scores(sent1)['compound']
    ss2 = abs(sid.polarity_scores(sent2)['compound']
    return classifier.classify(abs(ss1-ss2))

#print(compare_sent('3WEvgqcP8mg', 'this is terrible', 'this is great sentence'))


