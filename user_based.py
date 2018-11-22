import math
import json
import time
from operator import itemgetter
start_time = time.time()
file1 = open('user_to_song.json', 'r')
file2 = open('song_to_user.json','r')
user_to_song=file1.read()
song_to_user=file2.read()
song_to_user=json.loads(song_to_user)
user_to_song=json.loads(user_to_song)
users=user_to_song.keys()
songs=song_to_user.keys()

# print song_to_user

class Recommendation:
    songs_weight=dict()
    def __init__(self):
        self.songs_weight=dict()

    def similarity_users(self,u,v):
        list1=user_to_song[u]
        list2=user_to_song[v]
        common=0
        diff=[]
        for item in list2:
            if item in list1:
                common=common+1
            else:
                diff.append(item)
        sm=common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
        for item in diff:
            if item in self.songs_weight:
                self.songs_weight[item]+=sm
            else:
                self.songs_weight[item]=sm

    def user_based(self,type):
        for u in user_to_song:
            self.songs_weight=dict()
            for v in user_to_song:
                if u==v:
                    continue
                self.similarity_users(u,v)
            if type==1:
                sorted_songs=sorted(self.songs_weight.items(),key=lambda x : x[1],reverse=True)[:10] 
                return sorted_songs
            elif type==2:
                sorted_songs=sorted(self.songs_weight.items(),key=lambda x : x[1],reverse=True)[:10]     
                return self.calc_wo_meta(u,sorted_songs,type)
            elif type==3:
                return self.calc_wo_meta(u,self.songs_weight.items(),type)    
            

    def similarity_song(self,song1,song2):
        list1=song_to_user[song1]
        list2=song_to_user[song2]
        common=0
        for x in list1:
            if x in list2:
                common=common+1
        sm1=common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
        return sm1

    def calc_wo_meta(self,u,sorted_songs,type):
        user_songs=user_to_song[u]
        weights=[]
        for song_cand in sorted_songs:
            sm=0
            if type < 4:
                song_cand=song_cand[0]
            if song_cand in user_songs:
                weights.append(0)
                continue;    
            for song in user_songs:
                x=self.similarity_song(song_cand,song)
                sm=sm+x
            weights.append(sm)
        result= list(zip(sorted_songs,weights))
        result= sorted(result,key=lambda x: x[1],reverse=True)
        return result
        # print sorted_songs
        # return sorted_songs
        

    def main(self):
        print "main"
        
        # # Only user based recommendation list
        # song_list=r.user_based(1)
        # a,b=zip(*song_list)
        # print a
        # print song_list

        # # User based filtered item based recommendation list
        # song_list=r.user_based(2)
        # # result= sorted(song_list, key=lambda x: (x[1]+x[0][1]),reverse=True)[:10]
        # a,b=zip(*song_list)
        # a,b=zip(*a)
        # print a
        # print result

        # # complete userbased and item based recommendation list
        # takes a long time to execute!!! 25 secs approx
        # song_list=r.user_based(3)
        # print song_list

        # # Only item based recommendation list w/o metadata
        # takes a long time to execute!!! 25 secs approx
        # for user in users:
        # songlist=self.calc_wo_meta(users[0],songs,4)
        # print songlist

r=Recommendation()
r.main()


print("--- %s seconds" % (time.time() - start_time))