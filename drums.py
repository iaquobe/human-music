from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_drums(song, length=32, iterations=80):
    def main_line():
        se0 = Segment(length=length)

        t = 0
        d = int(length / 8)

        se0.addNote(Note(progression[0], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        t = t + 2 * d
        se0.addNote(Note(progression[3], t, d, channel=9))

        return se0

    def aggresive_var():
        se0 = Segment(length=length)

        t = 0
        d = int(length / 16)

        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[1], t, d, channel=9))
        t = t + 2 * d
        se0.addNote(Note(progression[2], t, 3 * d, channel=9))

        return se0



    progression = [choice(range(30, 50)) for i in range(5)]

    t = Track(100, volume=10)
    song.tracks.append(t)

    se0 = main_line()
    se1 = aggresive_var()

    for i in range(iterations):
        r = random()
        if r < .90:
            t.segments.append(se0)
        else:
            t.segments.append(se1)

    return song
