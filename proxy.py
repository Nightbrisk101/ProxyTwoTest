import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Proxy Browser")
        self.resize(800, 600)

        self.is_dark_mode = False  # Track theme state

        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.google.com"))

        self.url_bar = QLineEdit()

        # Buttons
        self.enter_button = QPushButton("Enter")
        self.enter_button.clicked.connect(self.navigate_to_url)

        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.go_home)

        self.theme_button = QPushButton("Dark Mode")
        self.theme_button.clicked.connect(self.toggle_theme)

        # Allow pressing Enter in URL bar
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Layout for URL bar and control buttons
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.url_bar)
        top_layout.addWidget(self.enter_button)
        top_layout.addWidget(self.home_button)
        top_layout.addWidget(self.theme_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.webview)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Apply initial theme
        self.apply_theme()

    def navigate_to_url(self):
        url_text = self.url_bar.text()
        if not url_text.startswith(('http://', 'https://')):
            url_text = 'http://' + url_text
        self.webview.load(QUrl(url_text))

    def go_home(self):
        self.webview.load(QUrl("https://www.google.com"))
        self.url_bar.setText("https://www.google.com")

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            # Dark theme stylesheet
            dark_style = """
                QMainWindow {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QLineEdit {
                    background-color: #3c3c3c;
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #555555;
                    color: #ffffff;
                }
                QWebEngineView {
                    background-color: #2b2b2b;
                }
            """
            self.theme_button.setText("Light Mode")
        else:
            # Light theme (default)
            dark_style = ""
            self.theme_button.setText("Dark Mode")
        self.setStyleSheet(dark_style)

if __name__ == "__main__":
    window = Browser()
    window.show()
    sys.exit(app.exec_())