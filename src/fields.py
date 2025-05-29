import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel, QSpinBox, QHBoxLayout, QPushButton
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import numpy as np
from template import BaseWidget

class VectorFieldVisualizerWidget(BaseWidget):
    """
    Vector Field Visualizer Widget for displaying 2D vector fields.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Vector Field Visualizer")
        self.init_vector_field()

    def init_vector_field(self):
        # Plot widget
        self.plot_widget = pg.PlotWidget(title="Vector Field")
        self.layout().addWidget(self.plot_widget)

        # Controls for grid density
        control_layout = QHBoxLayout()
        density_label = QLabel("Grid Density:")
        self.density_spin = QSpinBox()
        self.density_spin.setRange(5, 30)
        self.density_spin.setValue(15)
        update_btn = QPushButton("Update Field")
        control_layout.addWidget(density_label)
        control_layout.addWidget(self.density_spin)
        control_layout.addWidget(update_btn)
        self.layout().addLayout(control_layout)

        update_btn.clicked.connect(self.update_field)
        self.density_spin.valueChanged.connect(self.update_field)

        # Initial field
        self.quiver = None
        self.update_field()

    def update_field(self):
        density = self.density_spin.value()
        x = np.linspace(-5, 5, density)
        y = np.linspace(-5, 5, density)
        X, Y = np.meshgrid(x, y)

        # Example vector field: circular (vortex)
        U = -Y
        V = X

        self.plot_widget.clear()

        # Draw arrows as lines
        scale = 0.3  # Arrow length scaling
        for xi, yi, ui, vi in zip(X.ravel(), Y.ravel(), U.ravel(), V.ravel()):
            x_end = xi + scale * ui
            y_end = yi + scale * vi
            self.plot_widget.plot([xi, x_end], [yi, y_end], pen=pg.mkPen('b', width=2))

        self.plot_widget.setAspectLocked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = VectorFieldVisualizerWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())