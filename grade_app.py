from pathlib import Path

from about import AboutWindow
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFormLayout,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class GradeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.setWindowTitle("מערכת ציונים")
        self.setMinimumSize(820, 680)
        self.resize(860, 720)
        self.about_window = AboutWindow()

        title = QLabel("ניהול ציונים")
        title.setObjectName("title")

        self.grade_correction_input = QSpinBox()
        self.grade_correction_input.editingFinished.connect(
            self.handle_correction_input
        )

        self.selected_file_display = QLineEdit()
        self.selected_file_display.setReadOnly(True)
        self.load_file_button = QPushButton("Load File")
        self.load_file_button.clicked.connect(self.load_file)

        file_controls = QHBoxLayout()
        file_controls.addWidget(self.selected_file_display, 1)
        file_controls.addWidget(self.load_file_button)

        form = QFormLayout()
        form.setSpacing(8)
        form.addRow("נקודות בונוס / תיקון:", self.grade_correction_input)
        form.addRow("קובץ ציונים:", file_controls)

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
        self.update_file_button.clicked.connect(self.update_file)
        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.open_about)
        buttons = QHBoxLayout()
        buttons.addWidget(self.update_file_button)
        buttons.addWidget(self.about_button)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)
        layout.addWidget(title)
        layout.addLayout(form)
        layout.addWidget(table_label)
        layout.addWidget(self.grades_table, 1)
        layout.addLayout(buttons)

        stylesheet_path = Path(__file__).with_name("grade_app.qss")
        self.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    def update_table(self) -> None:
        columns = (
            self.student_ids,
            self.original_grades,
            self.corrected_grades,
        )
        if any(len(values) > self.grades_table.rowCount() for values in columns):
            raise ValueError("The table can display at most 50 students.")
        self.grades_table.clearContents()
        for column_index, values in enumerate(columns):
            for row_index, value in enumerate(values):
                self.grades_table.setItem(
                    row_index, column_index, QTableWidgetItem(str(value))
                )

    def load_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "בחרו קובץ ציונים",
            "",
            "CSV files (*.csv);;All files (*)",
        )
        if file_path:
            self.selected_file = file_path
            self.selected_file_display.setText(file_path)
            self.selected_file_display.setToolTip(file_path)

    def handle_correction_input(self) -> None:
        self.grade_correction_input.interpretText()

    def update_file(self) -> None:
        """Placeholder for future file update and auto-open behavior."""
        pass

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
