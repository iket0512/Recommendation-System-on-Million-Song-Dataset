import math

class ItemBased:
	user_songs=[]
	song_to_users={}
	sorted_songs=dict()
	def __init__(self,user_songs,sorted_songs,song_to_users):
		self.user_songs=user_songs
		self.sorted_songs=sorted_songs
		self.song_to_users=song_to_users

	def similarity(song1,song2):
		list1=song_to_users[song1]
		list2=song_to_users[song2]
		common=0
		for x in list1:
			if x in list2:
				common=common+1
		sm= common/(math.sqrt(len(list1))*math.sqrt(len(list2)))
		return sm

	def calc_wo_meta():
		i=0
		for song_cand in sorted_songs:
			for song in user_songs:
				sm=similarity(song_cand[0],song[0])
				sorted_songs[i]=sorted_songs[i]+(sm,)
			i+=1

		# decide weight multiplier of user and item based weightage

	def cal_with_meta():
		




