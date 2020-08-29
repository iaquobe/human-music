from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_drums(song, length=16, iterations=80):
    def hihats():
        n = list()
        s = 0
        d = int(length / 8)
        for i in range(8):
            n.append(Note(hihats, s, d, channel=9))
            s = s + d
        return n

    t = Track(100, volume=10)
    song.tracks.append(t)

    hihats = 42
    drum = 36

    for i in range(iterations):
        se0 = Segment(length=length)

        se0.addNote(Note(drum, 0, int(length/4), channel=9))
        se0.addNote(Note(drum, int(length/2), int(length/4), channel=9))

        s = 0
        d = int(length/2)
        for i in range(2):
            se0.addNote(Note(hihats, s, d, channel=9))
            s = s + d

        t.segments.append(se0)

    return song
