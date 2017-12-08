# -*- coding:utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
__author__ = 'neuclil'

import os
import surprise
from model.convertor import Convertor
from surprise import KNNBaseline, Reader
from surprise import Dataset

if __name__ == '__main__':
    convertor = Convertor()

    file_path = os.path.expanduser('../data/popular_music_suprise_format.txt')
    reader = Reader(line_format='user item rating timestamp', sep=',')
    music_data = Dataset.load_from_file(file_path, reader=reader)
    print('构建数据集')
    trainset = music_data.build_full_trainset()

    # 开始训练模型
    print('开始训练模型...')
    algo = KNNBaseline()
    algo.train(trainset)

    print()
    print('针对歌单进行预测:')
    current_playlist_name = convertor.get_name_by_index(39)
    print('歌单名称', current_playlist_name)

    playlist_rid = convertor.get_rid_by_name(current_playlist_name)
    print('歌单rid', playlist_rid)

    playlist_inner_id = algo.trainset.to_inner_uid(playlist_rid)
    print('歌曲inid', playlist_inner_id)

    playlist_neighbors_inner_ids = algo.get_neighbors(playlist_inner_id, k=10)
    playlist_neighbors_rids = (algo.trainset.to_raw_uid(inner_id) for inner_id in playlist_neighbors_inner_ids)
    playlist_neighbors_names = (convertor.get_name_by_rid(rid) for rid in playlist_neighbors_rids)

    print()
    print('歌单 《', current_playlist_name, '》 最接近的10个歌单为: \n')
    for playlist_name in playlist_neighbors_names:
        print(playlist_name, algo.trainset.to_inner_uid(convertor.get_rid_by_name(playlist_name)))

    print()
    print('针对用户进行预测:')
    user_inner_id = 4
    print('用户内部id', user_inner_id)
    user_rating = trainset.ur[user_inner_id]
    print('用户评价过的歌曲数量', len(user_rating))
    items = map(lambda x:x[0], user_rating)
    for song in items:
        print(algo.predict(user_inner_id, song, r_ui=1), convertor.get_song_name_by_iid(algo.trainset.to_raw_iid(song)))
    surprise.dump.dump('./knn_baseline.model', algo=algo)