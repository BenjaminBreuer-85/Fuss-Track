# Auftrag Fuss-Track: Reiter der Artikel- und Maßnahmenansicht zweizeilig, alle gleich groß

Stand 19.10.2026, Cowork-Sitzung. Datei `fusstrack.html`, Ausgangsstand 2b7ffba (700.803 B, md5 20358ab2…; Zeilenangaben darauf). Wunsch des Autors 19.10.2026 beim Durchsehen des Artikels „Diabetisches Fußsyndrom“: „Die Tabs sind nirgendwo ausgeschrieben und werden nur in verkürzter Form dargestellt. Könntest du diese nach unten verlängern, so dass auch zwei Zeilen darstellbar sind, aber die Breite gleich bleibt? Dies müsste homogen sein, so dass die Felder überall gleich groß sind, auch wenn dort weniger drin steht.“ Ein Commit, Vollzugsmeldung mit Commit-Hash und Zeilennummern.

## Befund

Zwei Reiterleisten mit demselben Muster: die Artikelansicht (Krankheitsbilder, OP-Techniken, Allgemein; Z. 3416–3452) und die Maßnahmenansicht (Z. 2731–2749). Beide kürzen den Titel im Code auf 17 Zeichen plus „…“ (Z. 3449 bzw. 2745), setzen `whiteSpace: nowrap` und `maxWidth: 160`, und jede Schaltfläche ist so breit wie ihr Text (heute 72 bis 144 px, Höhe 26 px). Dazu wurde der Seitentitel im Inhaltskasten der Artikelansicht entfernt (Z. 3457, Kommentar „steht bereits in den Tabs“), sodass ein langer Titel wie „Diagnostik & Risikoeinteilung“ tatsächlich nirgendwo vollständig erscheint. In der Maßnahmenansicht steht der Abschnittstitel dagegen über dem Inhalt (Z. 2674, 11 px, Großbuchstaben).

Bestand: 641 Reiter in der Artikelansicht (142 davon länger als 18 Zeichen, längster 55), 162 Reiter in der Maßnahmenansicht (längster 55). Prototyp `patient_tabs` (8831) geprüft, Zahlen unten daraus.

## Änderung

### 1. CSS, nach Z. 142 (`@media (prefers-reduced-motion …)`)

```
  /* Reiter der Artikel- und Maßnahmenansicht: feste Breite, Platz für zwei Zeilen, alle gleich groß */
  .reiter { flex: 0 0 132px; width: 132px; height: 40px; padding: 4px 8px; border-radius: 6px;
            display: flex; align-items: center; justify-content: center; text-align: center;
            font-size: 11px; line-height: 1.25; cursor: pointer; }
  .reiter-txt { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
                hyphens: auto; -webkit-hyphens: auto; overflow-wrap: anywhere; }
```

Alle Reiter sind damit 132 × 40 px, auch „8. Quellen“. Zwei Zeilen à 11 px, Text zentriert. `hyphens: auto` trennt lange Wörter („Behandlungsmög-lichkeiten“) auf iPhone und Android (Seite hat `lang="de"`); `overflow-wrap: anywhere` ist die Rückfallebene, wenn der Browser nicht trennt. Was auch in zwei Zeilen nicht passt, endet mit „…“ (`line-clamp`). Bei 393 px Breite sind 2,7 Reiter sichtbar, die Leiste scrollt wie heute seitlich.

### 2. Artikelansicht, Z. 3429–3450 (die `<button>` in `slides.map`)

Ersetzen durch:

```
            <button
              key={i}
              className="reiter"
              onClick={function() { setStep(i); }}
              style={{
                border: active ? "1px solid var(--c-main)" : "1px solid rgba(0,0,0,.10)",
                background: active ? "var(--c-main)" : "var(--c-card)",
                color: active ? "#fff" : "var(--c-text-muted)",
                fontWeight: active ? 700 : 500
              }}
              title={shortLabel}
            >
              <span className="reiter-txt">{(i + 1) + ". " + shortLabel}</span>
            </button>
```

Das geschützte Leerzeichen nach der Nummer verhindert, dass die Nummer allein in der ersten Zeile steht. Die Kürzung auf 17 Zeichen entfällt. Der umgebende Scroll-Container (Z. 3417–3424) bleibt unverändert.

