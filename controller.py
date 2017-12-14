# this controls all classifiers by feeding each of them data.
# It then aggregates each classifier's vote to decide which video will recieve the most likes.
import json
from collections import namedtuple
from sentiment_classifier import sent_classifier, sent_test
from cooccurrence import cooccurrence_classifier, cooccurrence_test


comment = namedtuple('comment', 'content, likes')

def ensemble(video_dict, video_id, c1, c2):
    classifier_sent = sent_classifier(video_dict, video_id)
    sent_classified = sent_test(classifier_sent, c1, c2)
    classifier_cooccur = cooccurrence_classifier(video_dict, video_id)
    cooccur_classified = cooccurrence_test(classifier_cooccur, c1, c2)
    print(sent_classified)
    print(cooccur_classified)


if __name__ == '__main__':
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
    ensemble(video_dict, 'cLdxuaxaQwc', "It's okay Pewds, you still my nigga <3", "dwdw")
    

