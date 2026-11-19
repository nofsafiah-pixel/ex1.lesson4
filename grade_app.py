from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class GradeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("מערכת ציונים")
        self.setMinimumSize(900, 820)

        title = QLabel("פרטי תלמיד")
        title.setObjectName("title")

        self.student_id_input = QLineEdit()
        self.student_id_input.setPlaceholderText("הקלידו מספר זהות")

        self.grade_output = QLineEdit()
        self.grade_output.setReadOnly(True)

        self.status_output = QLineEdit()
        self.status_output.setReadOnly(True)

        self.grade_correction_input = QLineEdit()

        form = QFormLayout()
        form.setSpacing(12)
        form.addRow("מספר זהות:", self.student_id_input)
        form.addRow("ציון:", self.grade_output)
        form.addRow("מצב:", self.status_output)
        form.addRow("ציון מתוקן:", self.grade_correction_input)

        table_label = QLabel("רשימת ציונים")
        self.grades_table = QTableWidget(50, 3)
        self.grades_table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.grades_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        header = self.grades_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.grades_table.setColumnWidth(0, 130)
        self.grades_table.setMinimumHeight(360)

        self.update_file_button = QPushButton("Update File")
        self.about_button = QPushButton("About")
        buttons = QHBoxLayout()
        buttons.addWidget(self.update_file_button)
        buttons.addWidget(self.about_button)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)
        layout.addWidget(title)
        layout.addLayout(form)
        layout.addWidget(table_label)
        layout.addWidget(self.grades_table, 1)
        layout.addLayout(buttons)

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
            QHeaderView::section {
                background-color: #e8eef4;
                color: #263238;
                font-weight: 600;
                padding: 6px;
                border: 1px solid #cbd5e1;
            }
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f7f9fb;
                gridline-color: #d8dee5;
                border: 1px solid #cbd5e1;
                selection-background-color: #dbeafe;
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
            QPushButton {
                min-height: 36px;
                padding: 4px 14px;
                border: none;
                border-radius: 6px;
                background-color: #1f4e79;
                color: #ffffff;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #286292;
            }
            """
        )


if __name__ == "__main__":
    app = QApplication()
    window = GradeWindow()
    window.show()
    app.exec()
