from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_drums(song, length=2, iterations=20, tpb=64):
    def hihats():
        n = list()
        s = 0
        d = int(length / 4)
        for i in range(4):
            n.append(Note(hihats, s, d))
            s = s + d
        return n

    def kickdrum():
        t = Track(100, 9, volume=100)
        see = Segment(length * tpb)
        for i in range(int(iterations/8)):
            t.segments.append(see)

        for i in range(int(3 * iterations/4)):
            if random() < .8:
                se0 = Segment(length * tpb)

                se0.addNote(Note(drum, int(length/2), int(length/4)))

                t.segments.append(se0)
            else:
                t.segments.append(see)
        return t


    hihats = 42
    drum = 36
    song.tracks.append(kickdrum())

    return song
