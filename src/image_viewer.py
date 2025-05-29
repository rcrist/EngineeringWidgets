import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QFileDialog
from PyQt6.QtGui import QPixmap
from template import BaseWidget

class ImageViewerWidget(BaseWidget):
    """
    Image Viewer Widget for displaying images.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Image Viewer")
        self.init_image_viewer()

    def init_image_viewer(self):
        # Image display label
        self.image_label = QLabel("No image loaded")
        self.image_label.setScaledContents(True)
        self.layout().addWidget(self.image_label)

        # Controls
        control_layout = QHBoxLayout()
        self.open_btn = QPushButton("Open Image")
        control_layout.addWidget(self.open_btn)
        self.layout().addLayout(control_layout)

        self.open_btn.clicked.connect(self.open_image)

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp *.gif)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = ImageViewerWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())