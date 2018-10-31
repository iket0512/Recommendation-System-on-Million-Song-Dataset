import math


# \\\Preprocessing data to convert it into two types:
# \\\ 1. user to song dict
# \\\ 2. song to user dict

f = open('eval_triplets.txt', 'r')
user_to_song = {}
song_to_user={}
i=0;
for line in f:
    row = line.split()
    user=row[0]
    temp=row[1:2]    

    if user in user_to_song:
        song=user_to_song[user]
    else:
        song=[]
    song.append(temp)    
    user_to_song[user]=song
    # temp_song=row[1]
    # temp_user=[]
    # temp_user.append(user)
    # temp_user.append(row[2])

    # if temp_song in song_to_user:
    #     users_list=song_to_user[temp_song]
    # else:
    #     users_list=[]
    # users_list.append(temp_user)
    # song_to_user[temp_song]=users_list

songs_weight = dict()
songs_weight['lob']=1

print user_to_song
# print song_to_user


# //function to find similarity between two users
# //and add the weight to each song.

def similarity(u,v):
    list1=user_to_song[u]
    list2=user_to_song[v]
    common=0
    # print list1
    diff=[]
    for item in list2:
        # print item
        if item in list1:
            common=common+1
        else:
            diff.append(item)
    sm=common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
    for item in diff:
        if item[0] in songs_weight:
            songs_weight[item[0]]+=sm
        else:
            songs_weight[item[0]]=sm 
i=0
for u in user_to_song:
    i=i+1
    if(i>1):
        break
    j=0
    songs_weight=dict()
    for v in user_to_song:
        j=j+1
        if j==i:
            continue
        similarity(u,v)
    sorted_songs=sorted(songs_weight.items(),key=lambda x : x[1],reverse=True)[:10]     
    print sorted_songs

    # print sorted_songs[1]

    # for  in sorted_songs:
    #     song=song+(5,)
    #     print song





