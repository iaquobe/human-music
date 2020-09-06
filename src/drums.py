from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_drums(song, length=16, iterations=160):
    def hihats():
        n = list()
        s = 0
        d = int(length / 4)
        for i in range(4):
            n.append(Note(hihats, s, d, channel=9))
            s = s + d
        return n

    def kickdrum():
        t = Track(100, volume=10)
        see = Segment(length=length)
        for i in range(int(iterations/8)):
            t.segments.append(see)

        for i in range(int(3 * iterations/4)):
            if random() < .8:
                se0 = Segment(length=length)

                se0.addNote(Note(drum, int(length/2), int(length/4), channel=9))

                t.segments.append(se0)
        return t


    hihats = 42
    drum = 36
    song.tracks.append(kickdrum())

    return song
