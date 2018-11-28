import math
import json
import time
import pandas as pd
import numpy as np
start_time = time.time()
import RecommendationModels as rm
import result
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
# print("\n####### Poplarity Based #######")
# recommend = (list(pm.recommend()['song_id']))


# ## User Based:
# um=rm.User_Based_Model(users[0],users,user_to_song,songs,True,500)
# print("\n####### User Based #######")
# recommend=um.recommend()


# ## Item Based:
# im=rm.Item_Based_Model(users[0],user_to_song,song_to_user,songs,1000)
# print("\n####### Item Based #######")
# recommend =im.recommend()


# ## User based Filtered Item Based:
# um=rm.User_Based_Model(users[0],users,user_to_song,songs,True,500)
# song_list=um.recommend()
# a,weight=zip(*song_list)
# im=rm.Item_Based_Model(users[0],user_to_song,song_to_user,a,200)
# print("\n####### User based Filtered Item Based #######")
# recommend= im.recommend()

# print("--- %s seconds" % (time.time() - start_time))

# ## Item Based Filtered User Based
im=rm.Item_Based_Model(users[0],user_to_song,song_to_user,songs,1000)
song_list=im.recommend()
a,weight=zip(*song_list)
um=rm.User_Based_Model(users[0],users,user_to_song,a,False,500)
print("\n####### User based Filtered Item Based #######")
recommend = um.recommend()

test_data=pd.read_csv('test_data.csv',usecols=['user_id','song_id','title','listen_count'])

user_to_song_test = {}
song_to_user_test={}
file2=open("test_data.csv",'r+')
data=file2.readlines()[1:]
for x in data:
	row=x.split(',')
	user=row[1]
	song=row[2]
	try:
		user_to_song_test[user].append(song)
	except:
		temp=[]
		temp.append(song)
		user_to_song_test[user]=temp
	try:
		song_to_user_test[song].append(user)
	except:
		temp=[]
		temp.append(user)
		song_to_user_test[song]=temp

users_test=list(test_data['user_id'].unique())
songs_test=list(test_data['song_id'].unique())


testing = user_to_song_test[users[0]]

recommend,x=zip(*recommend)
# print(recommend)
# print(testing)
res=result.Result(recommend,testing)

print( "precision = " , res.precision())
print( "recall = " , res.recall())
