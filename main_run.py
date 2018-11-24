import math
import json
import time
import pandas as pd
import numpy as np
start_time = time.time()
import RecommendationModels as rm

train_data=pd.read_csv('train_data.csv',usecols=['user_id','song_id','title','listen_count'])
users=list(train_data['user_id'].unique())
songs=list(train_data['song_id'].unique())

user_to_song = {}
song_to_user={}
file1=open("train_data.csv",'r+')
data=file1.readlines()[1:]
for x in data:
	row=x.split(',')
	user=row[1]
	song=row[2]
	try:
		user_to_song[user].append(song)
	except:
		temp=[]
		temp.append(song)
		user_to_song[user]=temp
	try:
		song_to_user[song].append(user)
	except:
		temp=[]
		temp.append(user)
		song_to_user[song]=temp

users=list(train_data['user_id'].unique())
songs=list(train_data['song_id'].unique())

# # Poplarity Based:
# pm=rm.Popularity_Based_Model(train_data)
# print list(pm.recommend()['title'])

# # User Based:
# um=rm.User_Based_Model(users[0],users,user_to_song,10)
# print um.recommend()

# # Item Based:
# im=rm.Item_Based_Model(users[0],user_to_song,song_to_user,songs[1:50])
# print im.recommend()

# # User based Filtered Item Based:
# um=rm.User_Based_Model(users[0],users,user_to_song,50)
# song_list=um.recommend()
# a,weight=zip(*song_list)
# im=rm.Item_Based_Model(users[0],user_to_song,song_to_user,a)
# print im.recommend()

print("--- %s seconds" % (time.time() - start_time))