### 3. Artikelansicht, Z. 3457: Seitentitel über dem Inhalt

Die Kommentarzeile `{/* Slide-Titel entfernt – steht bereits in den Tabs */}` ersetzen durch:

```
        {/* Titel der Seite ausgeschrieben (die Reiter können lange Titel kürzen), wie in der Maßnahmenansicht */}
        {current.titel && (
          <div style={{ fontSize: 11, fontWeight: 700, color: "var(--c-main)", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 8 }}>
            {current.titel}
          </div>
        )}
```

Gleiche Gestaltung wie der Abschnittstitel der Maßnahmenansicht (Z. 2674). Damit ist jeder Titel an einer Stelle vollständig lesbar, auch die 28 von 827 Reitern (3,4 %), die im Prototyp ohne Silbentrennung nicht in zwei Zeilen passen (z. B. „Versteifung des Großzehengrundgelenks (MTP1-Arthrodese)“, „Behandlungsmöglichkeiten beim Hallux rigidus“, „Ergebnisse — Muskel, Knochenheilung und Sesamoiditis“).

### 4. Maßnahmenansicht, Z. 2738–2746 (die `<button>` in `mSteps.map`)

Ersetzen durch:

```
                  <button key={it.key} className="reiter" onClick={function(){ mGeheZu(i); }} title={lbl}
                          style={{ border: aktiv ? "1px solid var(--c-main)" : "1px solid rgba(0,0,0,.10)",
                                   background: aktiv ? "var(--c-main)" : "var(--c-card)",
                                   color: aktiv ? "#fff" : "var(--c-text-muted)",
                                   fontWeight: aktiv ? 700 : 500 }}>
                    <span className="reiter-txt">{(i + 1) + ". " + lbl}</span>
                  </button>
```

### 5. Tipp-Feedback

Die Reiter sind `<button>` und damit vom Zuhörer (e20fde5) erfasst; `.is-pressed` wirkt weiter. Keine Änderung.

## Nichts anderes

Inhalte, Reihenfolge der Reiter, Scrollverhalten, Pagination unter dem Inhalt, Begleiter, Wegweiser, Datenformat unverändert. Keine Änderung an `app.html`.

## Abnahme

Prüfstand (Cowork, 393 px, Skripte `gp_tabs.py`, `gp_tabs2.py`, `gp_tabs3.py`): (1) `?op=diabetischer_fuss_kb&modus=aufklaerung`, `?op=mtp1_arthrodese&modus=aufklaerung`, `?op=scarf&modus=aufklaerung`, `?massnahme=entspannung`, `?massnahme=prp_acp`: alle Reiter genau 132 × 40 px, kein Reiter mit `substring`-Kürzung, Text zweizeilig zentriert, Nummer nie allein in der ersten Zeile; (2) aktiver Reiter weiterhin gefüllt (`var(--c-main)`, weiß, fett); (3) Seitentitel in Großbuchstaben über dem Inhalt der Artikelansicht auf jedem Reiter, in der Maßnahmenansicht wie bisher; (4) alle 827 Reitertitel als `.reiter` gemessen: höchstens die 28 bekannten Titel enden mit „…“, davon keiner aus `diabetischer_fuss_kb`; (5) Tipp-Feedback: `is-pressed` beim Drücken eines Reiters; (6) JSX transpiliert, keine Konsolenfehler; drei Referenzartikel (chevron, charcot_kb, syndesmose_kb) rendern mit identischem Inhaltstext, nur ergänzt um die Titelzeile.

Am Handy: Infomaterial → Diabetisches Fußsyndrom: alle acht Reiter gleich groß, „3. Diagnostik & Risikoeinteilung“ und „7. Die tägliche Pflege des Fußes“ in zwei Zeilen vollständig; OP-Technik MTP1-Arthrodese: Reiter 3 mit Silbentrennung oder „…“, Titel darunter vollständig in Großbuchstaben; eine Maßnahme (z. B. PRP/ACP): Reiter gleich groß, „Übersicht“ und „Kosten“ in einem gleich großen Feld.

Deploy: Push `fusstrack.html`.
