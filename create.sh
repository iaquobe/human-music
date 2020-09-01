#!/bin/bash

./gen.py

timidity mid.mid -Ow -o wav.wav 1>/dev/null

ffmpeg -y -loop 1 -framerate 1 -i cassetti.jpg -i wav.wav -c copy -shortest vid.mkv 1>/dev/null



