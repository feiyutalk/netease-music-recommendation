# -*- coding:utf-8 -*-  
__author__ = 'neuclil'
import json
import sys
import os

def parse_file(in_file, out_file):
    out = open(out_file, 'w')
    for line in open(in_file):
        result = parse_song_line(line)
        if(result):
            out.write(result.strip()+"\n")
    out.close()


def parse_song_line(line):
    data = json.loads(line)
    name = data['result']['name']
    tags = ','.join(data['result']['tags'])
    subscribed_count = data['result']['subscribedCount']
    if(subscribed_count < 100):
        return False
    playlist_id = data['result']['id']
    song_info = ''
    songs = data['result']['tracks']
    for song in songs:
        try:
            song_info += '\t'+':::'.join([str(song['id']), song['name'], song['artists'][0]['name'], str(song['popularity'])])
        except Exception as e:
            continue
    return name + '##' + tags + '##' + str(playlist_id) + '##' + str(subscribed_count) + song_info


if __name__ == '__main__':
    # parse_file('../p')
    # in_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/playlistdetail.all.json')
    parse_file('../data/playlistdetail.all.json', '../data/netease_music_playlist.txt')