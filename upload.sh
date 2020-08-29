#!/bin/bash

python3 gen.py

timidity $1 -Ow -o wav.wav

ffmpeg -y -loop 1 -framerate 1 -i cassetti.jpg -i wav.wav -c copy -shortest vid.mkv



