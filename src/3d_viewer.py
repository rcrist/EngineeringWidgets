import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel
import pyqtgraph.opengl as gl
import numpy as np
from template import BaseWidget

class ModelViewerWidget(BaseWidget):
    """
    3D Model Viewer Widget using pyqtgraph's OpenGL module.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("3D Model Viewer")
        self.init_model_viewer()

    def init_model_viewer(self):
        # 3D view widget
        self.gl_view = gl.GLViewWidget()
        self.layout().addWidget(self.gl_view)

        # Example: Add a 3D surface
        x = np.linspace(-10, 10, 50)
        y = np.linspace(-10, 10, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(0.2 * X) * np.cos(0.2 * Y)

        # Create a surface plot
        surface = gl.GLSurfacePlotItem(x=x, y=y, z=Z, shader='shaded', color=(0.2, 0.5, 1, 1))
        surface.scale(1, 1, 2)
        self.gl_view.addItem(surface)

        # Optional: Add grid
        grid = gl.GLGridItem()
        grid.scale(2, 2, 1)
        self.gl_view.addItem(grid)

        # Example controls (expand as needed)
        control_layout = QHBoxLayout()
        self.reset_btn = QPushButton("Reset View")
        control_layout.addWidget(self.reset_btn)
        self.layout().addLayout(control_layout)
        self.reset_btn.clicked.connect(self.reset_view)

    def reset_view(self):
        self.gl_view.opts['azimuth'] = 0
        self.gl_view.opts['elevation'] = 90
        self.gl_view.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = ModelViewerWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())