from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_sound_effects(song, length=2, iterations=40, tpb=64):
    ticks = length * tpb
    instruments = [96, 99, 102, 103, 119, 120, 125, 127]

    track = song.newTrack(choice(instruments), volume=80)
    segEmpty = Segment(ticks)
    segEffect = Segment(ticks)
    segEffect.addNote(Note(60, 0, ticks))

    for i in range(iterations):
        r = random()
        if r < .1:
            track.segments.append(segEffect)
        else:
            track.segments.append(segEmpty)

    song.tracks.append(track)
    return song


