#!/bin/bash

youtube-upload -t "$1" --privacy private --client-secrets secret.json "$2"
