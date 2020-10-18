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

## Tutorial Video on How to Use sbv2txt

I created a quick tutorial on how to use sbv2txt to download the automatic Youtube captions,
convert them to a text transcript, edit them, and then re-upload the edited transcription to
make better captions.

For my tutorial video on how to use sbv2txt please check out the following links:
- https://www.youtube.com/watch?v=a8fbL918qYU
- https://geoffmobile.com/blog/how-to-use-sbv2txt-youtube-captions-file-convert-to-transcript

## Typical Workflow for Youtube Captions using sbv2txt

sbv2txt provides an easier way to add captions to your Youtube videos.

- First, download the auto-generated captions file as a “.sbv” file from Youtube.
- Then use sbv2txt as shown in the video to convert the captions file to a plain text transcript.
- Edit the transcription to correct errors and add capitals/punctuation. 
- Then re-upload the transcript file and make Youtube sync up the timing automatically.﻿

## License

This script is provided under the MIT License.

## Author Contact

Geoff Peters

http://twitter.com/gpeters
