# sbv2txt
A python script to convert Youtube Caption files in sbv to plain text transcripts.

Youtube does a good job of creating automatic transcriptions of videos.
It's very benefical to download the automatic transcriptions, convert them to plain text,
and then edit the transcriptions, and re-upload them.

This simple utility takes a Caption file from sbv format and converts it to a plain
text file without the timing. It can be edited, saved, and re-uploaded to Youtube
as a Transcript which Youtube will automatically set timings for.

### Usage:

Requires Python to be installed.

Command line:
```
python sbv2txt.py [Source SBV Filename] [Destination TXT Filename]
```

Example:
```
python sbv2txt.py captions.sbv transcript.txt
```

Hope you find this useful! Adding Captions to a video can improve the viewership
and popularity of a video so this tool will hopefully come in handy.

Regards,
Geoff Peters
http://twitter.com/gpeters
