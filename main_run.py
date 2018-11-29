import math
import json
import time
import pandas as pd
import numpy as np
start_time = time.time()
import RecommendationModels as rm
import evaluation as eval
import result
train_data=pd.read_csv('train_data.csv',usecols=['user_id','song_id','title','listen_count'])
test_data=pd.read_csv('test_data.csv',usecols=['user_id','song_id','title','listen_count'])

user_to_song = {}
song_to_user={}
user_to_song_test={}
file1=open("train_data.csv",'r+')
file2=open("test_data.csv",'r+')
data1=file1.readlines()[1:]
data2=file2.readlines()[1:]

for x in data1:
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

for x in data2:
	row=x.split(',')
	user=row[1]
	song=row[2]
	try:
		user_to_song_test[user].append(song)
	except:
		temp=[]
		temp.append(song)
		user_to_song_test[user]=temp

users=list(train_data['user_id'].unique())
songs=list(train_data['song_id'].unique())

# Poplarity Based:
pm=rm.Popularity_Based_Model(train_data)
print("\n####### Poplarity Based #######")
# recommend = (list(pm.recommend(users[0])['song_id']))
# print recommend

res=eval.Precision(test_data,train_data,pm,user_to_song_test)
a,b=res.calculate(.1)
print a
print b

# # # User Based:
# um=rm.User_Based_Model(users,user_to_song,songs,True,10)
# print um.recommend(users[0])




# ## Item Based:
# im=rm.Item_Based_Model(user_to_song,song_to_user,songs,1000)
# print("\n####### Item Based #######")
# recommend =im.recommend(users[0])


# ## User based Filtered Item Based:
# um=rm.User_Based_Model(users,user_to_song,songs,True,500)
# song_list=um.recommend(users[0])
# a,weight=zip(*song_list)
# im=rm.Item_Based_Model(user_to_song,song_to_user,a,200)
# print("\n####### User based Filtered Item Based #######")
# recommend= im.recommend(users[0])

## Item Based Filtered User Based
# im=rm.Item_Based_Model(user_to_song,song_to_user,songs,50)
# song_list=im.recommend(users[0])
# a,weight=zip(*song_list)
# um=rm.User_Based_Model(users,user_to_song,a,False,10)
# recommend=um.recommend(users[0])
# print("\n####### User based Filtered Item Based #######")
# print recommend

print("--- %s seconds" % (time.time() - start_time))
