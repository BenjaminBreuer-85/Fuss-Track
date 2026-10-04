# Auftrag Fuss-Track (klein): Gemerktes Wegweiser-Ergebnis nur auf dem Rückweg aus einem Artikel; kurzes blaues Aufleuchten beim Antippen

Stand 04.10.2026, Cowork-Sitzung. Datei `fusstrack.html`, Ausgangsstand 74e099a (695.379 B, md5 f457e3a7…; Zeilenangaben darauf). Handy-Beobachtung des Autors 03./04.10.2026: Nach einem Durchgang bleiben die Angaben erhalten; wer den Wegweiser neu öffnet, landet sofort wieder auf dem alten Ergebnis. Gewünscht: Wer die Ergebnisseite über „‹ Zurück“ in der Leiste, „⌂ Start“ oder die Startseite verlässt, soll beim nächsten Öffnen unkompliziert von vorne beginnen; das gemerkte Ergebnis soll nur für den Rückweg aus einem Artikel („Mehr zum Krankheitsbild“ → „‹ Zurück“) gelten. Zweiter Wunsch des Autors 04.10.2026: Ein angetipptes Feld soll im Wegweiser und im Infomaterial kurz blau aufleuchten, damit die Auswahl in Videos erkennbar ist und der Nutzer eine Rückmeldung bekommt (Abschnitt 2). Ein Commit, eine Vollzugsmeldung mit Commit-Hash und Zeilennummern.

## Befund

Stufe 2 (74e099a) merkt das Ergebnis 30 Minuten in `sessionStorage` `fusstrack_finder` (`ergebnisMerken` Z. 3896–3898, Schreiben in `renderErgebnis` Z. 4259–4260) und startet `FinderView` damit direkt im Schritt „ergebnis“ (`gemerkt` Z. 3838–3847). Gelöscht wird der Merker nur durch „Erneut starten“ (`resetFinder` Z. 3915–3916) oder nach 30 Minuten. Jeder andere Weg zurück in den Wegweiser innerhalb dieser Zeit (Startseite → Kachel, Neuladen, Direktaufruf `?finder=1`) zeigt deshalb das alte Ergebnis.

## 1. Merker

(a) **Merker nur bei Rückkehr über den Verlauf anwenden.** In der Selbstaufruf-Funktion `gemerkt` (Z. 3838–3847) zusätzlich prüfen, wie die Seite geladen wurde: `const nav = (performance.getEntriesByType && performance.getEntriesByType("navigation")[0]) || null; const zurueck = nav ? nav.type === "back_forward" : (performance.navigation && performance.navigation.type === 2);` (alte API als Rückfall für ältere Safari-Versionen). Nur wenn `zurueck` wahr ist, wird der gemerkte Zustand übernommen; sonst wird der Eintrag sofort gelöscht (`sessionStorage.removeItem`) und der Wegweiser beginnt bei Schritt 1. Damit gilt: Artikel → „‹ Zurück“ (Browser-Verlauf) → Ergebnis bleibt; Startseite → Kachel, „⌂ Start“ → Kachel, Neuladen, Direktaufruf → Schritt 1. Hinweis zum Handy: Safari stellt die Seite beim Zurückwischen oft aus dem Seitenspeicher wieder her, dann läuft dieser Code gar nicht und das Ergebnis steht ohnehin noch; die Prüfung greift nur beim echten Neuladen über den Verlauf.

(b) **Beim Verlassen über die Leiste löschen.** Zusätzlich im `popstate`-Zuhörer (Z. 3861–3868): kommt ein Verlaufseintrag ohne `finder`-Zustand (also der Wegweiser wird nach hinten verlassen), vorher `ergebnisVergessen()` aufrufen. Und in `renderErgebnis` den Merker nicht bei jedem Rendern schreiben (Z. 4259–4260), sondern einmal beim Erreichen des Ergebnisses (in `goToNextFrage`, Z. 4139–4141, direkt vor `setStep("ergebnis")`), damit das Schreiben und Löschen an einer Stelle nachvollziehbar bleibt.

