from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_bass_guitar(song, length=2, iterations=20, tpb=64):
    def tt(beats):
        return int(beats * tpb)

    instrument = 36

    t = song.newTrack(instrument, volume=100)
    song.tracks.append(t)
    
    prog = [randint(0, 20) for i in range(5)]

    se0 = Segment(length * tpb)
    se0.addNote(Note(prog[0], tt(0), tt(2/4)))
    

    t.segments.append(se0)
    t.segments.append(se0)
    t.segments.append(se0)
    t.segments.append(se0)
    t.segments.append(se0)
    t.segments.append(se0)

    return song
