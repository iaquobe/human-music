#!/usr/bin/python3

from miparser import Note, Track, Segment, Song

s = Song()
t = Track(114)
seg = Segment()

seg.notes.add(Note(80, 0, 1))
seg.notes.add(Note(80, 1, 1))
t.segments.append(seg)
s.tracks.append(t)

mid = s.toMidi(1000)
mid.save("testing.mid")


