from mido import MidiFile, MidiTrack, Message, MetaMessage
from mido import bpm2tempo

class Note:
    def __init__(self, note, start, duration, channel=0):
        self.note       = note
        self.start      = start
        self.duration   = duration
        self.channel    = channel



class Segment:
    def __init__(self, length=128):
        self.notes = set()
        self.length = length

    def addNote(self, note):
        if note.start + note.duration <= self.length:
            self.notes.add(note)

    def toMidi(self, track, tpb, off=0):
        events = dict()
        for note in self.notes:
            if note.start not in events:
                events[note.start] = []
            if note.start + note.duration not in events:
                events[note.start + note.duration] = []

            events[note.start].append(("note_on", note))
            events[note.start + note.duration].append(("note_off", note))
        
        last = -off 
        for k in sorted(events):
            for event in events[k]:
                msg, note = event
                time = tpb * (k - last)
                track.append(Message(msg, note=note.note, channel=note.channel, velocity=100, time=time))
                last = k

        return self.length - last
            


class Track:
    def __init__(self, instruments, volume=100):
        self.segments   = []
        if isinstance(instruments, int):
            instruments = [instruments]
        self.instruments = instruments
        self.volume = volume

    def toMidi(self, track, tpb):
        track.append(Message("control_change", channel=0, control=7, value=self.volume, time=0))

        for i in range(len(self.instruments)):
            track.append(Message("program_change", channel=i, program=self.instruments[i], time=0))
        
        off = 0
        for segment in self.segments:
            off = segment.toMidi(track, tpb, off=off)

        track.append(MetaMessage("end_of_track", time=0))



class Song:
    def __init__(self):
        self.tracks = []

    def toMidi(self, tpb, bpm):
        m = MidiFile()

        metatrack = MidiTrack()
        metatrack.append(MetaMessage("time_signature", numerator=6, denominator=8, clocks_per_click=18, notated_32nd_notes_per_beat=8, time=0))
        metatrack.append(MetaMessage("set_tempo", tempo=bpm2tempo(bpm), time=0))
        metatrack.append(MetaMessage("end_of_track", time=0))

        m.tracks.append(metatrack)

        for track in self.tracks:
            t = MidiTrack()
            m.tracks.append(t)
            track.toMidi(t, tpb)

        return m
   
