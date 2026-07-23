#!/usr/bin/env python3
"""Lokaler Entwicklungsserver mit Live-Reload für Fußtrack.

Start:  python3 dev-server.py          (Port 8081, Toolbox nutzt 8080)
Dann:   http://localhost:8081/fusstrack.html

Keine Abhängigkeiten (nur Python-Standardbibliothek). In ausgelieferte
HTML-Seiten wird ein kleines Polling-Skript injiziert, das jede Sekunde
/__livereload abfragt; ändert sich eine überwachte Datei (*.html, *.json,
lib/, bilder/), lädt der Browser die Seite automatisch neu. Die Dateien
auf der Festplatte werden dabei nicht verändert.
"""

import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8081
ROOT = os.path.dirname(os.path.abspath(__file__))

LIVERELOAD_JS = b"""
<script>
(function () {
  var token = null;
  setInterval(function () {
    fetch("/__livereload").then(function (r) { return r.text(); }).then(function (t) {
      if (token === null) { token = t; }
      else if (t !== token) { location.reload(); }
    }).catch(function () {});
  }, 1000);
})();
</script>
"""


def watch_token():
    """Höchste mtime aller überwachten Dateien als String."""
    latest = 0.0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for name in filenames:
            if name.endswith((".html", ".json", ".js", ".svg", ".jpg", ".png")):
                try:
                    latest = max(latest, os.path.getmtime(os.path.join(dirpath, name)))
                except OSError:
                    pass
    return str(latest)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path == "/__livereload":
            body = watch_token().encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        path = self.translate_path(self.path)
        if path.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as f:
                content = f.read()
            if b"</body>" in content:
                content = content.replace(b"</body>", LIVERELOAD_JS + b"</body>", 1)
            else:
                content += LIVERELOAD_JS
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        super().do_GET()

    def log_message(self, fmt, *args):
        if "/__livereload" not in (args[0] if args else ""):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("localhost", PORT), Handler)
    print(f"Fußtrack-Devserver läuft: http://localhost:{PORT}/fusstrack.html")
    print("Live-Reload aktiv – Seite lädt bei Dateiänderungen automatisch neu. Beenden mit Ctrl+C.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
