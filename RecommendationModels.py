import math
import json
import time
from operator import itemgetter

class Popularity_Based_Model:
    train_data=None
    def __init__(self, train_data):
        self.train_data=train_data

    def recommend(self):
        song_grouped = self.train_data.groupby(['title']).agg({'listen_count': 'count'}).reset_index()
        grouped_sum = song_grouped['listen_count'].sum()
        return song_grouped.sort_values(['listen_count', 'title'], ascending = [0,1])[:10]

class User_Based_Model:
    user=None
    user_to_song={}
    output=10
    users=None
    user_song_list=None
    train_data=None
    def __init__(self,user,users,user_to_song,output):
        self.songs_weight=dict()
        self.user=user
        self.output=output
        self.user_to_song=user_to_song
        self.user_song_list = user_to_song[user]
        self.users=users

    def similarity_users(self,v):
        list2=self.user_to_song[v]
        common=0
        diff=[]
        for item in list2:
            if item in self.user_song_list:
                common=common+1
            else:
                diff.append(item)
            sm=common/(math.sqrt(len(self.user_song_list))*math.sqrt(len(list2)))
        for item in diff:
            if item in self.songs_weight:
                self.songs_weight[item]+=sm
            else:
                self.songs_weight[item]=sm

    def recommend(self):
        for v in self.users:
            if v==self.user:
                continue
            self.similarity_users(v)
        sorted_songs=sorted(self.songs_weight.items(),key=lambda x : x[1],reverse=True)[:output] 
        return sorted_songs

class Item_Based_Model:
    user=None
    users=None
    songs=None
    user_to_song={}
    song_to_user={}
    user_song_list=None
    def __init__(self, user,user_to_song,song_to_user,songs ):
        self.user=user
        self.user_to_song=user_to_song
        self.song_to_user=song_to_user
        self.user_song_list = user_to_song[user]
        self.songs=songs

    def similarity_song(self,song1,song2):
        list1=self.song_to_user[song1]
        list2=self.song_to_user[song2]
        common=len(set(list1).intersection(list2))
        sm1=common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
        return sm1

    def recommend(self):
        weights=[]
        for song_cand in self.songs:
            if song_cand in self.user_song_list:
                weights.append(0)
                continue;
            sm=0    
            for song in self.user_song_list:
                x=self.similarity_song(song_cand,song)
                sm=sm+x
            weights.append(sm)
        result= list(zip(self.songs,weights))
        result= sorted(result,key=lambda x: x[1],reverse=True)
        return result