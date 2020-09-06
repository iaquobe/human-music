#!/bin/bash

dir="$(pwd)/$(dirname "$0")"

$dir/gen.py $dir/data/mid.mid

timidity $dir/data/mid.mid -Ow -o $dir/data/wav.wav 1>/dev/null

ffmpeg -y -loop 1 -framerate 1 -i $dir/cassetti.jpg -i $dir/data/wav.wav -c copy -shortest $dir/data/vid.mkv 1>/dev/null

youtube-upload -t "$($dir/gen_title.py)" --privacy private --client-secrets secret.json $dir/data/vid.mkv
