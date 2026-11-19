from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap
import webbrowser

class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        

        self.my_name = QLabel('My name is: Nof Safiah', self)
        self.my_name.setGeometry(20,20,300,30)

        self.my_email = QLabel('My email is: Nofsafiah@gmail.com', self)
        self.my_email.setGeometry(20,50,400,30)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(20,60,300,300)

        # יצירת תמונה של קבוצה אהובה בתוך המחלקה
        self.btn_football = QPushButton("My football team is", self)
        self.btn_football.setGeometry(20, 100, 300, 35)
        self.btn_football.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.btn_football.clicked.connect(self.open_manu)

    
        # יצירת כפתור הלינקדאין בתוך המחלקה
        self.btn_linkedin = QPushButton("LinkedIn", self)
        self.btn_linkedin.setGeometry(20, 320, 120, 35)
        self.btn_linkedin.setStyleSheet("background-color:blue ; color: white; font-weight: bold;")
        self.btn_linkedin.clicked.connect(self.open_linkedin)

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/nof-safiae/")

    def open_manu(self):
            self.image_manu = QLabel(self)
            self.image_manu.setGeometry(20, 150, 150, 150)
            image = QPixmap('ManchesterUnited.webp').scaled(150,150)      
            self.image_manu.setPixmap(image)
            self.image_manu.show()

             


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()