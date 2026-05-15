import re
from urllib.parse import urlparse

class Analyzer:

    def extract_urls(self, text):
        return re.findall(r'https?://\S+', text)

    def analyze_domain(self, url):
        domain = urlparse(url).netloc

        score = 0
        reasons = []

        if len(domain) > 25:
            score += 20
            reasons.append("Dominio molto lungo")

        if "-" in domain:
            score += 10
            reasons.append("Caratteri sospetti nel dominio")

        if any(tld in domain for tld in [".xyz", ".top", ".click", ".info"]):
            score += 30
            reasons.append("TLD poco affidabile")

        return domain, score, reasons

    def compute_risk(self, total_score):
        if total_score < 20:
            return "Basso"
        elif total_score < 50:
            return "Medio"
        else:
            return "Alto"
