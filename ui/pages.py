from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QFrame
)
from PySide6.QtCore import Qt, QTimer, QDateTime
import random


# ===========================
# DASHBOARD PAGE
# ===========================
class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        # --- THREAT LEVEL ---
        threat_box = QFrame()
        threat_box.setObjectName("statsBox")
        threat_layout = QVBoxLayout(threat_box)

        threat_title = QLabel("🔥 Threat Level")
        threat_title.setObjectName("statusTitle")
        threat_layout.addWidget(threat_title)

        self.threat_label = QLabel("LOW")
        self.threat_label.setObjectName("threatLabel")
        threat_layout.addWidget(self.threat_label)

        layout.addWidget(threat_box)

        # Timer animazione threat level
        self.threat_timer = QTimer()
        self.threat_timer.timeout.connect(self.update_threat)
        self.threat_timer.start(3000)

        # --- GRAFICO ASCII MIGLIORATO ---
        ascii_box = QFrame()
        ascii_box.setObjectName("statsBox")
        ascii_layout = QVBoxLayout(ascii_box)

        ascii_title = QLabel("📊 Attività Ultimi 7 Giorni (ASCII Graph)")
        ascii_title.setObjectName("statusTitle")
        ascii_layout.addWidget(ascii_title)

        self.ascii_graph = QTextEdit()
        self.ascii_graph.setReadOnly(True)
        self.ascii_graph.setObjectName("terminalBox")
        ascii_layout.addWidget(self.ascii_graph)

        layout.addWidget(ascii_box)

        self.update_ascii_graph()

        # --- THREAT MAP ASCII ---
        threatmap_box = QFrame()
        threatmap_box.setObjectName("statsBox")
        threatmap_layout = QVBoxLayout(threatmap_box)

        threatmap_title = QLabel("🌍 Threat Map (ASCII)")
        threatmap_title.setObjectName("statusTitle")
        threatmap_layout.addWidget(threatmap_title)

        self.threatmap_text = QTextEdit()
        self.threatmap_text.setReadOnly(True)
        self.threatmap_text.setObjectName("terminalBox")
        threatmap_layout.addWidget(self.threatmap_text)

        layout.addWidget(threatmap_box)

        self.threatmap_timer = QTimer()
        self.threatmap_timer.timeout.connect(self.update_threatmap)
        self.threatmap_timer.start(4000)
        self.update_threatmap()

        # --- SYSTEM PERFORMANCE ---
        perf_box = QFrame()
        perf_box.setObjectName("statsBox")
        perf_layout = QVBoxLayout(perf_box)

        perf_title = QLabel("📈 System Performance")
        perf_title.setObjectName("statusTitle")
        perf_layout.addWidget(perf_title)

        self.perf_label = QLabel("CPU: 12% | RAM: 43% | DISK: 18%")
        perf_layout.addWidget(self.perf_label)

        layout.addWidget(perf_box)

        self.perf_timer = QTimer()
        self.perf_timer.timeout.connect(self.update_performance)
        self.perf_timer.start(5000)

        layout.addStretch()

    # ===== FUNZIONI DASHBOARD =====

    def update_threat(self):
        levels = ["LOW", "MEDIUM", "HIGH"]
        level = random.choice(levels)
        self.threat_label.setText(level)

    def update_ascii_graph(self):
        data = [random.randint(1, 10) for _ in range(7)]
        days = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

        graph = "ATTIVITÀ SETTIMANALE\n\n"
        max_len = max(data)

        for i in range(7):
            bar = "█" * data[i]
            spaces = " " * (max_len - data[i])
            graph += f"{days[i]} | {bar}{spaces} ({data[i]})\n"

        self.ascii_graph.setText(graph)

    def update_threatmap(self):
        ips = [
            "192.168.0.10",
            "10.0.5.23",
            "172.16.4.8",
            "185.23.44.12",
            "91.200.12.55",
            "37.14.88.201",
        ]
        levels = ["LOW", "MEDIUM", "HIGH"]
        text = ""

        for ip in ips:
            lvl = random.choice(levels)
            text += f"{ip}  ->  RISK: {lvl}\n"

        self.threatmap_text.setText(text)

    def update_performance(self):
        cpu = random.randint(5, 60)
        ram = random.randint(20, 80)
        disk = random.randint(5, 50)
        self.perf_label.setText(f"CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")


# ===========================
# ANALYZE PAGE (con caricamento email)
# ===========================
class AnalyzePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Analisi Email")
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        # --- Pulsante per caricare file ---
        self.load_button = QPushButton("Carica Email (.txt / .eml)")
        self.load_button.setObjectName("analyzeButton")
        layout.addWidget(self.load_button)

        # --- Box input email ---
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Incolla qui l'email oppure caricala da file...")
        layout.addWidget(self.input_box)

        # --- Pulsante analisi ---
        self.analyze_button = QPushButton("Esegui Analisi")
        self.analyze_button.setObjectName("analyzeButton")
        layout.addWidget(self.analyze_button)

        # --- Output ---
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        # === Collegamento pulsante carica file ===
        self.load_button.clicked.connect(self.load_email_file)

    def load_email_file(self):
        from PySide6.QtWidgets import QFileDialog

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleziona un file email",
            "",
            "Email Files (*.txt *.eml);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    self.input_box.setText(content)
            except Exception as e:
                self.input_box.setText(f"Errore nel caricamento del file:\n{e}")


