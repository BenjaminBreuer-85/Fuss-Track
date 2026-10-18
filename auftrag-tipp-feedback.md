# Auftrag Fuss-Track: einheitliches Tipp-Feedback für alle tippbaren Elemente

Stand 18.10.2026, Cowork-Sitzung. Datei `fusstrack.html`, Ausgangsstand c0b0b4a (697.621 B, md5 63540dec…; Zeilenangaben darauf). Wunsch des Autors 18.10.2026: „Im Begleiter gibt es noch kein Feedback bei Drücken von Tasten, beispielsweise bei der Auswahl des Krankheitsbildes. Kannst du dies überall in homogener Form einbauen, wie beim Beschwerdefinder?“ Ein Commit, Vollzugsmeldung mit Commit-Hash und Zeilennummern.

## Befund

Die App hat zwei Arten von Rückmeldung, und nur eine davon funktioniert auf dem Handy.

Der Beschwerde-Wegweiser gibt **Zustands-Feedback**: Antwort-Chips wechseln beim Tippen von `btn-secondary` auf `btn-primary` mit „✓ “ davor (Z. 4217–4225), die Fußregion im SVG wechselt Füllung und Rand (Z. 3655–3659). Das funktioniert, weil die Auswahl auf der Seite bleibt und der Zustand sichtbar wird.

Überall sonst gibt es nur **Hover-Feedback** per Maus: `.btn:hover { opacity: .88 }` (Z. 125), `.phase:hover`, `.modal-nav-btn:hover` sowie `onMouseEnter`/`onMouseLeave` auf den Karten (`cardHoverOn`/`cardHoverOff`, Z. 1587–1588 und 2455–2456; Optionskarten Z. 2977–2978 und 3027–3028). Auf dem Handy gibt es kein Hover. Die Karten des OP-Begleiters (Krankheitsbild Z. 2914–2927, Verfahrensauswahl Z. 2970–2980 und 3018–3031), die Menükarten der Startseite (Z. 2495–2525), die Listen im Infomaterial (Z. 2777, 2838) und im Nicht-OP-Begleiter (Z. 1852), die Ampel (Z. 2019), die Schrittlisten (Z. 1931, 2077, 2619, 2631), die Seitentabs der Artikel (Z. 2318) und die Zurück-Leiste (`.zl-btn`, Z. 1037) sind `<div onClick>` ohne `:active`-Regel, ohne Tap-Highlight-Steuerung und ohne Touch-Handler. Dazu kommt eine iOS-Eigenheit: Safari wendet `:active` auf Elemente nur an, wenn irgendwo ein `touchstart`-Listener registriert ist; die App hat keinen. Ergebnis: Beim Tippen auf „Hallux valgus“ im Begleiter passiert sichtbar nichts, bis die nächste Ansicht erscheint.

Bestand: 40 `<button>`, 44 `<div onClick>`, 4 `<span onClick>`, 2 `<a onClick>`, die SVG-Hotspots (Z. 3653 ff.), die Timeline-Phasen (`.phase`, Z. 4697), die Modal-Navigation (`.modal-nav-btn`).

## Änderung

Ein gemeinsames Prinzip für alle tippbaren Elemente: **beim Drücken sichtbar kleiner und getönt, beim Loslassen zurück**, dazu bei Karten, die sofort weiternavigieren, ein kurzes Nachleuchten von 120 ms, damit die Rückmeldung auch bei einem schnellen Tipp gesehen wird. Zustands-Feedback (✓, Farbwechsel) bleibt, wo es heute ist. Der gedrückte Zustand wird nicht über `:active` gesetzt, sondern über eine Klasse `is-pressed`, die ein einziger Zuhörer am Dokument vergibt. Grund: `:active` verhält sich bei Touch je nach Browser verschieden (iOS nur mit `touchstart`-Listener, Chrome mit Verzögerung zur Scroll-Erkennung; auf dem Prüfstand unter Touch-Emulation gar nicht), die Klasse dagegen überall gleich. Auf dem Prüfstand als Prototyp geprüft (`patient_tap`, 8817).

