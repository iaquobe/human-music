from mido import MidiFile, MidiTrack, Message, MetaMessage
from mido import bpm2tempo

class Note:
    def __init__(self, note, start, duration):
        self.note       = note
        self.start      = start
        self.duration   = duration



class Segment:
    def __init__(self, length=128):
        self.notes = set()
        self.length = length

    def addNote(self, note):
        if note.start + note.duration <= self.length:
            self.notes.add(note)

    def toMidi(self, track, channel, instrument, volume, off=0):
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
                time = k - last
                track.append(Message("control_change", channel=channel, control=7, value=volume, time=0))
                track.append(Message("program_change", channel=channel, program=instrument, time=0))
                track.append(Message(msg, note=note.note, channel=channel, velocity=100, time=time))
                last = k

        return self.length - last
            


class Track:
    def __init__(self, instrument, channel, volume=100):
        self.segments   = []
        self.instrument = instrument
        self.channel = channel
        self.volume = volume

    def toMidi(self, track):
        
        off = 0
        for segment in self.segments:
            off = segment.toMidi(track, self.channel, self.instrument, self.volume, off=off)

        track.append(MetaMessage("end_of_track", time=0))



class Song:
    def __init__(self, bpm=120, tpb=16):
        self.tracks = []
        self.bpm = bpm
        self.tpb = tpb
        self.last_channel = 0

    def newTrack(self, instrument, volume=100, channel=None):
        if channel is not None:
            return Track(instrument, channel, volume)

        t = Track(instrument, self.last_channel, volume)
        self.last_channel = self.last_channel + 1
        return t

    def toMidi(self):
        m = MidiFile(ticks_per_beat=self.tpb)

        metatrack = MidiTrack()
        metatrack.append(MetaMessage("time_signature", numerator=6, denominator=8, clocks_per_click=18, notated_32nd_notes_per_beat=8, time=0))
        metatrack.append(MetaMessage("set_tempo", tempo=bpm2tempo(self.bpm), time=0))
        metatrack.append(MetaMessage("end_of_track", time=0))

        m.tracks.append(metatrack)

        for track in self.tracks:
            t = MidiTrack()
            m.tracks.append(t)
            track.toMidi(t)

        return m
   
