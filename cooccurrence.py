from nltk.metrics.scores import precision, recall, f_measure
from operator import is_not
from collections import Counter
from functools import partial
import collections
import json
from itertools import combinations
from nltk.tokenize import word_tokenize
import nltk

def cooccurrence_classifier(video_dict, video_id):
    comments = ' '.join([comment[0] for comment in video_dict[video_id]])
    bow = get_bag(comments, 20)
    feature = features(video_dict[video_id], bow)
    feature_combo = [(dict(combo[0][0], **(combo[1][0])), (1 if combo[0][1] > combo[1][1] else 0)) for combo in list(combinations(feature, 2)) if combo[0][1] != combo[1][1]]
    classifier = nltk.NaiveBayesClassifier.train(feature_combo)
    print(nltk.classify.accuracy(classifier, feature_combo))
    return classifier

def cooccurrence_test(classifier, c1, c2):
    c1_feature = {word : (1 if word in c1.split(' ') else 0) for word in bow}
    c2_feature = {word : (1 if word in c1.split(' ') else 0) for word in bow}
    return classifier.classify(c1_feature.update(c2_feature))

def window(x, indices, window_size):
    '''pick the window according to window size'''
    windows = [context[index - window_size:index] + context[index + 1:index + window_size + 1]
            for context, index in zip(x, indices)]
    return windows

def get_bag(x, threshold):
    '''get the bag of words'''
    bag_of_words = Counter(word_tokenize(x))
    print("Bag = {}".format(bag_of_words))
    bag_of_words = [key for key in bag_of_words if bag_of_words[key] >= threshold]
    return bag_of_words

def features(x, bag):
    ## co-occurence
    cooccurrence_word = [({word : (1 if word in comment[0].split(' ') else 0) for word in bag}, comment[1]) for comment in x]
    return cooccurrence_word

def scores(classifier, test, ids):
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    for i, (feats, label) in enumerate(test):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)

    accuracy = nltk.classify.accuracy(classifier, test)
    print("accuracy: " + str(accuracy))
    p = filter(partial(is_not, None), [precision(refsets[sense], testsets[sense]) for sense in ids])
    p = sum(p) / len(p)
    print("precision: " + str(p))
    r = filter(partial(is_not, None), [recall(refsets[sense], testsets[sense]) for sense in ids])
    r = sum(r) / len(r)
    print("recall: " + str(r) )
    f_1 = filter(partial(is_not, None), [f_measure(refsets[sense], testsets[sense]) for sense in ids])
    f_1 = sum(f_1) / len(f_1)
    print("f-1 score: " + str(f_1))

    return({"precision":p, "recall":r, "f_1":f_1, "accuracy":accuracy})

#choose('cLdxuaxaQwc', "It's okay Pewds, you still my nigga <3", "dwdw")