### 1. CSS, nach `.btn-block` (Z. 130)

```
  /* Tipp-Feedback: einheitlich für alle tippbaren Elemente (Buttons, Karten, Chips, Tabs, Listen).
     Die Klasse is-pressed vergibt der Zuhörer beim App-Start (pointerdown/pointerup). */
  button, .btn, .tap, .zl-btn, .phase, .modal-nav-btn, .fs-karte, .fs-schmal {
    -webkit-tap-highlight-color: transparent; touch-action: manipulation;
    user-select: none; -webkit-user-select: none;
  }
  .is-pressed { transform: scale(0.97); transition: transform 0.06s ease-out, background 0.06s, border-color 0.06s; }
  .tap.is-pressed, .zl-btn.is-pressed { background: var(--c-bg) !important; border-color: var(--c-main) !important; }
  .btn-primary.is-pressed { opacity: 0.8; }
  .hotspot.is-pressed { opacity: 0.7; }
  @media (prefers-reduced-motion: reduce) { .is-pressed { transform: none; } }
```

Das `!important` ist nötig, weil die Karten ihren Hintergrund als Inline-Stil tragen (`background: "#fff"`), der sonst gewinnt. `touch-action: manipulation` verhindert Zoom beim Doppeltipp und die Tipp-Verzögerung älterer Browser; `user-select: none` verhindert das Markieren von Kartentext beim längeren Drücken.

### 2. Zuhörer beim App-Start (vor Z. 5519, vor `ReactDOM.createRoot`)

```
    // Tipp-Feedback: ein Zuhörer für alle tippbaren Elemente. Beim Drücken Klasse is-pressed,
    // beim Loslassen oder Abbruch (Wischen) wieder weg. Gilt für Maus, Finger und Stift.
    (function() {
      var SEL = "button, .btn, .tap, .zl-btn, .phase, .modal-nav-btn, .fs-karte, .fs-schmal, .hotspot";
      var cur = null;
      function loslassen() { if (cur) { cur.classList.remove("is-pressed"); cur = null; } }
      document.addEventListener("pointerdown", function(e) {
        var el = e.target && e.target.closest ? e.target.closest(SEL) : null;
        if (!el || el.disabled) return;
        cur = el; el.classList.add("is-pressed");
      }, { passive: true });
      document.addEventListener("pointerup", loslassen, { passive: true });
      document.addEventListener("pointercancel", loslassen, { passive: true });
    })();
```

Ein Wischen zum Scrollen löst `pointercancel` aus und nimmt den Zustand wieder weg; eine Karte leuchtet also nicht auf, wenn nur gescrollt wird. Wechselt die Ansicht beim Klick, ist das gedrückte Element danach nicht mehr im Dokument; das Entfernen der Klasse läuft ins Leere und ist unschädlich.

### 3. Klasse `tap` auf allen tippbaren `<div>`/`<span>`

Jedes `<div onClick>` und `<span onClick>` bekommt `className="tap"` (bei vorhandener `className` anhängen). Liste nach Zeilen (c0b0b4a): 998, 1041, 1611, 1630, 1643, 1646, 1664, 1720, 1752, 1835, 1852, 1931, 2019, 2038, 2077, 2191, 2202, 2208, 2209, 2247, 2318, 2331, 2334, 2381, 2405, 2495, 2506, 2518, 2619, 2631, 2777, 2838, 2870, 2881, 2914, 2970, 3018, 5364, 5373, 5374, 5412. Schon über ihre Klasse erfasst: 946 (`fs-karte`), 983 (`fs-schmal`), 1037 (`zl-btn`), 4697 (`phase`). Nicht: 4797, 5239, 5241, 5454, 5455, 5473, 5474 (Modal-Hintergründe und -Panels, kein Tipp-Ziel). Die `<a onClick>` in Z. 4102 und 4660 bleiben (Textlinks).

### 4. Nachleuchten bei Karten, die sofort navigieren

Ein Helfer, einmal global (z. B. nach Z. 499 bei den globalen Variablen):

