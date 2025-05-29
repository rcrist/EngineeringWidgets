from PyQt6.QtWidgets import *
class BaseWidget(QWidget):
    """
    Base template for scientific/engineering widgets.
    Inherit from this class and add your custom UI and logic.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.title_label = QLabel("Widget Title")
        layout.addWidget(self.title_label)
        # Add more UI elements here

        self.setLayout(layout)

    def set_title(self, title: str):
        self.title_label.setText(title)