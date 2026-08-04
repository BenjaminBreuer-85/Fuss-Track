# Fuss-Track (Patienten-App)

Patienten-App des Fußzentrums: Information und OP-Begleitung rund um Fuß- und
Sprunggelenkserkrankungen. Eine einzige HTML-Datei (`fusstrack.html`) lädt alle
Inhalte zur Laufzeit aus den JSON-Dateien im selben Ordner.

## Oberste Regel: Medizinische Inhalte nicht anfassen

Alle medizinischen Inhalte (Texte in den JSON-Dateien) werden **extern
erarbeitet, geprüft und freigegeben**. In diesem Repository werden sie nur
**technisch eingepflegt** (einfügen, verschieben, verdrahten, validieren).

- Niemals medizinische Texte inhaltlich „verbessern", umformulieren, kürzen,
  ergänzen oder „korrigieren" — auch nicht bei vermeintlichen Fehlern.
  Auffälligkeiten stattdessen melden und auf Anweisung warten.
- Textänderungen nur, wenn der neue Wortlaut explizit vorgegeben wurde.
- Rein technische Korrekturen (JSON-Syntax, kaputte Referenzen, Encoding)
  sind erlaubt, dürfen aber den Wortlaut nicht verändern.

## Autorenregeln für Patiententexte

**Aufzählungen sind erlaubt, aber nur als eigenständige Liste.** Eine Liste steht
als abgesetzter Block, eingeleitet durch einen Satz oder eine Zwischenüberschrift.
Innerhalb eines laufenden Absatzes werden keine Spiegelstriche gesetzt —
Aufzählungen mitten im Fließtext werden ausformuliert.

**Ein einziges Listenzeichen im gesamten Bestand: der Spiegelstrich `- `.**
Keine `*`, `+`, `•` und keine nummerierten Listen (`1.`), auch nicht vereinzelt.
Das gilt für `bausteine.json`, `aufklaerung.json`, `phasen.json` und `nonop.json`.

Nicht betroffen sind Strukturen, die keine Markdown-Listen sind:
Quellenverzeichnisse, die aus Daten erzeugten Übungsschritte und Tabellen.

Beim Umformulieren bleibt der Inhalt identisch — es ändert sich ausschließlich
die Form.

