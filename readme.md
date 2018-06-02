# Impossible Technology

## David Martin Carl, Tjalfe Jon Klarskov Møller, Anton Kornholt & Kasper Ravn Breindal

### Project - Audio fingerprinting with Python

We want to create some tools that wrap around audio recognizing with dejavu.

To make it easy to add songs to our database, we have spent time making a program, that you give a search query (song - artist), which it then searches for, downloads, converts to mp3 and fingerprints into the database. Then it can be recognized afterwards.

We will make the changes to the dejavu project that makes it more efficient - Change timed searches to confidence level based searches

* * *

### Installation

Windows (Requires Git Bash or other Bash terminal):

```bash
git clone https://github.com/kasperonfire/ImpossibleTechnologyProject && cd ImpossibleTechnologyProject
```

Linux/Mac:

```bash
git clone https://github.com/kasperonfire/ImpossibleTechnologyProject
cd ImpossibleTechnologyProject
chmod +x DejavuSetup.sh
./DejavuSetup.sh
```

### Usage

We recommend running the project on a local MySQL Database. Create a database, and a user with permissions for that Database, and put in your settings in dejavu.cnf

To Download a song to learn directory:

```bash
python youtube.py -v "search query - can be one word, or artist + title, or anything"
```

To Learn the songs in the learn directory:

```bash
python learner.py
```

To Recognize a song:

```bash
python visualize_pyqtgraph.py
```

### Resources

[Dejavu audio fingerprinting](https://github.com/worldveil/dejavu)

[Article abous dejavu](http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/)

[youtube-dl](https://rg3.github.io/youtube-dl/)
