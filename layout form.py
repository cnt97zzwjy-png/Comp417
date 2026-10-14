import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit, QComboBox,
    QTextEdit, QPushButton, QFormLayout, QHBoxLayout, QVBoxLayout,
)

class EquipmentRequestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("University Equipment-Request System")

        name_input = QLineEdit()
        name_input.setPlaceholderText("Requester name")
        department_combo = QComboBox()
        department_combo.addItems(["CS", "IT", "IS"])
        category_combo = QComboBox()
        category_combo.addItems(["Computer", "Monitor", "Printer"])
        quantity_input = QLineEdit()
        details_input = QTextEdit()
        details_input.setPlaceholderText("Explain why the equipment is needed")
        submit_button = QPushButton("Submit")
        clear_button = QPushButton("Clear")

        form = QFormLayout()
        form.addRow("Requester Name:", name_input)
        form.addRow("Department:", department_combo)
        form.addRow("Category:", category_combo)
        form.addRow("Quantity:", quantity_input)
        form.addRow("Description:", details_input)

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(submit_button)
        buttons.addWidget(clear_button)

        main = QVBoxLayout()
        main.addLayout(form)
        main.addLayout(buttons)

        central_widget = QWidget()
        central_widget.setLayout(main)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentRequestWindow()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec())
