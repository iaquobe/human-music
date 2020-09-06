from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_bass(song, length=8, iterations=20, tpb=64):
    def tt(beats):
        return int(beats * tpb)

    instrument = 82

    t = song.newTrack(instrument, volume=127)
    song.tracks.append(t)
    
    prog = [randint(30, 50) for i in range(5)]

    se0 = Segment(length * tpb)
    se0.addNote(Note(prog[0], tt(0), tt(1)))
    se0.addNote(Note(prog[1], tt(1), tt(1)))
    se0.addNote(Note(prog[2], tt(2), tt(1)))
    se0.addNote(Note(prog[3], tt(3), tt(1)))
    
    se0.addNote(Note(prog[0], tt(4), tt(1)))
    se0.addNote(Note(prog[1], tt(5), tt(1)))
    se0.addNote(Note(prog[2], tt(6), tt(1)))
    se0.addNote(Note(prog[4], tt(7), tt(1)))


    for i in range(int(iterations/2)):
        t.segments.append(se0)
        t.segments.append(se0)

    return song
