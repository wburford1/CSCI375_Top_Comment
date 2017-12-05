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

def readvideos(name):
    columns = ['video_id', 'title', 'channel_title', 'category_id',
              'tags', 'views', 'likes', 'dislikes', 'comment_total',
              'thumbnail_link', 'date']
    us_vid_df = pd.read_csv('youtube/USvideos.csv',usecols = columns, encoding = 'utf8', error_bad_lines = False)
    video_dict = {}
    category_id = {}
    tags_id = {}
    taglist = []

    ##need to find the unique values
    for i in range(len(us_vid_df['title'])):
        if str(us_vid_df['title'][i]) in video_dict and str(us_vid_df['video_id'][i]) not in video_dict.values():
            video_dict[str(us_vid_df['title'][i])].append(str(us_vid_df['video_id'][i]))
        else: 
            video_dict[str(us_vid_df['title'][i])] = [str(us_vid_df['video_id'][i])]
        if str(us_vid_df['category_id'][i]) in category_id and str(us_vid_df['video_id'][i]) not in category_id.values():
            category_id[str(us_vid_df['category_id'][i])].append(str(us_vid_df['video_id'][i]))
        else:
            category_id[str(us_vid_df['category_id'][i])] = [str(us_vid_df['video_id'][i])]
        taglist.append((us_vid_df['tags'][i], us_vid_df['video_id'][i]))
    for e in taglist:
        for element in e[0].split('|'):
            if element in tags_id and str(e[1]):
                tags_id[str(element)].append(str(e[1]))
            else:
                tags_id[str(element)] = [str(e[1])]
    if name == 'title':
        return video_dict
    elif name == 'category':
        print (category_id)
        return category_id
    elif name == 'tags':
        return tags_id


if __name__ == '__main__':
    '''
    video_dict = readcomments()
    with open('video_dict.json', 'w') as f:
        json.dump(video_dict, f)
    '''    
    videoinfo_dict = readvideos('title')
    category_dict = readvideos('category')
    tags_dict = readvideos('tags')
    with open('title_dict.json', 'w', encoding='UTF-8') as f:
        json.dump(videoinfo_dict, f, cls=MyEncoder)
    with open('category_dict.json', 'w',encoding='UTF-8') as f:
        json.dump(category_dict, f, cls=MyEncoder)
    with open('tags_dict.json', 'w',encoding='UTF-8') as f:
        json.dump(tags_dict, f, cls=MyEncoder)

