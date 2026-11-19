from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QWidget


class GradeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("מערכת ציונים")
        self.setMinimumWidth(420)

        title = QLabel("פרטי תלמיד")
        title.setObjectName("title")

        self.student_id_input = QLineEdit()
        self.student_id_input.setPlaceholderText("הקלידו מספר זהות")

        self.grade_output = QLineEdit()
        self.grade_output.setReadOnly(True)

        self.status_output = QLineEdit()
        self.status_output.setReadOnly(True)

        form = QFormLayout()
        form.setSpacing(12)
        form.addRow("מספר זהות:", self.student_id_input)
        form.addRow("ציון:", self.grade_output)
        form.addRow("מצב:", self.status_output)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)
        layout.addWidget(title)
        layout.addLayout(form)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #ffffff;
                color: #263238;
                font-family: "Segoe UI";
                font-size: 14px;
            }
            QLabel#title {
                color: #1f4e79;
                font-size: 22px;
                font-weight: 600;
            }
            QLineEdit {
                min-height: 34px;
                padding: 4px 8px;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                background-color: #ffffff;
            }
            QLineEdit:read-only {
                background-color: lightgray;
                color: #495057;
            }
            """
        )


if __name__ == "__main__":
    app = QApplication()
    window = GradeWindow()
    window.show()
    app.exec()
