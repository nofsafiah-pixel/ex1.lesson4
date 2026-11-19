from collections.abc import Iterable, Sequence
from pathlib import Path

from about import AboutWindow
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class GradeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("מערכת ציונים")
        self.setMinimumSize(900, 820)
        self.about_window = AboutWindow()

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
        self.about_button.clicked.connect(self.open_about)
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

        stylesheet_path = Path(__file__).with_name("grade_app.qss")
        self.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    def update_table(self, rows: Iterable[Sequence[object]]) -> None:
        rows = list(rows)
        if len(rows) > self.grades_table.rowCount():
            raise ValueError("Too many rows for the grades table.")
        if any(len(row) != self.grades_table.columnCount() for row in rows):
            raise ValueError("Each row must contain an ID and two grade values.")

        self.grades_table.clearContents()
        for row_index, values in enumerate(rows):
            for column_index, value in enumerate(values):
                self.grades_table.setItem(
                    row_index, column_index, QTableWidgetItem(str(value))
                )

    def open_about(self) -> None:
        self.about_window.show()
        self.about_window.raise_()
        self.about_window.activateWindow()

    def auto_open_file(self, file_path: str) -> bool:
        return QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))


if __name__ == "__main__":
    app = QApplication()
    window = GradeWindow()
    window.show()
    app.exec()
