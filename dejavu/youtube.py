import sys, getopt
import urllib.request
import urllib.parse
import os
import re
import downloader


def song(songName):
    query_string = urllib.parse.urlencode({"search_query": str(songName)})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                html_content.read().decode())
    result = "http://www.youtube.com/watch?v=" + search_results[0]
    print(result)
    # Download that link
    downloader.download(result)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "v:", ["video="])
    except getopt.GetoptError:
        print('Wrong arguments, use -v songName')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-v':
            song(str(arg))


if __name__ == "__main__":
    main(sys.argv[1:])
