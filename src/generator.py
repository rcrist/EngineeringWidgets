import sys
from PyQt6.QtWidgets import QLabel, QSpinBox, QHBoxLayout, QPushButton, QComboBox
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
from PyQt6.QtCore import QTimer
from template import BaseWidget

class SignalGeneratorWidget(BaseWidget):
    """
    Signal Generator Widget for generating and visualizing basic waveforms.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Signal Generator")
        self.init_signal_generator()

    def init_signal_generator(self):
        # Plot widget
        self.plot_widget = pg.PlotWidget(title="Signal Output")
        self.layout().addWidget(self.plot_widget)

        # Controls: waveform, frequency, amplitude
        control_layout = QHBoxLayout()
        wave_label = QLabel("Waveform:")
        self.wave_combo = QComboBox()
        self.wave_combo.addItems(["Sine", "Square", "Triangle"])
        freq_label = QLabel("Frequency (Hz):")
        self.freq_spin = QSpinBox()
        self.freq_spin.setRange(1, 100)
        self.freq_spin.setValue(5)
        amp_label = QLabel("Amplitude:")
        self.amp_spin = QSpinBox()
        self.amp_spin.setRange(1, 10)
        self.amp_spin.setValue(1)
        control_layout.addWidget(wave_label)
        control_layout.addWidget(self.wave_combo)
        control_layout.addWidget(freq_label)
        control_layout.addWidget(self.freq_spin)
        control_layout.addWidget(amp_label)
        control_layout.addWidget(self.amp_spin)
        self.layout().addLayout(control_layout)

        # Start/Stop buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        self.layout().addLayout(btn_layout)

        # Signal data
        self.x = np.linspace(0, 1, 1000)
        self.y = np.zeros(1000)
        self.curve = self.plot_widget.plot(self.x, self.y, pen='c')

        # Timer for updating plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        # Connect controls
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.wave_combo.currentIndexChanged.connect(self.update_params)
        self.freq_spin.valueChanged.connect(self.update_params)
        self.amp_spin.valueChanged.connect(self.update_params)

        self.phase = 0
        self.waveform = self.wave_combo.currentText()
        self.frequency = self.freq_spin.value()
        self.amplitude = self.amp_spin.value()

    def start(self):
        self.timer.start(30)

    def stop(self):
        self.timer.stop()

    def update_params(self):
        self.waveform = self.wave_combo.currentText()
        self.frequency = self.freq_spin.value()
        self.amplitude = self.amp_spin.value()

    def update_plot(self):
        self.phase += 0.1
        if self.waveform == "Sine":
            self.y = self.amplitude * np.sin(2 * np.pi * self.frequency * self.x + self.phase)
        elif self.waveform == "Square":
            self.y = self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * self.x + self.phase))
        elif self.waveform == "Triangle":
            self.y = self.amplitude * (2 * np.abs(2 * ((self.frequency * self.x + self.phase/(2*np.pi)) % 1) - 1) - 1)
        else:
            self.y = np.zeros_like(self.x)
        self.curve.setData(self.x, self.y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = SignalGeneratorWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())