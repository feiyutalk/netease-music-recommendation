# -*- coding:utf-8 -*-  
__author__ = 'neuclil'


import _pickle as pickle
import sys

def parse_playlist_get_info(in_line, playlist_dict, song_dict):
    contents = in_line.strip().split('\t')
    name, tags, playlist_id, subscribed_count = contents[0].split('##')
    playlist_dict[playlist_id] = name
    for song in contents[1:]:
        try:
            song_id, song_name, artist, popularity = song.split(':::')
            song_dict[song_id] = song_name + '\t' + artist
        except Exception as e:
            print('song format error')
            print(song+'\n')


def parse_file(in_file, out_playlist, out_song):
    playlist_dict = {}
    song_dict = {}
    for line in open(in_file):
        parse_playlist_get_info(line, playlist_dict, song_dict)
    pickle.dump(playlist_dict, open(out_playlist, 'wb'))
    pickle.dump(song_dict, open(out_song, 'wb'))


if __name__ == '__main__':
    parse_file('../data/netease_music_playlist.txt', '../data/playlist.pkl', '../data/song.pkl')