**Verweise auf Übungsprogramme stehen bei der ersten Erwähnung der Übungen im
Artikel, prominent als eigene Linkzeile.** Maßgeblich ist die erste Erwähnung
über alle Slides hinweg, nicht die erste Detail-Liste: Nennt schon der
Überblick die Übungen, gehört der Link dorthin. Gemeint ist die Erwähnung der
Übungen **als Behandlung** — Training als Risikofaktor („Trainingsfehler",
„hohes Trainingspensum") zählt nicht. Zusätzlich steht der Verweis im
Konservativ-Abschnitt, wenn dieser als QR-/`thema`-Einstieg dient — diese
Doppelung ist gewollt: Wer über den Anker dort landet, sieht den Überblick nie.

## Markenrichtlinie (BRAND.md)

Verbindlich: Alle Änderungen an Oberfläche, Texten oder Grafiken müssen
[BRAND.md](BRAND.md) entsprechen. Bei Konflikten BRAND.md folgen und mich
(den Autor) auf den Konflikt hinweisen.

BRAND.md existiert identisch in beiden Fuss-Track-Repos (Toolbox und
Fußtrack). Nach jeder Änderung an BRAND.md den Nutzer erinnern, die Kopie
im jeweils anderen Repo zu aktualisieren.

Schreibweise der Marke in allen Texten einheitlich „Fuss-Track" (Doppel-s).

Der Bestand wird NICHT automatisch an BRAND.md angeglichen — nur künftige
Änderungen werden dagegen geprüft; Abweichungen im Bestand nur auflisten,
nicht eigenmächtig ändern.

## Öffentliche Startseite und Domain

`index.html` ist die Patienten-Landingpage (statisches HTML, Schriften lokal
aus `fonts/` per @font-face — keine externen Font-Server, DSGVO). Ihre
Buttons „Zur App"/„App öffnen" führen zu `fusstrack.html`; der Footer-Link
„Fuss-Track Clinic" führt zu https://fuss-track.de. Die `CNAME`-Datei setzt
die GitHub-Pages-Domain **patienten.fuss-track.de**. Die Patienten-App
selbst bleibt `fusstrack.html`.

## Aufbau der App

`fusstrack.html` ist eine React-18-Single-File-App (JSX via Babel im Browser,
kein Build-Schritt). Die Bibliotheken liegen lokal in `lib/`
(`react.production.min.js`, `react-dom.production.min.js`, `babel.min.js`).
Beim Start werden sechs JSON-Dateien mit Cachebuster (`?v=Date.now()`)
gefetcht. Es gibt keinen Server-Backend-Anteil; Nutzerauswahl (Eingriff,
OP-Datum …) liegt im localStorage.

Drei Hauptbereiche:

1. **Begleiter** — Schritt-für-Schritt-Begleitung vor und nach der OP
   (Phasen, Erinnerungen, Wissensartikel). Daten: `phasen.json`, `aufklaerung.json`.
2. **Infomaterial** — Krankheitsbilder, OP-Techniken, nicht-operative
   Maßnahmen, Allgemeines. Daten: `infomaterial.json` (Struktur) +
   `bausteine.json` (Texte) + `nonop.json` (konservative Stufenschemata).
3. **Diagnose-Helfer** — Eingrenzung möglicher Ursachen von Beschwerden.
   Daten: `katalog.json`.

Deep-Link-Parameter (URLSearchParams): `?op=<key>` (+ `&modus=aufklaerung`),
`?massnahme=<key>`, `?kb=`, `?var=`, `?wissen=`, `?finder=`, `?ctx=`, `?home=`.

## Welche Inhalte liegen in welcher JSON-Datei?

| Datei | Inhalt |
|---|---|
| `infomaterial.json` | `INFOMATERIAL`: alle Infomaterial-Einträge (Kategorien `krankheitsbild`, `op_technik`, `allgemein`). Ein Eintrag enthält Titel/Untertitel, `betrifft_eingriffe`, `quellen`, `stand` und eine `slides`-Liste, deren Keys auf `BAUSTEINE` verweisen. Außerdem `NONOP_MASSNAHMEN`: die nicht-operativen Maßnahmen (Stoßwelle, PRP, RSO …) mit eigenen `abschnitte`-Texten und Quellen. |
| `bausteine.json` | `BAUSTEINE`: die eigentlichen Textbausteine (`{titel, text}`), auf die `infomaterial.json` per Slide-Key verweist. Hier liegt der Großteil des Patiententextes. |
| `nonop.json` | Konservative Behandlungspfade für den Bereich „nicht-operativ": `NONOP_KB` (Krankheitsbilder), `NONOP_INHALTE` (Stufentexte), `NONOP_STUFEN`, `NONOP_AMPEL`. |
| `phasen.json` | Alles für den Begleiter: `KRANKHEITSBILDER`, `EINGRIFFE` (chevron, osg_arthrodese, osg_tep), `ONBOARDING_PHASEN`, `SHARED_PRE_OP_PHASEN`, `POST_OP_PHASEN_BY_OP`, `PHASEN_INHALTE` sowie Wissensartikel (`WISSEN`, `WISSEN_KATEGORIEN`). |
| `aufklaerung.json` | `AUFKLAERUNG`: Aufklärungstexte je Eingriff/Krankheitsbild (osg_arthrose, chevron, osg_arthrodese_op, osg_tep_op), erreichbar u. a. über `?op=<key>&modus=aufklaerung`. |
| `katalog.json` | Datenbasis des Diagnose-Helfers: `kb_universum`, `regionen`, `ansichten` (oben/unten/innen/außen), `ergebnis_logik`, `akut_bypass`, `haeufigkeits_bonus`. |

`bilder/` enthält Abbildungen (Entscheidungsbäume als SVG, OP-/Verbandsfotos).

## Entwicklungsserver (Live-Reload, Port 8081)

Die Toolbox belegt Port 8080, Fuss-Track nutzt daher **8081**.

```bash
python3 dev-server.py
```

Adresse: **http://localhost:8081/fusstrack.html**

`dev-server.py` (nur Python-Standardbibliothek, kein Node nötig) serviert den
Ordner und injiziert beim Ausliefern von HTML ein kleines Polling-Skript: bei
jeder Änderung an `*.html`/`*.json`/`lib/`/`bilder/` lädt der Browser die
Seite automatisch neu. Die Dateien selbst werden nicht verändert. Alternativ
kann der Server über die Preview-Konfiguration `.claude/launch.json`
(Name `fusstrack`) gestartet werden.

## Nach jeder Änderung validieren

- JSON parst fehlerfrei (`python3 -m json.tool <datei> > /dev/null`).
- Keine toten Referenzen: jeder `slides`-Key aus `infomaterial.json` existiert
  in `BAUSTEINE`; Deep-Link-Keys (`?op=`, `?massnahme=`) lösen auf.
- App im Browser unter Port 8081 laden und den betroffenen Bereich anklicken.

Deployment erfolgt manuell durch den Autor über GitHub; die zu deployenden
Dateien beim Abschluss einer Änderung explizit benennen.
