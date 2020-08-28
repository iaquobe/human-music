#!/usr/bin/python3

from miparser import Note, Track, Segment, Song
from random import randint, seed, choice
from copy import deepcopy

from base_line import add_baseline
from drums import add_drums


se = randint(0, 1000000)
print(se)
seed(se)

s = Song()

s = add_baseline(s)
s = add_drums(s)

mid = s.toMidi(64, 160)
mid.save("testing.mid")

