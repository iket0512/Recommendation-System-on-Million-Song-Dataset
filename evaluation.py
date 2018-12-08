#Class to calculate precision and recall

import random

class Precision():
    def __init__(self, test_data, train_data, pm,user_to_song,flag,percentage):
        self.test_data = test_data
        self.train_data = train_data
        self.user_to_song=user_to_song
        self.user_test_sample = None
        self.model1 = pm
        self.flag=flag
        self.create_user_test_sample(percentage)
        
    def create_user_test_sample(self, percentage):
        users_test_and_training = list(set(self.test_data['user_id'].unique()).intersection(set(self.train_data['user_id'].unique())))
        l=len(users_test_and_training)  
        k = int(l * percentage)
        random.seed(0)
        indicies = random.sample(range(l),k)
        self.users_test_sample = [users_test_and_training[i] for i in indicies]
        print("Length of user sample:%d" % len(self.users_test_sample))
        song_grouped =self.train_data.groupby(['song_id']).agg({'listen_count': 'count'}).reset_index()
        temp=song_grouped.sort_values(['listen_count', 'song_id'], ascending = [0,1])[:10]
        self.popular=list(temp['song_id'])
        
    def get_test_sample_recommendations(self):
        if self.flag==1:
            user_sim_items =self.model1.recommend()
            user_list=list(user_sim_items["song_id"])
            for user_id in self.users_test_sample:
                self.pm_training_dict[user_id] = user_list
                self.test_dict[user_id] =set(self.user_to_song[user_id])
                # a= len(self.test_dict[user_id].intersection(self.pm_training_dict[user_id]))
        elif self.flag==2:
            for user_id in self.users_test_sample:
                # print user_id
                song_list = self.model1.recommend(user_id)
                if len(song_list)==0:
                    song_list1=self.popular
                else:
                    song_list1,temp=zip(*song_list)
                self.pm_training_dict[user_id]=song_list1
                self.test_dict[user_id] =set(self.user_to_song[user_id]) 

    def calculate_precision_recall(self):
        cutoff_list = list(range(1,11))
        pm_avg_precision_list = []
        pm_avg_recall_list = []
        num_users_sample = len(self.users_test_sample)
        pre_sum=0;
        rec_sum=0;
        for N in cutoff_list:
            pm_sum_precision = 0
            pm_sum_recall = 0
            pm_avg_precision = 0
            pm_avg_recall = 0
            for user_id in self.users_test_sample:
                pm_hitset = set(self.test_dict[user_id]).intersection(set(self.pm_training_dict[user_id][0:N]))
                testset = self.test_dict[user_id]
                pm_sum_precision += float(len(pm_hitset))/float(N)
                pm_sum_recall += float(len(pm_hitset))/float(len(testset))

            pm_avg_precision = pm_sum_precision/float(num_users_sample)
            pm_avg_recall = pm_sum_recall/float(num_users_sample)
            pm_avg_precision_list.append(pm_avg_precision)
            pm_avg_recall_list.append(pm_avg_recall)
            pre_sum+=pm_avg_precision;
            rec_sum+=pm_avg_recall;
        print (pre_sum/10)
        print (rec_sum/10 )   
        # return (pm_avg_precision_list, pm_avg_recall_list)
        return pre_sum/10 ,rec_sum/10

    def calculate(self): 
        self.pm_training_dict = dict()
        self.test_dict = dict()
        self.get_test_sample_recommendations()
        return self.calculate_precision_recall()
