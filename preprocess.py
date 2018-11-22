import math
import json
import time
start_time = time.time()
f = open('eval_triplets.txt', 'r')
user_to_song = {}
song_to_user = {}
for line in f:
	row = line.split()
	user=row[0]
	song=row[1]
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

f.close()

user_to_song=json.dumps(user_to_song)
song_to_user=json.dumps(song_to_user)
print("--- %s seconds" % (time.time() - start_time))


file=open("user_to_song.json","w+")
file.write(user_to_song)
file.close()
file=open("song_to_user.json","w+")
file.write(song_to_user)
file.close()
