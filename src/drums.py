from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_drums(song, length=2, iterations=40, tpb=64):

    def hihats0():
        se = Segment(ticks)

        s = 0
        d = int(ticks / 4)
        for i in range(4):
            se.addNote(Note(42, s, d)) 
            s = s + d
        return se 

    def hihats1():
        se = Segment(ticks)

        s = 0
        d = int(ticks / 8)
        for i in range(8):
            se.addNote(Note(42, s, d)) 
            s = s + d
        return se 

    def kickdrum0():
        se = Segment(ticks)
        se.addNote(Note(36, int(ticks/2), int(ticks/4)))

        return se

    def kickdrum1():
        se = Segment(ticks)
        se.addNote(Note(36, 0, int(ticks/4)))
        se.addNote(Note(36, int(ticks/2), int(ticks/4)))
        se.addNote(Note(36, int(3*ticks/4), int(ticks/4)))

        return se

    ticks = length * tpb
    segEmpty = Segment(ticks)
    segDrum0  = kickdrum0()
    segDrum1  = kickdrum1()
    segHihat0 = hihats0()
    segHihat1 = hihats1()

    trackDrum  = Track(36, 9, volume=100)
    trackHihat = Track(42, 9, volume=randint(50,100))

    for i in range(iterations):
        r = random()
        if r < .6:
            trackDrum.segments.append(segDrum0)
        elif r < .8:
            trackDrum.segments.append(segDrum1)
        else:
            trackDrum.segments.append(segEmpty)

        r = random()
        if r < .5:
            trackHihat.segments.append(segHihat1)
        elif r < .7:
            trackHihat.segments.append(segHihat0)
        else:
            trackHihat.segments.append(segEmpty)

    song.tracks.append(trackDrum)
    song.tracks.append(trackHihat)
    
    return song
