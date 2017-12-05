import numpy as np
import pandas as pd
import json
from collections import namedtuple

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


comment = namedtuple('comment', 'content, likes')
#videoinfo = namedtuple('title', 'channel_title', 'category_id', 'tags', 'views', 'likes', 'dislikes', 'comment_total')

def readcomments(): 

    UScomments = pd.read_csv('youtube/UScomments.csv', encoding = 'utf8', error_bad_lines = False) 

    del(UScomments['replies'])

    video_dict = {}
    for index, row in UScomments.iterrows():
        video_dict.setdefault(row['video_id'], []).append(comment(row['comment_text'], row['likes']))
    
    return (video_dict)

def readvideos():
    columns = ['video_id', 'title', 'channel_title', 'category_id',
              'tags', 'views', 'likes', 'dislikes', 'comment_total',
              'thumbnail_link', 'date']
    us_vid_df = pd.read_csv('youtube/USvideos.csv',usecols = columns, encoding = 'utf8', error_bad_lines = False)
    video_dict = {}
    for i in range(len(us_vid_df['video_id'])):
        if us_vid_df['video_id'][i] in video_dict:
            video_dict[us_vid_df['video_id'][i]].append((us_vid_df['title'][i], us_vid_df['channel_title'][i],us_vid_df['category_id'][i],us_vid_df['tags'][i],us_vid_df['views'][i],us_vid_df['likes'][i],us_vid_df['dislikes'][i],us_vid_df['comment_total'][i]))
        else:
            video_dict[us_vid_df['video_id'][i]]= [(us_vid_df['title'][i], us_vid_df['channel_title'][i],us_vid_df['category_id'][i],us_vid_df['tags'][i],us_vid_df['views'][i],us_vid_df['likes'][i],us_vid_df['dislikes'][i],us_vid_df['comment_total'][i])]
    return (video_dict)


if __name__ == '__main__':

    video_dict = readcomments()
    with open('video_dict.json', 'w') as f:
        json.dump(video_dict, f)
    
    videoinfo_dict = readvideos()
    with open('videoinfo_dict.json', 'w',encoding='UTF-8') as f:
        json.dump(videoinfo_dict, f, cls=MyEncoder)
    
