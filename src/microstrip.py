import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel, QDoubleSpinBox, QHBoxLayout, QPushButton
from template import BaseWidget
import numpy as np

class MicrostripCalculatorWidget(BaseWidget):
    """
    Microstrip Calculator Widget for characteristic impedance and effective dielectric constant.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_title("Microstrip Calculator")
        self.init_microstrip_calculator()

    def init_microstrip_calculator(self):
        # Controls for W, H, Er
        control_layout = QHBoxLayout()
        w_label = QLabel("Width (W, mm):")
        self.w_spin = QDoubleSpinBox()
        self.w_spin.setRange(0.01, 100.0)
        self.w_spin.setValue(2.0)
        self.w_spin.setDecimals(3)

        h_label = QLabel("Height (H, mm):")
        self.h_spin = QDoubleSpinBox()
        self.h_spin.setRange(0.01, 10.0)
        self.h_spin.setValue(1.0)
        self.h_spin.setDecimals(3)

        er_label = QLabel("Dielectric (εr):")
        self.er_spin = QDoubleSpinBox()
        self.er_spin.setRange(1.0, 20.0)
        self.er_spin.setValue(4.4)
        self.er_spin.setDecimals(3)

        self.calc_btn = QPushButton("Calculate")
        self.result_label = QLabel("Z₀: -- Ω, ε_eff: --")

        control_layout.addWidget(w_label)
        control_layout.addWidget(self.w_spin)
        control_layout.addWidget(h_label)
        control_layout.addWidget(self.h_spin)
        control_layout.addWidget(er_label)
        control_layout.addWidget(self.er_spin)
        control_layout.addWidget(self.calc_btn)
        self.layout().addLayout(control_layout)
        self.layout().addWidget(self.result_label)

        self.calc_btn.clicked.connect(self.calculate)

    def calculate(self):
        W = self.w_spin.value()
        H = self.h_spin.value()
        Er = self.er_spin.value()
        w_h = W / H

        # Effective dielectric constant (Hammerstad and Jensen)
        e_eff = (Er + 1) / 2 + (Er - 1) / 2 * (1 / np.sqrt(1 + 12 * H / W))
        # Characteristic impedance (Z0)
        if w_h <= 1:
            Z0 = (60 / np.sqrt(e_eff)) * np.log(8 * H / W + 0.25 * W / H)
        else:
            Z0 = (120 * np.pi) / (np.sqrt(e_eff) * (w_h + 1.393 + 0.667 * np.log(w_h + 1.444)))

        self.result_label.setText(f"Z₀: {Z0:.2f} Ω, ε_eff: {e_eff:.3f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    osc_widget = MicrostripCalculatorWidget()
    osc_widget.resize(800, 400)
    osc_widget.show()
    sys.exit(app.exec())