# Auftrag Fuss-Track: Fortsetzen-Karte ausblenden oder Verlauf löschen

Stand 19.09.2026, Cowork-Sitzung. Entscheidung des Autors 19.09.2026: Variante A (schmale Zeile statt Karte) und Regel 2 (Karte kehrt nur bei Meilensteinen zurück); Konzept `konzept-fortsetzen-karte.md`. Datei `fusstrack.html`, Ausgangsstand Commit 5a99241 (NavLeiste; 674.750 Byte, Zeilenangaben darauf). Datenteil 3t (`phasen.json`, Feld `meilenstein: true` an 43 Bausteinen in `BEGLEITER_BAUSTEINE`) schreibt die Cowork-Sitzung nach eigener Freigabe; beide Dateien liegen im selben Repo und werden zusammen gepusht (Reihenfolge egal, der heutige Code ignoriert das Feld, der neue Code fällt ohne das Feld auf „nie wieder einblenden" zurück, siehe Punkt 4). Ein Commit, eine Vollzugsmeldung.

## Ausgangslage

`FortsetzenBanner` (Z. 878–930, CSS `.fs-karte` Z. 232–260) erscheint auf der Startseite bei bestehender Sitzung (Z. 1344–1348) und ist als Ganzes der Knopf „Weiter im Begleiter". Sitzung: `Storage` (Z. 764–789), Schlüssel `fusstrack_session`, Felder u. a. `eingriff`, `variante`, `aufenthalt`, `opDatum`, `createdAt`. Löschen: `resetSession` (Z. 1133–1141), Dialog `ResetModal` (Z. 5061–5076). Phasen: `getPhasenForVariant` (Z. 470), `computeCurrentPhaseIndex(phasen, opDatum)` (Z. 1047–1060); jede Phase hat `baustein` (Schlüssel in `BEGLEITER_BAUSTEINE`).

## Änderungen

1. **X in der Karte.** Oben rechts in `.fs-karte` ein Schließen-Knopf „✕" (36 × 36 px, weiß auf Blau, `position:absolute; top:8px; right:8px`, `.fs-karte` bekommt `position:relative`). `onClick` mit `stopPropagation`, damit die Karte nicht gleichzeitig „Fortsetzen" auslöst. `aria-label="Karte ausblenden oder Verlauf löschen"`.

2. **Dialog `KarteDialog`** nach dem Muster von `ResetModal` (Overlay, Klick außerhalb = Abbrechen). Titel „Hinweis zum Begleiter". Text: „Ihr Begleiter läuft weiter. Wollen Sie nur diese Karte ausblenden oder den Verlauf löschen?" Knöpfe in dieser Reihenfolge: „Nur ausblenden" (`btn btn-primary`), „Verlauf löschen" (`btn btn-secondary`, rote Schrift und roter Rand, darunter in 12 px: „Auswahl, OP-Datum und Fortschritt werden gelöscht. Das lässt sich nicht rückgängig machen."), „Abbrechen" (`btn btn-secondary`). Kein zweiter Dialog beim Löschen; „Verlauf löschen" ruft `resetSession` (Z. 1133) auf.

3. **Ausblenden speichern.** `Storage.set` mit dem neuen Feld in der Sitzung:

   ```
   karteAusgeblendet: { phaseIdx: <computeCurrentPhaseIndex(...)>, opDatum: session.opDatum, am: new Date().toISOString() }
   ```

   Ohne OP-Datum ist `phaseIdx` −1.

4. **Regel `karteZeigen(session)`** (neue Hilfsfunktion neben `computeCurrentPhaseIndex`): liefert `true`, wenn `karteAusgeblendet` fehlt; sonst `true`, wenn (a) `session.opDatum !== karteAusgeblendet.opDatum` (Datum eingetragen oder geändert) oder (b) zwischen `karteAusgeblendet.phaseIdx + 1` und dem heutigen `computeCurrentPhaseIndex` mindestens eine Phase liegt, deren Baustein in `BEGLEITER_BAUSTEINE` `meilenstein === true` trägt. Sonst `false`. Eine neue Sitzung (QR mit anderem Eingriff, Z. 1085–1113) hat das Feld nicht und zeigt die Karte. Trägt kein Baustein das Feld (Daten noch nicht deployt), gilt nur (a).

5. **Anzeige auf der Startseite** (Z. 1344–1348): `karteZeigen(session)` → volle Karte wie heute, zusätzlich mit dem Chip „Neu" vor der Zeile „Aktuell", wenn `karteAusgeblendet` gesetzt ist (die Karte kommt also gerade zurück). Sonst → **schmale Zeile** `FortsetzenZeile`: 44 px hoch, Hintergrund `var(--c-bg)`, Rahmen 1 px, Radius 10, eine Zeile: links „Ihr OP-Begleiter: `<anzeigename>`" (Ellipse bei Überlänge), rechts „Weiter ›" in `var(--c-main)`; Tippen = `onFortsetzen`. Ohne OP-Datum lautet der linke Teil „Ihr OP-Begleiter: OP-Datum eintragen". Kein X in der Zeile.

6. **Rückkehr der Karte:** Beim Tippen auf X in der zurückgekehrten Karte wird `karteAusgeblendet` mit dem heutigen `phaseIdx` neu gesetzt (Ausblenden bis zum nächsten Meilenstein). Das Feld wird bei `resetSession` mit gelöscht (es liegt in der Sitzung).

7. **Nichts anderes.** `resetSession`, `ResetModal` im Begleiter, `NavLeiste`, Deep-Links, `buildUrl`, Phasenlogik unverändert. Kein neuer Speicherschlüssel.

## Abnahme

Cowork-Prüfstand (Kopie mit 3t-`phasen.json`, 393 px, `localStorage` gestellt): (1) Sitzung `chevron/einfach`, OP-Datum heute −13 Tage: Karte sichtbar; X → „Nur ausblenden" → schmale Zeile, Tippen öffnet den Begleiter. (2) OP-Datum in der Sitzung auf heute −14 setzen (Meilenstein `faden_vorfuss` an Tag 14 erreicht): Karte wieder da mit Chip „Neu"; X → ausblenden → Zeile; OP-Datum auf heute −16: Zeile bleibt (kein Meilenstein zwischen 14 und 16). (3) OP-Datum auf heute −21 (`verband_ab_vorfuss`): Karte wieder da. (4) OP-Datum ändern (Feld in der Sitzung): Karte wieder da. (5) X → „Verlauf löschen": Startseite ohne Sitzung, kein Schlüssel `fusstrack_session`. (6) Sitzung ohne OP-Datum: Karte „Bitte OP-Datum eintragen" → ausblenden → Zeile „OP-Datum eintragen"; Datum eintragen → Karte wieder da. (7) Klick auf X löst kein „Fortsetzen" aus. Keine Konsolenfehler, JSX transpiliert.

Abnahme des Autors am Handy: Startseite mit laufendem Begleiter → X → „Nur ausblenden": schmale Zeile; App schließen und neu öffnen: Zeile bleibt; „Weiter ›" führt in den Begleiter. Zweites Gerät oder Reset: X → „Verlauf löschen" → Startseite ohne Karte.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern von `KarteDialog`, `karteZeigen` und `FortsetzenZeile`.