(c) **Aufräumen aus der Gegenprobe:** `ergebnisGemerkt()` (Z. 3904–3912) ist ungenutzt und doppelt zu Z. 3838–3846, entfernen. Hinweissatz Z. 4358: schließendes Anführungszeichen typografisch („‹ Zurück“ statt „‹ Zurück").

## 2. Kurzes blaues Aufleuchten beim Antippen (Wegweiser, Infomaterial, Schaltflächen)

Befund: Die Antwortknöpfe (`.btn`, Z. 4177–4185), die Trefferflächen im Fußbild (`HotSpot`, Z. 3614–3652, Polygone mit `cursor: pointer`), die Themenliste im Infomaterial (Z. 2836 ff., `div` mit Inline-Stil `cursor: pointer` und `onClick`), die Kacheln der Startseite und die Reiter der Artikel haben keinen Druckzustand; auf dem Handy sieht man beim Tippen nichts, erst der Zustandswechsel danach. Es gibt keine `:active`-Regel und keine Tipp-Animation im Stylesheet (nur `modal-fade`/`modal-slide`, Z. 314–315).

Umsetzung ohne Eingriff in jede Komponente, ein zentraler Zuhörer plus CSS:

(a) Stylesheet, neben Z. 314: 
```
@keyframes ft-tipp { 0% { box-shadow: 0 0 0 4px rgba(44,79,124,.45); background-color: rgba(44,79,124,.18); } 100% { box-shadow: 0 0 0 0 rgba(44,79,124,0); background-color: transparent; } }
.ft-tipp { animation: ft-tipp .4s ease-out; }
@keyframes ft-tipp-svg { 0% { fill: rgba(44,79,124,.45); stroke: rgba(44,79,124,.95); stroke-width: 3; } 100% { fill: transparent; stroke: transparent; } }
svg .ft-tipp { animation: ft-tipp-svg .45s ease-out; }
```
Blau = `--c-main` (#2C4F7C). Für bereits blaue Knöpfe (`.btn-primary`, gewählte Antwort) genügt der Ring; die Hintergrundfarbe fällt dort nicht auf, das ist in Ordnung. Für die Trefferfläche: nach der Animation gilt wieder der gesetzte Zustand (Punktraster bei Auswahl, sonst transparent), weil die Animation keinen `fill-mode` hat.

(b) Ein globaler Zuhörer, einmal beim Start der App (neben den anderen Initialisierungen, z. B. nach Z. 1020):
```
document.addEventListener("pointerdown", function(ev) {
  var el = ev.target && ev.target.closest && ev.target.closest(".btn, .zl-btn, .fs-chip, button, a, [role=button], [style*='cursor: pointer']");
  if (!el || el.classList.contains("ft-tipp")) return;
  el.classList.add("ft-tipp");
  var weg = function() { el.classList.remove("ft-tipp"); el.removeEventListener("animationend", weg); };
  el.addEventListener("animationend", weg);
  setTimeout(weg, 600);
}, { passive: true });
```
Der Attribut-Selektor `[style*='cursor: pointer']` trifft die Themenliste im Infomaterial, die Kacheln, die Ansicht-Reiter des Wegweisers und die SVG-Polygone, weil React den Zeiger als Inline-Stil schreibt; `button`/`a` treffen Antwortknöpfe, Weiter/Zurück, Leiste und Links. Reine Textabsätze und Karten ohne Zeiger leuchten nicht. `pointerdown` feuert bei Maus, Finger und Stift, vor dem Klick, darum ist das Aufleuchten auch dann sichtbar, wenn der Klick die Ansicht sofort wechselt. Keine Änderung an den Klick-Handlern selbst; die Touch-Logik der Trefferflächen (Z. 3622–3638) bleibt unberührt, der Zuhörer ist passiv.

(c) Nicht aufleuchten sollen Eingabefelder (`input`, Suchfeld) und der Datenschutz-Banner-Hintergrund; der Selektor oben trifft sie nicht. Auf `prefers-reduced-motion: reduce` die Animation auf 0,15 s verkürzen, nicht abschalten (die Rückmeldung ist der Zweck).

## Nichts anderes

Punktesystem, Sonderfälle, Verlaufseinträge, Ergebniskarten, `katalog.json` unverändert.

## Abnahme

Cowork-Prüfstand (393 px): (1) Ergebnis → „Mehr zum Krankheitsbild“ → Artikel → „‹ Zurück“ → dieselbe Ergebnisseite. (2) Ergebnis → „⌂ Start“ → Kachel Beschwerde-Wegweiser → Schritt 1; `sessionStorage` ohne `fusstrack_finder`. (3) Ergebnis → Neuladen → Schritt 1. (4) Ergebnis → Direktaufruf `?finder=1` in derselben Sitzung → Schritt 1. (5) Ergebnis → Browser-Zurück bis vor den Wegweiser → Merker gelöscht; erneuter Aufruf → Schritt 1. (6) „Erneut starten“ wie bisher. (7) Aufleuchten: Antwortknopf, Trefferfläche im Fußbild, Ansicht-Reiter, Eintrag in der Themenliste des Infomaterials, Kachel der Startseite, Artikel-Reiter zeigen bei `pointerdown` die Klasse `ft-tipp` und verlieren sie nach spätestens 600 ms; Trefferfläche nach dem Aufleuchten im gesetzten Zustand (Punktraster oder transparent); Suchfeld ohne Aufleuchten; Screenshots während der Animation (393 px) als Beleg. (8) Keine Konsolenfehler, JSX-Transpile-Prüfung.

Am Handy: Durchgang bis zum Ergebnis → ein Thema öffnen → „‹ Zurück“ → Ergebnis noch da; „⌂ Start“ → Kachel Wegweiser → beginnt bei Schritt 1. Beim Antippen einer Antwort, einer Zone im Fußbild und eines Themas im Infomaterial leuchtet das Feld kurz blau auf.

Deploy: Push `fusstrack.html`.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
