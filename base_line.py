from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_baseline(song, bases=None, length=128, iterations=20):
    def rbase():
        return randint(0, len(bases) - 1)


    def main_line():
        se0 = Segment(length=length)

        t = 0
        d = int(length / 4)

        se0.addNote(Note(prog[0], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(prog[1], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(prog[2], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(prog[1], t, d, channel=rbase()))

        return se0


    def alt_line(main):
        se0 = deepcopy(main)

        t = 0
        d = int(length / 4)

        for note in se0.notes:
            if note.start == 3 * d:
                note.note = prog[3]
                note.channel = rbase()

        return se0


    def tense_line(main):
        se0 = deepcopy(main)

        d = int(length / 4)

        drop = choice(list(se0.notes))
        d2 = choice(list(se0.notes))

        if abs(drop.start - d2.start) == d:
            se0.notes.remove(d2)
        se0.notes.remove(drop)

        n = 2**randint(1, 3)
        d = int(d / n)

        s = drop.start

        for i in range(int(n)):
            se0.addNote(Note(drop.note, s, d, channel=drop.channel))
            s = s + d

        return se0 


    if bases == None:
        bases = [choice(range(80, 88)) for i in range(4)]

    t = Track(bases, volume=127)
    song.tracks.append(t)
    
    prog = sorted([randint(20, 40) for i in range(4)])

    se0 = main_line() 
    se1 = alt_line(se0)
    se2 = tense_line(se0)
    
    for i in range(int(iterations / 2)):
        r = random()
        if r < .9:
            t.segments.append(se0)
        else:
            t.segments.append(se2)
        t.segments.append(se1)


    return song
