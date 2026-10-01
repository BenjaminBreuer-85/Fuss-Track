# Auftrag Fuss-Track: Anleitung „Fuss-Track auf den Startbildschirm“ für Patienten

Stand 01.10.2026, Cowork-Sitzung. Repo Fuss-Track, Datei `fusstrack.html` (Ausgangsstand 635dcf9, md5 c8144237…, 682.479 B), dazu neu `manifest.json`; `index.html` eine Zeile. Wunsch des Autors: Patienten, die die App laden, sollen geführt werden, wie sie Fuss-Track wie eine normale App auf den Startbildschirm legen, weil das nicht wie im App Store automatisch passiert. Ein Commit, eine Vollzugsmeldung mit Zeilennummern.

## Befund

Fuss-Track Clinic hat die Anleitung bereits (`app.html` Stand dcc5c9f): Konstante `HOMESCREEN_MERKER`, `alsAppGestartet()` (Standalone-Erkennung über `display-mode: standalone` und `navigator.standalone`), `geraeteArt()` (iOS Safari / iOS anderer Browser / Android / Desktop über User-Agent), die Symbolgrafiken `SymbolTeilen` und `SymbolMenue`, die Komponente `HomescreenKarte({onClose, alsSchritt})` mit gerätespezifischem Text (Z. 9299–9375), der Menüpunkt „Zum Startbildschirm hinzufügen“ (Z. 10123) und die Einmal-Anzeige nach dem Login mit Merker in `localStorage` und Aufruf über `?tipp=homescreen` (Z. 10213). Kopf der Clinic: `<link rel="manifest" href="manifest.json">` (Z. 31), Apple-Touch-Icon (Z. 30), `theme-color`.

Fuss-Track (`fusstrack.html`) hat nichts davon: nur `<meta name="theme-color" content="#2C4F7C">` (Z. 6) und `<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">` (Z. 13); kein Manifest, kein Hinweistext. Die Landing-Page `index.html` sagt unter „Auf welchen Geräten läuft Fuss-Track?“ nur „auf Wunsch lässt sich die App wie eine normale App auf den Startbildschirm legen“ (Z. 278), ohne das Wie. Folge: Ohne Manifest öffnet iOS ein Startbildschirm-Symbol als Safari-Lesezeichen mit Adressleiste, nicht als eigenständige App, und der Patient findet den Weg nicht.

## 1. Manifest und Icons

Neue Datei `manifest.json` im Repo-Root: `name` „Fuss-Track“, `short_name` „Fuss-Track“, `start_url` „./fusstrack.html“, `scope` „./“, `display` „standalone“, `background_color` „#FFFFFF“, `theme_color` „#2C4F7C“, `lang` „de“, `icons` mit `icons/icon-192.png` und `icons/icon-512.png` (`purpose` „any“); beide Dateien liegen bereits im Repo (192 × 192 und 512 × 512 Pixel, geprüft 01.10.2026), keine neuen Icons nötig. In `fusstrack.html` nach Z. 13: `<link rel="manifest" href="manifest.json">`. Kein Service Worker, kein Offline-Cache (die App lädt die JSON-Daten mit `?v=Date.now()`; das bleibt so). Prüfen, ob iOS 17/18 das Manifest mit `display: standalone` ohne das veraltete Meta-Tag `apple-mobile-web-app-capable` übernimmt; andernfalls das Meta-Tag zusätzlich setzen und in der Vollzugsmeldung nennen.

## 2. Anleitung übernehmen

Aus der Clinic übernehmen, Farben und Schrift an Fuss-Track anpassen: `alsAppGestartet()`, `geraeteArt()`, `SymbolTeilen`, `SymbolMenue`, `HomescreenKarte`. Texte für Patienten (Sie-Form, wie in der Clinic), Überschrift „Fuss-Track auf den Startbildschirm“, Einleitungssatz „Dann öffnen Sie Fuss-Track wie eine normale App, ohne Browser und ohne Adresse eintippen.“ Gerätetexte wie in der Clinic (iOS Safari: Teilen-Symbol, „Zum Home-Bildschirm“; iOS anderer Browser: nur in Safari möglich; Android: drei Punkte, „App installieren“ bzw. „Zum Startbildschirm hinzufügen“; Desktop: Lesezeichen). Keine Markennamen außer Safari und Chrome in den Gerätetexten.

