from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_bass_guitar(song, length=2, iterations=20, tpb=64):
    ticks = length * tpb

    instrument = 36

    track = song.newTrack(instrument, volume=100)
    
    note = [randint(30, 40) for i in range(5)]

    seg = Segment(ticks)
    seg.addNote(Note(note[0], 0, 2*tpb))
    
    for i in range(iterations):
        track.segments.append(seg)

    song.tracks.append(track)

    return song
