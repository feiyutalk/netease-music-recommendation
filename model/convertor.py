# -*- coding:utf-8 -*-  
__author__ = 'neuclil'

import _pickle as pickle
import os


class Convertor():
    def __init__(self) -> None:
        # 歌单 <-> id
        self.id_name_dict = pickle.load(open('../data/popular_playlist.pkl', 'rb'), encoding='utf8')
        print('加载歌单id到歌单名映射字典完成...')
        self.name_id_dict = {}
        for playlist_id in self.id_name_dict:
            self.name_id_dict[self.id_name_dict[playlist_id]] = playlist_id
        print('加载歌单名到歌单id的映射字典完成')
        # 歌曲 <-> id
        self.song_id_name_dict = pickle.load(open('../data/popular_song.pkl', 'rb'), encoding='utf8')
        print('加载歌曲id到歌曲名的映射字典完成..')
        song_name_id_dict = {}
        for song_id in self.song_id_name_dict:
            song_name_id_dict[self.song_id_name_dict[song_id]] = song_id
        print('加载歌曲名到歌曲id的映射字典完成..')

    def get_name_by_index(self, index):
        return list(self.name_id_dict.keys())[index]

    def get_name_by_rid(self, rid):
        return self.id_name_dict[rid]

    def get_rid_by_name(self, name):
        return self.name_id_dict[name]

    def get_song_name_by_iid(self, iid):
        return self.song_id_name_dict[iid]