## 3. Wo die Karte erscheint

(a) Einmalig, dismissbar, Merker `ft-homescreen-gesehen` in `localStorage` (mit try/catch wie beim Datenschutz-Merker): auf der Startseite unterhalb der Hauptkacheln, aber erst, nachdem der Hinweis zur Datenverarbeitung bestätigt ist (nicht beide gleichzeitig). Nicht in Artikel- und Maßnahmenansichten über Deep-Link (`?op=`, `?massnahme=`, `?nonop=`), damit ein Patient, der in der Praxis einen QR-Code gescannt hat, zuerst den Artikel liest. Nicht, wenn die App schon vom Startbildschirm läuft (`alsAppGestartet()`).
(b) Im Begleiter (OP-Begleitung), weil Patienten dort täglich wiederkommen: dieselbe Karte einmalig oberhalb der Tagesansicht, gleicher Merker.
(c) Dauerhaft erreichbar: Eintrag „Fuss-Track auf den Startbildschirm“ im Menü der Navigationsleiste (bzw. dort, wo Impressum und Datenschutz verlinkt sind), der die Karte aufklappt; entfällt, wenn die App schon vom Startbildschirm läuft.
(d) `?tipp=homescreen` zeigt die Karte auch nach dem Wegklicken, damit die Landing-Page `index.html` (Z. 278) darauf verlinken kann: Satz dort ergänzen um „ — so geht es“ mit Link `fusstrack.html?tipp=homescreen`.

Schaltflächen der Karte: „Verstanden“ (setzt den Merker) und „Später“ (schließt nur für diese Sitzung, kein Merker).

## 4. Folgen des Standalone-Modus prüfen

Vom Startbildschirm gestartet gibt es keine Adressleiste und keinen Browser-Zurück-Knopf. Prüfen, dass jede Ansicht über „‹ Zurück“ und „⌂ Start“ verlassen werden kann (auch Impressum, Datenschutz, Maßnahmen-Seiten, Diagnose-Helfer). Externe Links (Praxis-Website, DOI-Links der Quellen) mit `target="_blank"` öffnen, damit sie den App-Rahmen nicht ersetzen. QR-Deep-Links aus der Clinic öffnen auf iOS weiterhin in Safari, nicht in der installierten App; das ist akzeptiert und braucht keine Änderung.

## Nichts anderes

`infomaterial.json`, `bausteine.json`, `phasen.json` unverändert. Keine Änderung an Begleiter-Inhalten oder Artikeln. Clinic unverändert.

## Abnahme

Cowork-Prüfstand: (1) `manifest.json` gültiges JSON, Icons vorhanden und quadratisch; `<link rel="manifest">` im Kopf. (2) Mit iPhone-Safari-User-Agent: Startseite zeigt nach „Einverstanden“ die Karte mit Teilen-Symbol und „Zum Home-Bildschirm“; „Verstanden“ setzt `ft-homescreen-gesehen`, nach Neuladen keine Karte; `?tipp=homescreen` zeigt sie wieder. (3) Chrome-iOS-UA: Safari-Hinweis; Android-UA: drei Punkte, „App installieren“; Desktop: Lesezeichen mit Cmd/Strg + D. (4) Deep-Link `?op=osg_tep_op&modus=aufklaerung`: keine Karte. (5) Begleiter: Karte einmalig oberhalb der Tagesansicht. (6) Menüpunkt vorhanden, klappt die Karte auf; bei simuliertem Standalone (`navigator.standalone = true`) weder Karte noch Menüpunkt. (7) Alle Ansichten mit „‹ Zurück“/„⌂ Start“ verlassbar; keine Konsolenfehler; JSX-Transpile-Prüfung.

Handy-Abnahme des Autors: iPhone, Safari, Fuss-Track öffnen, Datenschutz bestätigen → Karte lesen → Teilen → „Zum Home-Bildschirm“ → Symbol antippen: App öffnet ohne Adressleiste mit Fuss-Track-Symbol; zweiter Start: keine Karte, Menüpunkt fehlt.

Deploy: Push (`fusstrack.html`, `manifest.json`, `index.html`).

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
