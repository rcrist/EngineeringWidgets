import sys
from PyQt6.QtWidgets import QApplication
from generator import SignalGeneratorWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = SignalGeneratorWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())