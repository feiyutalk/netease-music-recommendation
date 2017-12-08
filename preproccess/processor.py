# -*- coding:utf-8 -*-  
__author__ = 'neuclil'

import json
import sys


def is_null(s):
    return len(s.split(',')) > 2


def process_song_info(song_info):
    try:
        song_id, name, artist, popularity = song_info.split(':::')
        return ','.join([song_id, '1.0', '1300000'])
    except Exception as e:
        return ''


def process_playlist_line(in_line):
    try:
        contents = in_line.strip().split('\t')
        name, tags, playlist_id, subscribed_count = contents[0].split('##')
        songs_info = map(lambda x: playlist_id+','+process_song_info(x), contents[1:])
        songs_info = filter(is_null, songs_info)
        return '\n'.join(songs_info)
    except Exception as e:
        print(e)
        return False


def process_file(in_file, out_file):
    out = open(out_file, 'w')
    for line in open(in_file):
        result = process_playlist_line(line)
        if(result):
            out.write(result.strip()+'\n')
    out.close()


if __name__ == '__main__':
    process_file('../data/netease_music_playlist.txt', '../data/netease_music_surprise_format.txt')
    # process_file('../data/popular.playlist', '../data/popular_music_surprise_format.txt')
