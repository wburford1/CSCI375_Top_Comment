import numpy as np
import pandas as pd
import json
from collections import namedtuple

comment = namedtuple('comment', 'content, likes')

def read(): 

    columns = ['video_id','views']

    us_vid_df = pd.read_csv('youtube/USvideos.csv', usecols = columns)
    UScomments = pd.read_csv('youtube/UScomments.csv', encoding = 'utf8', error_bad_lines = False) 

    del(UScomments['replies'])

    video_dict = {}
    for index, row in UScomments.iterrows():
        video_dict.setdefault(row['video_id'], []).append(comment(row['comment_text'], row['likes']))
    
    return (video_dict)

if __name__ == '__main__':

    video_dict = read()
    with open('video_dict.json', 'w') as f:
        json.dump(video_dict, f)
