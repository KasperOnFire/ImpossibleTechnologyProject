from pyqtgraph.Qt import QtGui, QtCore
from dejavu.recognize import FileRecognizer
from dejavu import Dejavu
import youtube
import os
import sys
import time
import numpy as np
import pyqtgraph as pg
import pyaudio
import wave
import threading
import json


with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

confidence = 0
song = {}

REQUIRED_CONFIDENCE = 100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"
FORMAT = pyaudio.paInt16
CHANNELS = 2
DEFAULT_CONFIG_FILE = "dejavu.cnf.SAMPLE"

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Realtime Soundwave Chunk Plot")
win.resize(1000,600)
win.setWindowTitle('Realtime Soundwave Chunk Plot')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

RATE = 44100
CHUNK = int(RATE/12)
sound_plot = win.addPlot(title="Updating plot")
curve = sound_plot.plot(pen='y')
p=pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHUNK)
sound_plot.setYRange(-2**15-10000, 2**15+10000, padding=None, update=True)

frames = []

def findSong():
    global confidence, song
    djv = Dejavu(config)
    song_internal = djv.recognize(FileRecognizer, "voice.wav")
    print(song_internal)
    confidence = song_internal['confidence']
    song = song_internal

def save():
    global frames 
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
def update():
    global curve, CHUNK, frames, start_time, app
    if time.time() - start_time > 10:
        save()
        #timer.stop()
        #app.closeAllWindows()
        if confidence < REQUIRED_CONFIDENCE:
            t = threading.Thread(target=findSong, args=())
            t.start()
        start_time = time.time()
        if confidence > REQUIRED_CONFIDENCE:
            timer.stop()
            app.closeAllWindows()
            print("Pretty sure the song is the following!")
            print("'" + song['song_name'] + "' with a confidence of " + str(confidence))
            youtube.song(song['song_name'])
            sys.exit(0)
    data = stream.read(CHUNK)
    frames.append(data)
    dataVis = np.fromstring(data, dtype=np.int16)
    curve.setData(dataVis)

start_time = time.time()
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1) #refresh rate

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()