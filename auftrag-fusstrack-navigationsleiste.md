# Auftrag Fuss-Track (Patienten-App): eine feste Navigationsleiste für alle Ansichten

Stand 19.09.2026, Cowork-Sitzung. Entscheidung des Autors 19.09.2026: nur dieser Punkt („erst mal nur 1"); kein Hinweistext zur iOS-Leiste, keine Textänderung in der Clinic. Datei: `fusstrack.html` im Repo Fuss-Track (Stand der Cowork-Kopie vom 13.09.2026, 676.585 Byte, 5.151 Zeilen; Zeilenangaben beziehen sich darauf, bitte am aktuellen Stand nachziehen). Ein Commit, eine Vollzugsmeldung; Deploy per Push wie gewohnt (patienten.fuss-track.de).

## Anlass und Befund

Am Handy geht die Orientierung verloren, sobald man scrollt: Die Knöpfe zum Zurückspringen und zur Startseite stehen nur im Seitenkopf und wandern mit dem Inhalt weg. Wird die App aus der Clinic geöffnet (dort läuft sie als App vom Startbildschirm), zeigt iOS zusätzlich sein eigenes Browserfenster mit X oben links (schließt das Fenster, zurück zur Clinic) und ‹ unten links (eine Seite zurück im Fenster). Diese iOS-Elemente kann die App nicht beeinflussen; sie kann nur ihre eigene Navigation so machen, dass man sie nicht braucht.

Heute gibt es zwei verschiedene Leisten, beide nicht fixiert, und eine Ansicht ohne Leiste:

1. `Header` (Z. 2928–2995): Titel „Fuss-Track", darunter je nach Aufruf die Knöpfe „← Zurück" (`goBack`: Verlauf, sonst Hauptmenü) und „⌂ Hauptmenü" (`goHauptmenue`: `?home=1`) sowie der Moduswechsel („Infomaterial zum Krankheitsbild ansehen" / „Zum Patientenbegleiter"). Aufrufe: Z. 1152, 1164 (Startseite, ohne Knöpfe), 1180 (Wegweiser, mit Knöpfen), 1195 (Wissen direkt), 1234, 1305 (Aufklärung, Knöpfe nur bei `IN_APP_NAV`), 1323 (Startseite ohne Session, ohne Knöpfe), 1338 (Begleiter, mit Knöpfen), 3450 (Fehlerseite). CSS `.app-header` Z. 69–82 (zentriert, Trennlinie, `margin-bottom: 24px`).
2. `ZurueckLeiste` (Z. 965–973, CSS `.zurueck-leiste`/`.zl-btn`/`.zl-titel` Z. 51–66): „← zurück" (Rücksprung innerhalb der Ansicht per Zustand) · Titel · „⌂ Start" (`?home=1`). Aufrufe: Z. 1472, 1489, 1694 (Nicht-OP-Begleiter), 2041, 2138 (Krankheitsbild), 2642, 2686 (Infomaterial), 2736, 2779 (Begleiter-Auswahl).

Beide Leisten scrollen mit dem Inhalt weg. Die Startseite (`LandingView`, Z. 1164 und 1323) hat gar keine Knöpfe.

## Änderung

**Eine Leiste, oben fixiert, in jeder Ansicht.** Neue Komponente `NavLeiste({ onBack, titel, zurueckLabel })`, CSS-Klasse `.nav-leiste`:

```
.nav-leiste { position: sticky; top: 0; z-index: 50; display: flex; align-items: center; gap: 8px;
  padding: 8px 12px; padding-top: calc(8px + env(safe-area-inset-top));
  background: var(--c-card); border-bottom: 1px solid rgba(0,0,0,.08); }
```

Aufbau: links Knopf „‹ Zurück", Mitte Titel (eine Zeile, `overflow: hidden; text-overflow: ellipsis; white-space: nowrap`, Schrift 15, Markenschrift wie `h1`), rechts Knopf „⌂ Start". Knöpfe in der Optik von `.zl-btn` (Z. 56–59), Mindesthöhe 36 px für den Daumen. Die Leiste steht als erstes Kind von `<div className="app">` in jeder Ansicht, damit `sticky` gegen das Dokument wirkt (kein umschließendes Element mit `overflow`).

Verhalten der Knöpfe:

- „‹ Zurück": in den Ansichten mit eigenem Zustand (die bisherigen `ZurueckLeiste`-Aufrufe) der bisherige `onBack`; in den Ansichten mit `Header` das bisherige `goBack` (Verlauf, sonst Startseite). Auf der Startseite entfällt der Knopf; an seiner Stelle bleibt der Platz leer, damit der Titel zentriert steht.
- „⌂ Start": immer `?home=1` (wie heute `goHauptmenue` und `ZurueckLeiste`). Auf der Startseite ausgegraut und ohne Funktion (Merkmal: man ist schon dort).
- Titel: der Ansichtstitel (bisheriger `titel` der `ZurueckLeiste`, bei `Header` der übergebene `titel`, sonst „Fuss-Track").

**Der Moduswechsel** („Infomaterial zum Krankheitsbild ansehen" / „→ Zum Patientenbegleiter", `switchMode` Z. 2929–2955) bleibt, wo er ist, als Knopf unterhalb der Leiste im bisherigen `Header`-Bereich; er gehört nicht in die feste Leiste (zu lang für eine Zeile am Handy).

**Umbau:** `ZurueckLeiste` wird durch `NavLeiste` ersetzt (neun Aufrufe, gleiche Parameter), das alte CSS `.zurueck-leiste`/`.zl-titel` entfällt, `.zl-btn` bleibt als Knopf-Optik. Im `Header` entfallen die Knöpfe „← Zurück" und „⌂ Hauptmenü" (Z. 2970–2985); der `Header` rendert nur noch `h1`, Untertitel und Moduswechsel, und die `NavLeiste` steht vor ihm. Auf der Startseite (`?home=1`, Z. 1164; ohne Session, Z. 1323) bekommt die Leiste `onBack={null}`. Die Fehlerseite (Z. 3450) und die Auffangseite (`AuffangSeite`, Z. 3018) bekommen die Leiste ebenfalls, damit es keinen Endpunkt ohne Weg zur Startseite gibt.

**Fokus-Ansicht (QR aus dem Sprechstundenbrief, `IN_APP_NAV === false`):** Dort ist die Navigation bewusst reduziert (`FokusKopf`, `FokusFuss`, `FokusRuecksprung`), weil der Patient genau ein Thema sehen soll. Die Leiste erscheint dort mit „‹ Zurück" (Verlauf, sonst Startseite) und „⌂ Start" wie überall; die Fokus-Bausteine bleiben unverändert darunter. Wenn du das anders willst (Fokus ohne Leiste), sag es in der Vollzugsmeldung, dann entscheidet der Autor.

**Nichts anderes:** Inhalte, Deep-Links, Session-Verhalten, `buildUrl`, Moduswechsel, Fokus-Bausteine unverändert.

## Abnahme

Cowork-Prüfstand (Kopie der Patienten-App, 393 px und 1280 px): In Begleiter (`?op=…&var=…`), Infomaterial (Krankheitsbild und Kategorie), Nicht-OP-Begleiter, Aufklärung (`?op=…&modus=aufklaerung&nav=1`), Wegweiser (`?finder=1`) und Wissen direkt bleibt die Leiste beim Scrollen oben stehen, überdeckt keinen Inhalt (erste Karte beginnt unter der Leiste), Titel wird bei Überlänge mit „…" gekürzt, Knöpfe mindestens 36 px hoch. Startseite: kein „Zurück", „Start" ausgegraut. „‹ Zurück" führt in jeder Unteransicht dahin, wo der bisherige Knopf hinführte (Vergleich mit dem Stand davor je Ansicht). „⌂ Start" führt überall auf `?home=1`. Keine Konsolenfehler, JSX transpiliert (Babel-Prüfung wie üblich).

Abnahme des Autors am Handy, aus der Clinic heraus: Kachel „Fußtrack (Patient-App)" → Startseite mit Leiste (nur „Start", ausgegraut) → Begleiter → Eingriff wählen → nach unten scrollen: Leiste bleibt oben stehen; „⌂ Start" bringt zur Startseite der Patienten-App; X oben links (iOS) bringt zur Clinic zurück, der Brief ist noch da.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern von `NavLeiste`, dem geänderten `Header` und der Startseite.
