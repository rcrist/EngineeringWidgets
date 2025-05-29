import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QHBoxLayout, QPushButton
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
from PyQt6.QtCore import *
from template import BaseWidget

class DigitalOscilloscopeWidget(BaseWidget):
    """
    Digital Oscilloscope Widget for real-time signal visualization.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Digital Oscilloscope")
        self.init_oscilloscope()

    def init_oscilloscope(self):
        # Add plot widget
        self.plot_widget = pg.PlotWidget(title="Oscilloscope")
        self.layout().addWidget(self.plot_widget)

        # Frequency and Amplitude controls
        control_layout = QHBoxLayout()
        freq_label = QLabel("Frequency (Hz):")
        self.freq_spin = QSpinBox()
        self.freq_spin.setRange(1, 100)
        self.freq_spin.setValue(5)
        amp_label = QLabel("Amplitude:")
        self.amp_spin = QSpinBox()
        self.amp_spin.setRange(1, 10)
        self.amp_spin.setValue(1)
        control_layout.addWidget(freq_label)
        control_layout.addWidget(self.freq_spin)
        control_layout.addWidget(amp_label)
        control_layout.addWidget(self.amp_spin)
        self.layout().addLayout(control_layout)

        # Add control buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        self.layout().addLayout(btn_layout)

        # Signal data
        self.x = np.linspace(0, 1, 1000)
        self.y = np.zeros(1000)
        self.curve = self.plot_widget.plot(self.x, self.y, pen='y')

        # Timer for updating plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        # Connect buttons and controls
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.freq_spin.valueChanged.connect(self.update_params)
        self.amp_spin.valueChanged.connect(self.update_params)

        self.phase = 0
        self.frequency = self.freq_spin.value()
        self.amplitude = self.amp_spin.value()

    def start(self):
        self.timer.start(30)  # Update every 30 ms

    def stop(self):
        self.timer.stop()

    def update_params(self):
        self.frequency = self.freq_spin.value()
        self.amplitude = self.amp_spin.value()

    def update_plot(self):
        # Simulate a sine wave signal with adjustable frequency and amplitude
        self.phase += 0.1
        self.y = self.amplitude * np.sin(2 * np.pi * self.frequency * self.x + self.phase)
        self.curve.setData(self.x, self.y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = DigitalOscilloscopeWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())