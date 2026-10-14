import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QComboBox, QPushButton, QMessageBox, QFormLayout,
)

class EquipmentRequestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("University Equipment-Request System")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Requester name")

        self.category_combo = QComboBox()
        self.category_combo.addItems(["Computer", "Monitor", "Printer"])

        self.submit_button = QPushButton("Submit Request")

        form = QFormLayout()
        form.addRow("Name:", self.name_input)
        form.addRow("Category:", self.category_combo)
        form.addRow(self.submit_button)

        central_widget = QWidget()
        central_widget.setLayout(form)
        self.setCentralWidget(central_widget)

        # register the event handler: connect the clicked signal to the slot
        self.submit_button.clicked.connect(self.submit_request)

    def submit_request(self):
        # read the requester name
        name = self.name_input.text().strip()
        # check that the requester name is not empty
        if not name:
            QMessageBox.warning(self, "Missing Data",
                                "Enter requester name.")
            return
        # read the equipment category
        category = self.category_combo.currentText()
        # display an appropriate message
        QMessageBox.information(
            self, "Request Submitted",
            f"{name}'s {category} request was submitted.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentRequestWindow()
    window.show()
    sys.exit(app.exec())
