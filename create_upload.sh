#!/bin/bash

dir="$(pwd)/$(dirname "$0")"

$dir/create.sh

$dir/upload.sh "$($dir/gen_title.py)" $dir/data/vid.mkv
