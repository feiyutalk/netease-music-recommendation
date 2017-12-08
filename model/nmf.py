# -*- coding:utf-8 -*-  
__author__ = 'neuclil'
import surprise
from surprise import NMF, evaluate
from surprise import Dataset, Reader
from model.convertor import Convertor
import os

if __name__ == '__main__':
    convetor = Convertor()

    file_path = os.path.expanduser('../data/popular_music_suprise_format.txt')
    reader = Reader(line_format='user item rating timestamp', sep=',')
    music_data = Dataset.load_from_file(file_path, reader=reader)

    algo = NMF()
    trainset = music_data.build_full_trainset()
    algo.train(trainset)

    user_inner_id = 4
    user_rating = trainset.ur[user_inner_id]
    items = map(lambda x:x[0], user_rating)
    for song in items:
        print(algo.predict(algo.trainset.to_raw_uid(user_inner_id), algo.trainset.to_raw_iid(song),r_ui=1), convetor.get_song_name_by_iid(algo.trainset.to_raw_iid(song)))
    surprise.dump.dump('./nmf.model', algo=algo)