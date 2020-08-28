from miparser import Note, Track, Segment, Song
from random import randint, seed, choice, random
from copy import deepcopy


def add_baseline(song, bases=None, length=128, iterations=20):
    def rbase():
        return choice(range(nbases))

    def main_line():
        se0 = Segment(length=length)

        b1 = rbase()
        b2 = rbase()
        b3 = rbase()

        t = 0
        d = int(length / 4)

        se0.addNote(Note(progression[0], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(progression[1], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(progression[2], t, d, channel=rbase()))
        t = t + d
        se0.addNote(Note(progression[3], t, d, channel=rbase()))

        return se0

    def tense_var0(se0):
        se1 = deepcopy(se0)

        note = choice(list(se1.notes))
        se1.notes.remove(note)
       
        t = note.start 
        d = int(length / 16)

        se1.addNote(Note(progression[1], t, d, note.channel))
        t = t + d
        se1.addNote(Note(progression[1], t, d, note.channel))
        t = t + d
        t = t + d
        se1.addNote(Note(progression[2], t, d, note.channel))

        return se1

    def tense_var1(se0):
        se1 = deepcopy(se0)

        note = choice(list(se1.notes))
        se1.notes.remove(note)
       
        t = note.start 
        d = int(length / 32)

        se1.addNote(Note(note.note, t, d, note.channel))
        t = t + d
        se1.addNote(Note(note.note, t, d, note.channel))
        t = t + d
        se1.addNote(Note(note.note, t, d, note.channel))
        t = t + d
        se1.addNote(Note(note.note, t, d, note.channel))
        t = t + d
        t = t + d
        t = t + d
        t = t + d
        se1.addNote(Note(progression[2], t, d, note.channel))

        return se1



    if bases == None:
        nbases = randint(2, 5)
        bases = [choice(range(80, 88)) for i in range(nbases)]

    t = Track(bases, volume=127)
    song.tracks.append(t)
    
    progression = [choice(range(20, 40)) for i in range(5)]

    se0 = main_line() 
    se1 = tense_var0(se0)
    se2 = tense_var1(se0)
    
    for i in range(iterations):
        r = random()
        if r < .5:
            t.segments.append(se0)
        elif r < .75:
            t.segments.append(se2)
        else:
            t.segments.append(se1)


    return song
