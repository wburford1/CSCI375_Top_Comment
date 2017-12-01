#Generic imports
import numpy as np
import pandas as pd
import json

#Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
from pprint import pprint
'''
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
#Statistical imports
import statsmodels.api as sm
from sklearn.preprocessing import MultiLabelBinarizer
'''
columns = ['video_id', 'title', 'channel_title', 'category_id',
          'tags', 'views', 'likes', 'dislikes', 'comment_total',
          'thumbnail_link', 'date']



us_vid_df = pd.read_csv('/Users/refstudent/Downloads/CSCI375_Top_Comment-master/youtube/USvideos.csv',usecols = columns)
UScomments = pd.read_csv('/Users/refstudent/Downloads/CSCI375_Top_Comment-master/youtube/UScomments.csv',encoding='utf8', error_bad_lines = False) 
'''
with open('../input/US_category_id.json') as file:    
    US_category_id = json.load(file)
'''
us_vid_df.loc[us_vid_df['date'] == '24.09xcaeyJTx4Co', 'date'] = '24.09'
us_vid_df.loc[us_vid_df['date'] == '26.0903jeumSTSzc', 'date'] = '26.09'
us_vid_df.loc[us_vid_df['date'] == '100', 'date'] = '09.10'
us_vid_df['date'] = us_vid_df['date'].apply(lambda x: pd.to_datetime(str(x).replace('.','')+"2017",
                                                                     format='%d%m%Y'))
us_vid_df['date'] = us_vid_df['date'].dt.date

us_vid_df = us_vid_df.drop_duplicates()
#print('US video head:')
print(us_vid_df.head(10))
print(UScomments.head(10))
#print(us_vid_df['title'])
'''
#reading the data into list
Videoinformation = []

print(len(us_vid_df['title']))
print(len(us_vid_df['category_id']))
print(len(us_vid_df['tags']))
print(us_vid_df['title'][5298])
for i in range(len(us_vid_df['title'])):
	print(us_vid_df['title'][i])
	#Videoinformation.append(us_vid_df['video_id'][i])
		#, us_vid_df['title'][i])
#		, us_vid_df['channel_title'][i], us_vid_df['category_id'][i], us_vid_df['tags'][i], us_vid_df['views'][i], us_vid_df['likes'][i], us_vid_df['dislikes'][i], us_vid_df['comment_total'][i]))

print(Videoinformation)
'''