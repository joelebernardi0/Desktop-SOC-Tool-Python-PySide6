# 🟩 PHISHING ANALYZER – MATRIX EDITION
### _Advanced SOC Desktop Tool – Python 3.14 + PySide6_

---

## 🟢 Overview

Phishing Analyzer – Matrix Edition è un’applicazione desktop progettata per simulare un ambiente SOC (Security Operations Center) e fornire strumenti rapidi per:

- Analizzare email sospette  
- Identificare URL malevoli  
- Valutare il rischio complessivo  
- Visualizzare indicatori di sicurezza in tempo reale  
- Allenarsi nella detection e nell’analisi  

Il tutto con un’interfaccia **Matrix Green UI**, animazioni, overlay e componenti ASCII che richiamano l’estetica cyberpunk.

---

## 🟢 Features

### 🔥 Dashboard SOC
- Threat Level animato (LOW / MEDIUM / HIGH)  
- Grafico ASCII settimanale  
- Threat Map ASCII  
- System Performance (CPU / RAM / Disk)  
- Overlay Matrix con trasparenza regolata  

---

### 🔥 Email Analyzer
- Caricamento email da file `.txt` o `.eml`  
- Parsing del contenuto  
- Estrazione URL  
- Analisi dominio  
- Punteggio rischio  
- Output strutturato  

---

### 🔥 Hacker Terminal
- Log animati in tempo reale  
- Output dinamico stile SOC  
- Modalità **Full Hacker Mode**  
- Effetto “console verde”  

---

### 🔥 Info Tool
- Dettagli tecnici del software  
- Moduli caricati  
- Stato sistema  
- Changelog  
- Informazioni su autore e versione  

---

## 🟢 Project Structure


PhishingAnalyzer-MatrixEdition/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── main.py
│   ├── logic/
│   │   └── analyzer.py
│   └── ui/
│       ├── main_window.py
│       ├── pages.py
│       └── style.qss
│
├── assets/
│   ├── matrix.gif
│   └── screenshots/
│       ├── dashboard.png
│       ├── analyze.png
│       ├── logs.png
│       └── info.png
│
└── docs/
├── architecture.md
├── threat-model.md
└── changelog.md


---

## 🟢 Requirements
Python 3.14
PySide6


---

## 🟢 Run

```cmd
cd src
python main.py
```

🟢 Analyzer Engine
Il motore di analisi implementa:

Estrazione URL tramite regex

Normalizzazione dominio

Heuristics scoring

Rischio finale (LOW / MEDIUM / HIGH)

Output strutturato
🟢 Documentation
architecture.md
Struttura del software

UI Layer

Logic Layer

Rendering ASCII

Background Engine

threat-model.md
Input email

URL extraction

Domain scoring

Risk classification

changelog.md
Storico versioni

Feature aggiunte

Fix

🟢 Threat Model (Sintesi)
Componente	Rischio	Mitigazione
Input email	Possibile contenuto malevolo	Parsing testuale, nessuna esecuzione
URL	Phishing / spoofing	Domain scoring + heuristics
UI	Nessun rischio	Sandbox locale
File loader	File non fidati	Apertura in sola lettura


🟢 License
MIT License

🟢 Author
Joele  
Cybersecurity Student & SOC Analyst Trainee
Italia 🇮🇹

🟢 Purpose
Questo progetto è stato sviluppato per:

Portfolio professionale

Training SOC

Studio della detection

Simulazione di un ambiente operativo

Dimostrazione di competenze Python + UI + Cybersecurity

🟢 Notes
Nessuna libreria esterna oltre PySide6

Compatibile con Python 3.14

Nessuna dipendenza complessa (no NumPy, no Matplotlib)

UI completamente customizzata

🟢 Comando di avvio
cd src
python main.py

---






