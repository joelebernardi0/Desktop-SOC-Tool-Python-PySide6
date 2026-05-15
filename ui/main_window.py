from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QStackedWidget, QPushButton
)
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QTimer
import random

from ui.pages import DashboardPage, AnalyzePage, LogsPage, InfoPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Phishing Analyzer – Matrix Edition")
        self.setMinimumSize(1300, 800)

        # === SFONDO ANIMATO MATRIX ===
        self.bg = QLabel(self)
        self.bg.setScaledContents(True)
        self.bg.lower()

        movie = QMovie("assets/matrix.gif")
        self.bg.setMovie(movie)
        movie.start()

        # Overlay scuro per leggibilità
        self.overlay = QLabel(self)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.55);")
        self.overlay.lower()

        self.resizeEvent = self._resize_background

        # === LAYOUT PRINCIPALE ===
        main_layout = QVBoxLayout(self)

        # === HEADER ===
        header = QFrame()
        header.setObjectName("header")
        header_layout = QHBoxLayout(header)

        self.title_label = QLabel("☣ MATRIX PHISHING ANALYZER")
        self.title_label.setObjectName("headerTitle")
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        main_layout.addWidget(header)

        # Timer per effetto glitch sul titolo
        self.glitch_timer = QTimer()
        self.glitch_timer.timeout.connect(self._glitch_title)
        self.glitch_timer.start(800)

        # === CONTENUTO CENTRALE ===
        center_layout = QHBoxLayout()

        # === SIDEBAR ===
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout(sidebar)

        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_analyze = QPushButton("Analizza Email")
        self.btn_logs = QPushButton("Terminale Hacker")
        self.btn_info = QPushButton("Info Tool")

        for btn in [self.btn_dashboard, self.btn_analyze, self.btn_logs, self.btn_info]:
            btn.setObjectName("sidebarButton")
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        # === STACKED PAGES ===
        self.pages = QStackedWidget()
        self.dashboard_page = DashboardPage()
        self.analyze_page = AnalyzePage()
        self.logs_page = LogsPage()
        self.info_page = InfoPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.analyze_page)
        self.pages.addWidget(self.logs_page)
        self.pages.addWidget(self.info_page)

        # === COLLEGA I BOTTONI (pseudo-transizione: status dinamico) ===
        self.btn_dashboard.clicked.connect(lambda: self._switch_page(0, "Dashboard"))
        self.btn_analyze.clicked.connect(lambda: self._switch_page(1, "Analisi Email"))
        self.btn_logs.clicked.connect(lambda: self._switch_page(2, "Terminale Hacker"))
        self.btn_info.clicked.connect(lambda: self._switch_page(3, "Info Tool"))

        center_layout.addWidget(sidebar)
        center_layout.addWidget(self.pages)

        main_layout.addLayout(center_layout)

        # === FOOTER ===
        footer = QFrame()
        footer.setObjectName("footer")
        footer_layout = QHBoxLayout(footer)

        self.status_label = QLabel("Pronto")
        footer_layout.addWidget(self.status_label)

        main_layout.addWidget(footer)

    def _resize_background(self, event):
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.overlay.setGeometry(0, 0, self.width(), self.height())

    def _glitch_title(self):
        base_text = "☣ MATRIX PHISHING ANALYZER"
        chars = list(base_text)
        # Piccolo glitch random
        for _ in range(3):
            idx = random.randint(0, len(chars) - 1)
            chars[idx] = random.choice(["#", "@", "%", "&", "§", "!", "?", "X"])
        self.title_label.setText("".join(chars))

    def _switch_page(self, index, name):
        self.pages.setCurrentIndex(index)
        self.status_label.setText(f"Pagina attiva: {name}")
