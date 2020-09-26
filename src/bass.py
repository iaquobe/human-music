from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_bass(song, length=8, iterations=10, tpb=64):

    def melody():
        se = Segment(ticks)
        se.addNote(Note(noteMelody[0], 0*tpb, tpb))
        se.addNote(Note(noteMelody[1], 1*tpb, tpb))
        se.addNote(Note(noteMelody[2], 2*tpb, tpb))
        se.addNote(Note(noteMelody[3], 3*tpb, tpb))
        
        se.addNote(Note(noteMelody[0], 4*tpb, tpb))
        se.addNote(Note(noteMelody[1], 5*tpb, tpb))
        se.addNote(Note(noteMelody[2], 6*tpb, tpb))
        se.addNote(Note(noteMelody[4], 7*tpb, tpb))

        return se

    def low():
        se = Segment(ticks)
        se.addNote(Note(noteLow, tpb, 4*tpb))

        return se

    ticks = length * tpb

    instrumentMelody = randint(81,88)
    instrumentLow = 81

    noteMelody = [randint(30, 50) for i in range(5)]
    noteLow = randint(10, 30)

    segEmpty = Segment(ticks)
    segMelody = melody()
    segLow = low()

    trackMelody = song.newTrack(instrumentMelody, volume=100)
    trackLow = song.newTrack(instrumentLow, volume=127)

    for i in range(iterations):
        trackMelody.segments.append(segMelody)

        r = random()
        if r < .8:
            trackLow.segments.append(segEmpty)
        else:
            trackLow.segments.append(segLow)

    song.tracks.append(trackMelody)
    song.tracks.append(trackLow)

    return song
