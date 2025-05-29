import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel, QComboBox, QLineEdit, QHBoxLayout, QPushButton
from template import BaseWidget

class UnitConverterWidget(BaseWidget):
    """
    Unit Converter Widget for converting between common units.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Unit Converter")
        self.init_unit_converter()

    def init_unit_converter(self):
        # Supported units for length
        self.units = {
            "Meters": 1.0,
            "Kilometers": 1000.0,
            "Miles": 1609.34,
            "Feet": 0.3048
        }

        layout = QHBoxLayout()
        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("Enter value")
        self.from_combo = QComboBox()
        self.from_combo.addItems(self.units.keys())
        self.to_combo = QComboBox()
        self.to_combo.addItems(self.units.keys())
        self.convert_btn = QPushButton("Convert")
        self.result_label = QLabel("Result: ")

        layout.addWidget(self.input_edit)
        layout.addWidget(self.from_combo)
        layout.addWidget(QLabel("to"))
        layout.addWidget(self.to_combo)
        layout.addWidget(self.convert_btn)
        layout.addWidget(self.result_label)
        self.layout().addLayout(layout)

        self.convert_btn.clicked.connect(self.convert_units)

    def convert_units(self):
        try:
            value = float(self.input_edit.text())
            from_unit = self.from_combo.currentText()
            to_unit = self.to_combo.currentText()
            # Convert to base (meters), then to target
            value_in_meters = value * self.units[from_unit]
            converted = value_in_meters / self.units[to_unit]
            self.result_label.setText(f"Result: {converted:.4f} {to_unit}")
        except Exception:
            self.result_label.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = UnitConverterWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())