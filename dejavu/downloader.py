from __future__ import unicode_literals
import youtube_dl
import sys
import os
import glob

# Run this file with python downloader.py youtube.com/YourLinkHere, or import in other python file and run with downloader.download(link)

link = sys.argv[1]

# Define the options for youtube downloader. Most important is outtmpl - defines the template for the filename afterwards.
# Downloads the video as a stream, so it can start converting while still downloading. This means max speed is your net speed.
ydl_opts = {
    'format':
    'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist':
    True,
    'outtmpl':
    os.path.join('mp3', '%(title)s.%(ext)s')
}


def download(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #Download the file with the given options
        ydl.download([link])
        #find latest file
        list_of_files = glob.glob(os.path.join('mp3', '*'))
        latest_file = max(list_of_files, key=os.path.getctime)
        # rename folder according to dejavu file names
        os.replace(latest_file, parse_title(latest_file))


# Renames a file from format "artist - title.ext" to  "artist-name--title-name.ext", so it matches dejavus current pattern
def parse_title(file_name):
    words = file_name.split("-")
    artist = words[0].replace(" ", "-")
    title = words[1].replace(" ", "-")
    title_format = artist + title
    return title_format
