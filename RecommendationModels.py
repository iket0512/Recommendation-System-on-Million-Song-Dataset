import math
import json
import time

class Popularity_Based_Model:
    def __init__(self, train_data):
        self.train_data=train_data

    def recommend(self):
        # self.user_id=user
        # test_data_user = self.train_data[self.train_data['user_id'] == self.user_id]
        # print test_data_user
        # return  test_data_user
        song_grouped = self.train_data.groupby(['song_id']).agg({'listen_count': 'count'}).reset_index()
        return song_grouped.sort_values(['listen_count', 'song_id'], ascending = [0,1])[:10]

class User_Based_Model:
    def __init__(self,users,user_to_song,songs,output):
        self.songs_weight=dict()
        self.output=output
        self.user_to_song=user_to_song
        self.users=users
        self.songs=songs

    def similarity_users(self,v):
        list2=set(self.user_to_song[v])
        common=[]
        common=self.user_song_list.intersection(list2)
        if len(common)==0:
            return
        diff=list2-common
        for item in diff:
            sm=len(common)/(math.sqrt(len(self.user_song_list))*math.sqrt(len(list2)))
            if (item in self.songs_weight):
                self.songs_weight[item]+=sm
            else:
                self.songs_weight[item]=sm

    def recommend(self,user):
        # start_time = time.time()
        temp=self.users
        temp.remove(user)
        self.user_song_list =set(self.user_to_song[user])
        for v in temp:
            self.similarity_users(v)
        sorted_songs=sorted(self.songs_weight.items(),key=lambda x : x[1],reverse=True)[:self.output] 
        # print("--- %s seconds" % (time.time() - start_time))
        return sorted_songs

class Item_Based_Model:
    def __init__(self,user_to_song,song_to_user,songs,output ):
        self.song_to_user=song_to_user
        self.user_to_song=user_to_song
        self.songs=songs
        self.output=output

    def similarity_song(self,song1,song2):
        list1=self.song_to_user[song1]
        list2=self.song_to_user[song2]
        common=len(set(list1).intersection(list2))
        sm1=common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
        return sm1

    def recommend(self,user):
        # start_time = time.time()
        weights=[]
        user_song_list=set(self.user_to_song[user])
        temp=set(self.songs)-user_song_list
        for song_cand in temp:
            sm=0
            for song in user_song_list:
                x=self.similarity_song(song_cand,song)
                sm=sm+x
            weights.append(sm)
        result= list(zip(list(temp),weights))
        result= sorted(result,key=lambda x: x[1],reverse=True)[:self.output] 
        # print("--- %s seconds " % (time.time() - start_time) )
        return result