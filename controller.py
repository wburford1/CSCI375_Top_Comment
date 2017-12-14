# this controls all classifiers by feeding each of them data.
# It then aggregates each classifier's vote to decide which video will recieve the most likes.
import json
from collections import namedtuple
from sentiment_classifier import sent_classifier, sent_test
from cooccurrence import cooccurrence_classifier, cooccurrence_test
from itertools import combinations
import time


comment = namedtuple('comment', 'content, likes')
video = namedtuple('video', 'id, title, like_count, cat_id')

def ensemble(training_video_dict, testing_video_dict, video_id):
    classifier_sent = sent_classifier(training_video_dict, video_id)
    classifier_cooccur = cooccurrence_classifier(training_video_dict, video_id)

    # print(training_video_dict[video_id][0])
    test_pre = testing_video_dict[video_id]
    # print(test_pre)
    test_set = [(combo[0].content, combo[1].content, 0 if combo[0].likes > combo[1].likes else 1) for combo in list(combinations(test_pre, 2)) if combo[0].likes != combo[1].likes]
    sent_classified = []
    cooccur_classified = []
    correct = []
    test_start = time.time()
    for pair in test_set:
        s = sent_test(classifier_sent, pair[0], pair[1])
        sent_classified.append(s)
        c = cooccurrence_test(training_video_dict, video_id, classifier_cooccur, pair[0], pair[1])
        cooccur_classified.append(c)
        correct.append(pair[2])
        # print('sent {}, cooc {}, correct {}'.format(s, c, pair[2]))
    test_end = time.time()

    f1s = []
    for guess in [sent_classified, cooccur_classified]:
        tp = sum([1 for i in range(0, len(correct), 1) if correct[i]==1 and guess[i]==1])
        tn = sum([1 for i in range(0, len(correct), 1) if correct[i]==0 and guess[i]==0])
        fp = sum([1 for i in range(0, len(correct), 1) if correct[i]==0 and guess[i]==1])
        fn = sum([1 for i in range(0, len(correct), 1) if correct[i]==1 and guess[i]==0])
        accuracy = (tp + tn)/float(tp + tn + fp + fn)
        prec_p = tp / float(tp + fp) if tp + tp != 0 else 0
        prec_n = tn / float(tn + fn) if tn + fn != 0 else 0
        rec_p = tp / float(tp + fn) if tp + fn != 0 else 0
        rec_n = tn / float(tn + fp) if tn + fp != 0 else 0
        f1_p = (2*prec_p*rec_p) / float(prec_p + rec_p) if prec_p + rec_p != 0 else 0
        f1_n = (2*prec_n*rec_n) / float(prec_n + rec_n) if prec_n + rec_n != 0 else 0
        f1s.append(f1_p)
    print('f1 for sent = {}, f1 for cooccur = {}'.format(f1s[0], f1s[1]))


    print("It took {}m to classify {} combinations.".format((test_end - test_start)/60.0, len(test_set)))
    print(sent_classified)
    print(cooccur_classified)


def parse_video_dict():
    with open('video_dict.json', 'r') as f:
        video_dict_raw = json.load(f)
        video_dict = {}
        for key in video_dict_raw:
            # if key in ['TPnuT2TLvLQ', '_qb4_uvYSG0', 'YYwB63YslbA', 'CiHV9oFXFzY', 'j-JOG2mUt0c']:
            video_dict[key] = []
            for com_thing in video_dict_raw[key]:
                try:
                    int(com_thing[1])
                    video_dict[key].append(comment(str(com_thing[0]), int(com_thing[1])))
                except ValueError:
                    1 + 1
    return video_dict

def parse_category_dict():
    with open('category_dict.json', 'r') as f:
        category_dict_raw = json.load(f)
        category_dict = {}
        for cat_id in category_dict_raw:
            for v in category_dict_raw[cat_id]:
                vid_id = v[0]
                category_dict[vid_id] = video(vid_id, v[1], v[2], cat_id)
    return category_dict

def split_video_dict(dic):
    train = {}
    test = {}
    for vid in dic:
        coms = dic[vid]
        train[vid] = coms[:int(.7*len(coms))]
        test[vid] = coms[int(.7*len(coms)):]
    return (train, test)

if __name__ == '__main__':
    video_dict = parse_video_dict()
    splits = split_video_dict(video_dict)
    train_set = splits[0]
    test_set = splits[1]
    # test_set = ("It's okay Pewds, you still my nigga <3", "dwdw", 0)
    #meta_data_dict = parse_category_dict()
    ensemble(train_set, test_set, 'cLdxuaxaQwc')
