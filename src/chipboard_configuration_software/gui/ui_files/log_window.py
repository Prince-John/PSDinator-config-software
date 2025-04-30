from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTextEdit


class FailureDetailsDialog(QDialog):
    def __init__(self, failure_list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration Failures")

        layout = QVBoxLayout()

        # Text box to show all failures
        failure_text = QTextEdit()
        failure_text.setReadOnly(True)

        # Build the detailed log
        if failure_list:
            detailed_log = "\n".join(
                f"Command '{cmd}': {reason}" for cmd, reason in failure_list
            )
        else:
            detailed_log = "No failures recorded."

        failure_text.setPlainText(detailed_log)
        layout.addWidget(failure_text)

        # OK button
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)
