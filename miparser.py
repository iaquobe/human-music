from mido import MidiFile, MidiTrack, Message, MetaMessage

class Note:
    def __init__(self, note, start, duration):
        self.note       = note
        self.start      = start
        self.duration   = duration



class Segment:
    def __init__(self):
        self.notes = set()

    def toMidi(self, track, tpb):
        events = dict()
        for note in self.notes:
            if note.start not in events:
                events[note.start] = []
            if note.start + note.duration not in events:
                events[note.start + note.duration] = []

            events[note.start].append(("note_on", note))
            events[note.start + note.duration].append(("note_off", note))
        
        last = 0
        for k in sorted(events):
            for event in events[k]:
                msg, note = event
                time = tpb * (k - last)
                track.append(Message(msg, note=note.note, velocity=100, time=time, channel=0))
                last = k
            


class Track:
    def __init__(self, instrument):
        self.segments   = []
        self.instrument = instrument

    def toMidi(self, track, tpb):
        track.append(Message("control_change", channel=0, control=7, value=100, time=0))
        track.append(Message("program_change", channel=0, program=self.instrument, time=0))

        for segment in self.segments:
            segment.toMidi(track, tpb)

        track.append(MetaMessage("end_of_track", time=0))



class Song:
    def __init__(self):
        self.tracks = []

    def toMidi(self, tpb):
        m = MidiFile()

        metatrack = MidiTrack()
        metatrack.append(MetaMessage("time_signature", numerator=6, denominator=8, clocks_per_click=18, notated_32nd_notes_per_beat=8, time=0))
        metatrack.append(MetaMessage("set_tempo", tempo=396825, time=0))
        metatrack.append(MetaMessage("end_of_track", time=0))

        m.tracks.append(metatrack)

        for track in self.tracks:
            t = MidiTrack()
            m.tracks.append(t)
            track.toMidi(t, tpb)

        return m
   