# ===========================
# TERMINALE HACKER + FULL HACKER MODE
# ===========================
class LogsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Terminale Hacker")
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setObjectName("terminalBox")
        layout.addWidget(self.log_box)

        # Pulsante Full Hacker Mode
        self.full_mode_button = QPushButton("Attiva Full Hacker Mode")
        self.full_mode_button.setObjectName("analyzeButton")
        layout.addWidget(self.full_mode_button)

        self.full_hacker_mode = False
        self.full_mode_button.clicked.connect(self.toggle_full_hacker_mode)

        self.timer = QTimer()
        self.timer.timeout.connect(self.add_terminal_line)
        self.timer.start(1500)

    def toggle_full_hacker_mode(self):
        self.full_hacker_mode = not self.full_hacker_mode
        if self.full_hacker_mode:
            self.full_mode_button.setText("Disattiva Full Hacker Mode")
            self.log_box.append("=== FULL HACKER MODE ATTIVATA ===")
            self.timer.setInterval(600)
        else:
            self.full_mode_button.setText("Attiva Full Hacker Mode")
            self.log_box.append("=== FULL HACKER MODE DISATTIVATA ===")
            self.timer.setInterval(1500)

    def add_terminal_line(self):
        timestamp = QDateTime.currentDateTime().toString("hh:mm:ss")
        fake_lines = [
            "Scanning network...",
            "Decrypting payload...",
            "Analyzing headers...",
            "Checking domain reputation...",
            "Running heuristics...",
            "Threat signature updated.",
            "No anomalies detected.",
            "Packet inspection running...",
            "Firewall rules validated.",
            "Suspicious pattern not found.",
            "Bruteforce protection active...",
            "Sandbox environment clean.",
        ]
        line = random.choice(fake_lines)
        self.log_box.append(f"[{timestamp}] {line}")


# ===========================
# INFO PAGE (VERSIONE COMPLETA)
# ===========================
class InfoPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Informazioni sul Tool")
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        # --- INFO GENERALI ---
        info_box = QFrame()
        info_box.setObjectName("statsBox")
        info_layout = QVBoxLayout(info_box)

        info_layout.addWidget(QLabel("🟢 Nome Tool: Phishing Analyzer – Matrix Edition"))
        info_layout.addWidget(QLabel("🟢 Versione: 2.0.0"))
        info_layout.addWidget(QLabel("🟢 Autore: Joele"))
        info_layout.addWidget(QLabel("🟢 Framework: PySide6 (Python 3.14)"))
        info_layout.addWidget(QLabel("🟢 Tema: Matrix Green UI"))
        info_layout.addWidget(QLabel("🟢 Modalità: Desktop App"))
        info_layout.addWidget(QLabel("🟢 Compatibilità: Windows 10/11"))

        layout.addWidget(info_box)

        # --- MODULI ---
        modules_box = QFrame()
        modules_box.setObjectName("statsBox")
        modules_layout = QVBoxLayout(modules_box)

        modules_title = QLabel("📦 Moduli Caricati")
        modules_title.setObjectName("statusTitle")
        modules_layout.addWidget(modules_title)

        modules_layout.addWidget(QLabel("• UI Engine: PySide6"))
        modules_layout.addWidget(QLabel("• Analyzer Engine: Custom Python Logic"))
        modules_layout.addWidget(QLabel("• ASCII Graph Engine: Custom Renderer"))
        modules_layout.addWidget(QLabel("• Terminal Engine: Randomized Stream Generator"))
        modules_layout.addWidget(QLabel("• Threat Level Engine: Randomized Heuristic"))
        modules_layout.addWidget(QLabel("• Background Engine: Matrix GIF + Overlay"))

        layout.addWidget(modules_box)

        # --- SISTEMA ---
        system_box = QFrame()
        system_box.setObjectName("statsBox")
        system_layout = QVBoxLayout(system_box)

        system_title = QLabel("🖥 Stato Sistema")
        system_title.setObjectName("statusTitle")
        system_layout.addWidget(system_title)

        system_layout.addWidget(QLabel("• Sistema operativo: Windows 10"))
        system_layout.addWidget(QLabel("• Architettura: 64-bit"))
        system_layout.addWidget(QLabel("• Python: 3.14"))
        system_layout.addWidget(QLabel("• RAM: OK"))
        system_layout.addWidget(QLabel("• CPU: OK"))
        system_layout.addWidget(QLabel("• Disco: OK"))

        layout.addWidget(system_box)

        # --- CHANGELOG ---
        changelog_box = QFrame()
        changelog_box.setObjectName("statsBox")
        changelog_layout = QVBoxLayout(changelog_box)

        changelog_title = QLabel("📝 Changelog")
        changelog_title.setObjectName("statusTitle")
        changelog_layout.addWidget(changelog_title)

        changelog_layout.addWidget(QLabel("• v2.0.0 – Dashboard SOC completa"))
        changelog_layout.addWidget(QLabel("• v2.0.0 – Terminale Hacker animato"))
        changelog_layout.addWidget(QLabel("• v2.0.0 – Threat Level animato"))
        changelog_layout.addWidget(QLabel("• v2.0.0 – Grafici ASCII Matrix"))
        changelog_layout.addWidget(QLabel("• v2.0.0 – Overlay sfondo Matrix"))
        changelog_layout.addWidget(QLabel("• v1.0.0 – Prima versione"))

        layout.addWidget(changelog_box)

        layout.addStretch()
