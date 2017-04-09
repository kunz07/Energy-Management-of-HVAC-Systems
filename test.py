from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg

data = np.array([
    [0.0, 0.5, 0.0],
    [0.5, 1.0, 0.5],
    [0.0, 0.5, 0.0]
])
pg.plot(data)
