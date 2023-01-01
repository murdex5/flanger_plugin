import wave
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore

# Open the audio file
with wave.open('input.wav', 'rb') as wav:
    # Read the audio data and sample rate
    data = wav.readframes(wav.getnframes())
    rate = wav.getframerate()

# Convert the audio data to a NumPy array
data = np.frombuffer(data, dtype=np.int16)

# Set the flanger parameters
depth = 0.5  # Depth of the flanger effect (0.0 - 1.0)
rate = 0.5   # Rate of the flanger effect (0.0 - 1.0)
delay = 0.5  # Base delay time (in seconds)

# Create a sine wave to use as the LFO
lfo_freq = 5  # LFO frequency (in Hz)
t = np.arange(len(data)) / rate  # Time array (in seconds)
lfo = np.sin(2 * np.pi * lfo_freq * t)

# Create the flanger effect by modulating the delay time with the LFO
delay = delay + depth * lfo
indices = np.arange(len(data)) + np.round(delay * rate).astype(int)
flanged = data[indices % len(data)]

# Save the flanged audio data to a new wave file
with wave.open('output.wav', 'wb') as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(rate)
    wav.writeframes(flanged.astype(np.int16))

with wave.open('output.wav', 'wb') as wav:
    # Set the sample rate
    wav.setframerate(44100)
    # Set the number of channels
    wav.setnchannels(1)
    # Set the sample width
    wav.setsampwidth(2)
    # Write the audio data
    wav.writeframes(flanged.astype(np.int16))

class FlangerDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the user interface
        self.setWindowTitle('Flanger Effect')
        self.setMinimumSize(400, 200)
        self.layout = QtGui.QVBoxLayout(self)

        # Add sliders for the flanger parameters
        self.depth_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.depth_slider.setMinimum(0)
        self.depth_slider.setMaximum(100)
        self.depth_slider.setValue(50)
        self.layout.addWidget(QtGui.QLabel('Depth'))
        self.layout.addWidget(self.depth_slider)

        self.rate_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.rate_slider.setMinimum(0)
        self.rate_slider.setMaximum(100)
        self.rate_slider.setValue(50)
        self.layout.addWidget(QtGui.QLabel('Rate'))
        self.layout.addWidget(self.rate_slider)

        self.delay_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.delay_slider.setMinimum(0)
        self.delay_slider.setMaximum(100)
        self.delay_slider.setValue(50)
        self.layout.addWidget(QtGui.QLabel('Delay'))
        self.layout.addWidget(self.delay_slider)

        # Add a button to apply the flanger effect
        self.button = QtGui.QPushButton('Apply Flanger')
        self.button.clicked.connect(self.apply_flanger)
        self.layout.addWidget(self.button)

    def apply_flanger(self):
        # Read the audio data and sample rate
        with wave.open('input.wav', 'rb') as wav:
            data = wav.readframes(wav.getnframes())
            rate = wav.getframerate()

        # Convert the audio data to a NumPy array
        data = np.frombuffer(data, dtype=np.int16)

        # Get the flanger parameters from the sliders
        depth = self.depth_slider.value() / 100
        rate = self.rate_slider.value() / 100
        delay = self.delay_slider.value() / 100

        # Create a sine wave to use as the LFO
        lfo_freq = 5  # LFO frequency (in Hz)
        t = np.arange(len(data)) / rate 