```
// Tipp-Feedback für Karten, die sofort weiternavigieren: 120 ms gedrückt zeigen, dann handeln.
function tapThen(e, fn) {
  var el = e && e.currentTarget;
  if (!el || !el.classList) { fn(); return; }
  el.classList.add("is-pressed");
  setTimeout(function() { el.classList.remove("is-pressed"); fn(); }, 120);
}
```

Einsatz nur bei Karten, deren Klick die Ansicht wechselt, also `onClick={function(e){ tapThen(e, function(){ …bisheriger Rumpf… }); }}`: Startseite Z. 2495, 2506, 2518; Begleiter-Wahl Z. 2870, 2881; Krankheitsbild Z. 2914; Verfahrensauswahl Z. 2970 und 3018; Infomaterial Z. 2777, 2838; Nicht-OP-Liste Z. 1852 und 1835; Fortsetzen-Karte Z. 946, 983; Zurück-Leiste Z. 1037, 1041. Nicht bei Zuständen, die auf der Seite bleiben (Ampel, Checklisten, Chips, Tabs, Schrittlisten), dort reicht der gedrückte Zustand. Bei `window.location.href = …` (Z. 2518, 2838) bleibt die Zuweisung im Rumpf, die 120 ms vor dem Seitenwechsel sind gewollt.

### 5. SVG-Hotspots

In `HotSpot` (Z. 3653 ff.) `className: "hotspot"` in `common` ergänzen, damit `.hotspot.is-pressed` greift (`closest` funktioniert auf SVG-Elementen). Die Auswahlfüllung bleibt wie heute.

### 6. Hover-Handler

`cardHoverOn`/`cardHoverOff` und die Inline-`onMouseEnter`/`onMouseLeave` bleiben für die Maus. Auf Touch-Geräten setzt Safari `mouseenter` beim Tippen und lässt es stehen („sticky hover“); das ist unschädlich, weil die Ansicht wechselt. Keine Änderung.

### 7. Nicht enthalten

Vibration (`navigator.vibrate`) ist absichtlich nicht vorgesehen: iOS unterstützt sie im Browser nicht, das Feedback wäre je nach Gerät verschieden und damit nicht homogen. Falls gewünscht, als Folgeauftrag nur für Android.

## Nichts anderes

Inhalte, Begleiter-Logik, Wegweiser-Logik, Zustands-Feedback des Wegweisers, Datenformat unverändert. Keine Änderung an `app.html` (Clinic hat eigene Bedienung).

## Abnahme

Prüfstand (Cowork, Playwright mit Touch-Emulation 393 px, wie im Prototyp): (1) Begleiter → OP-Begleiter → Karte „Hallux valgus“: nach `touchstart` Klasse `is-pressed`, Hintergrund `var(--c-bg)`, Rand `var(--c-main)`, `transform: scale(0.97)`; nach dem Loslassen bleibt die Klasse 120 ms, dann Ansichtswechsel. (2) Startseiten-Karten, Infomaterial-Liste, Artikel-Tabs, Ampel, Checklisten, Schrittlisten, Zurück-Leiste, Wegweiser-Buttons: `is-pressed` beim Drücken, weg nach dem Loslassen. (3) Wegweiser: Chips zeigen weiterhin „✓ “ und `btn-primary`; SVG-Region: `opacity .7` beim Drücken, Füllung nach Auswahl wie bisher. (4) `button:disabled` ohne Effekt. (5) Wischen über eine Karte (pointercancel) lässt keinen gedrückten Zustand stehen. (6) Kein Textmarkieren beim langen Drücken einer Karte. (7) JSX transpiliert, keine Konsolenfehler; Artikel-Rendering (drei Referenzartikel) unverändert.

Am Handy: Begleiter → OP-Begleiter → Krankheitsbild antippen und den Finger kurz halten: Karte wird kleiner und grau-blau, nach dem Loslassen kurz gehalten, dann wechselt die Ansicht. Infomaterial-Liste und Zurück-Taste ebenso. Beschwerde-Wegweiser unverändert.

Deploy: Push `fusstrack.html`.
