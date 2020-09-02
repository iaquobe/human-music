#!/bin/bash

./gen.py

timidity data/mid.mid -Ow -o data/wav.wav 1>/dev/null

ffmpeg -y -loop 1 -framerate 1 -i cassetti.jpg -i data/wav.wav -c copy -shortest data/vid.mkv 1>/dev/null



