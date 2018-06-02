from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pyaudio

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

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
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,input=True, frames_per_buffer=CHUNK)
#p6(([0,len(data),-2**16/2,2**16/2]))
sound_plot.setYRange(-2**15-10000, 2**15+10000, padding=None, update=True)

def update():
    global curve, CHUNK
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    curve.setData(data)
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()