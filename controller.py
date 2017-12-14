# this controls all classifiers by feeding each of them data.
# It then aggregates each classifier's vote to decide which video will recieve the most likes.
import json
from collections import namedtuple
from cooccurrenceclassifier import CooccurrenceClassifier
from sentiment_classifier import SentimentClassifier


comment = namedtuple('comment', 'content, likes')
video = namedtuple('video', 'id, title, like_count')

def parse_videos_dict():
    with open('video_dict.json', 'r') as f:
        videos_dict_raw = json.load(f)
        videos_dict = {}
        for key in videos_dict_raw:
            # if key in ['TPnuT2TLvLQ', '_qb4_uvYSG0', 'YYwB63YslbA', 'CiHV9oFXFzY', 'j-JOG2mUt0c']:
            videos_dict[key] = []
            for com_thing in videos_dict_raw[key]:
                try:
                    int(com_thing[1])
                    videos_dict[key].append(comment(str(com_thing[0]), int(com_thing[1])))
                except ValueError:
                    1+1
        return videos_dict

def parse_category_dict():
    with open('category_dict.json', 'r') as f:
        category_dict_raw = json.load(f)
        category_dict = {}
        for video in category_dict_raw:
            vid_id = video[0]
            category_dict[vid_id] = video(vid_id, video[1], video[2])
        return category_dict


if __name__ == '__main__':
    videos_dict = parse_videos_dict()
    meta_data_dict = parse_category_dict()

    all_classifiers = [
        CooccurrenceClassifier(videos_dict)
    ]
    coms = [
        ('I really like this video.', "This was the worst video I've ever seen!")
    ]

    for comment_set in coms:
        print('Comment 1: "{}"\nComment 2: "{}"'.format(comment_set[0], comment_set[1]))
        results = []
        for classifier in all_classifiers:
            results.append(classifier.choose(comment_set[0], comment_set[1], 'YYwB63YslbA'))
        r_counter = 0
        for res in results:
            r_counter += 1
            print('Classifier {} chose {} with {} confidence.'.format(r_counter, res.choice+1, res.confidence))
