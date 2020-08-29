# Human Music

This is a project to automate music generation.\
Most of the project is dedicated to create MIDI files.\
The rest are some scripts to transform those MIDI files to videos with a static background that can be uploaded to youtube.

Eventually the goal is to create a new song every week and upload it to youtube.\
https://www.youtube.com/channel/UCDfNLU_M0MK3WOsIsScWirw \
This is the channel where they should be uploaded to.\
Right now Youtube blocks new videos as private because they are uploaded automatically.\
I'm trying to get into contact with them for that right now.

# What is the solution?

The scripts to create a video are running as cronjobs on my vps weekly.\
It is hosted on contaboo at 5.189.146.192

# What I use

youtube uploader at:\
https://github.com/tokland/youtube-upload/

ffmpeg, cronjobs, and timidity
