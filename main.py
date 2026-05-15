import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from logic.analyzer import Analyzer

def run():
    app = QApplication(sys.argv)

    with open("ui/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    analyzer = Analyzer()

    analyze_page = window.analyze_page

    def on_analyze():
        text = analyze_page.input_box.toPlainText()
        analyze_page.output_box.clear()

        urls = analyzer.extract_urls(text)
        total_score = 0

        if urls:
            analyze_page.output_box.append("🟢 URL trovati:\n")
            for url in urls:
                domain, score, reasons = analyzer.analyze_domain(url)
                total_score += score

                analyze_page.output_box.append(f"URL: {url}")
                analyze_page.output_box.append(f"Dominio: {domain}")
                analyze_page.output_box.append(f"Punteggio: {score}")
                if reasons:
                    analyze_page.output_box.append("Motivi:")
                    for r in reasons:
                        analyze_page.output_box.append(f" - {r}")
                analyze_page.output_box.append("")
        else:
            analyze_page.output_box.append("Nessun URL trovato.\n")

        risk = analyzer.compute_risk(total_score)
        analyze_page.output_box.append(f"🟢 Livello di rischio: {risk}")

    analyze_page.analyze_button.clicked.connect(on_analyze)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
