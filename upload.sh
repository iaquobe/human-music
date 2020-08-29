#!/bin/bash

python3 ./gen.py

timidity ./testing.mid -Ow -o - \
	| ffmpeg -loop 1 -i ./casseti.jpg -i - -c:a copy out.mp4
