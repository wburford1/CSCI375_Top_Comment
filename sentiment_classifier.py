import json
import numpy as np
from collections import namedtuple
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
from text.classifiers import NaiveBayesClassifier

with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

def not_int(s):
    try: 
        int(s)
        return False
    except ValueError:
        return True

def SentimentClassifier(sent):
    sid = SentimentIntensityAnalyzer()
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

def test(sent1, sent2):
    classifier = SentimentClassifier(sent)
    sid = SentimentIntensityAnalyzer()
    ss1 = abs(sid.polarity_scores(sent1)['compound']
    ss2 = abs(sid.polarity_scores(sent2)['compound']
    return classifier.classify(abs(ss1-ss2))



