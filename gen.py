#!/usr/bin/python3

from miparser import Note, Track, Segment, Song
from random import randint, seed, choice
from copy import deepcopy

from bass import add_bass
from bass_guitar import add_bass_guitar
from drums import add_drums


se = randint(0, 1000000)
print(se)
seed(se)

tpb = 16
bpm = 81

s = Song(tpb, bpm)

s = add_bass_guitar(s, tpb=tpb)
s = add_bass(s, tpb=tpb)

mid = s.toMidi()
mid.save("mid.mid")

