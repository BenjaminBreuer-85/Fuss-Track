# Auftrag Fuss-Track: Nachbesserung Fortsetzen-Karte und Navigationsleiste (vier Punkte)

Stand 19.09.2026, Cowork-Sitzung. Entscheidung des Autors 19.09.2026 („setze um wie dein Vorschlag") nach der Gegenprobe des Commits 526e342 (Prüfstand-Bericht Abschnitt 25). Datei `fusstrack.html`, Ausgangsstand Commit 526e342 (681.631 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## 1. Das X der Fortsetzen-Karte ist in der Mitte nicht tippbar (Fehler)

Befund: `document.elementFromPoint` in der Spalte des X trifft bei y = 4 px und ab y = 26 px den Knopf `.fs-x`, dazwischen (y = 10 bis 24 px) aber `.fs-label` („Ihr OP-Begleiter"). Ein echter Tipp auf die X-Mitte kommt bei der Karte an (`onClick={onFortsetzen}`, Z. 935) und öffnet den Begleiter statt des Dialogs. Ursache: `.fs-label` hat `opacity: 0.8` (Z. 250) und bildet damit einen eigenen Stapelkontext, der in DOM-Reihenfolge nach dem absolut gesetzten X (Z. 937, CSS Z. 264) gemalt wird; wegen `padding-right: 40px` (Z. 263) reicht sein Kasten bis unter das X. Die Abnahme mit programmatischem Klick auf das Element hat das nicht gezeigt, weil sie die Trefferprüfung umgeht.

Änderung: `.fs-x` bekommt `z-index: 1` (Z. 264 ff.). Nichts anderes an der Karte.

## 2. Leiste in Karten mit Innenabstand bis zum Kartenrand (Nachtrag (a) vom 19.09.)

Befund (von der Code-Sitzung gemeldet, auf dem Prüfstand bestätigt): Wo die `NavLeiste` innerhalb einer `.card` mit `padding: 24` sitzt, bleiben dem Titel bei 393 px nur 131 px statt 169 px; „Frische Außenbandverletzung OSG" wird trotz zweizeiligem Umbruch gekürzt („Außenbandver…"). Betroffen sind die sechs Aufrufe als erstes Kind einer Karte: Nicht-OP-Begleiter Z. 1805, Krankheitsbild Z. 2152 und 2249, Eingriffswahl Z. 2883, 2929 (Baum) und 2977 (Begleitung).

Änderung: eine CSS-Regel, kein Eingriff in die Aufrufe:

```
.card > .nav-leiste:first-child { margin: -24px -24px 12px; border-radius: 10px 10px 0 0; }
```

Die Leiste reicht damit an den Kartenrand (gleiche Breite wie die frei stehende Leiste, Titel bei 393 px wieder 169 px), die obere Rundung folgt der Karte (`borderRadius: 10`), `sticky` bleibt (der Stapelkontext der Karte ändert sich nicht). Der Innenabstand der Karte bleibt für den Inhalt darunter erhalten. Wenn eine der sechs Karten einen anderen Innenabstand als 24 px hat, bitte die Regel je Karte anpassen und in der Vollzugsmeldung nennen.

## 3. Wegweiser ohne doppelten Titel (achter `ohneTitel`-Aufruf)

Befund: Z. 1280 `NavLeiste titel="Beschwerde-Wegweiser"` und Z. 1281 `Header … titel="Beschwerde-Wegweiser"` zeigen den Titel zweimal untereinander (Leiste zweizeilig, darunter `h1` mit Untertitel). Änderung: Z. 1281 bekommt `ohneTitel={true}`; da `showSwitcher` dort `false` ist, rendert der `Header` dann nichts (Z. 3058 ff.). Der Untertitel „Ihr Begleiter bei Erkrankungen von Fuß und Sprunggelenk" entfällt in dieser Ansicht; auf der Startseite bleibt er.

## 4. Schmale Zeile auch bei `?home=1`

Befund: „⌂ Start" führt aus dem Begleiter auf `?home=1` (`navZurStartseite`), und dieser Zweig (Z. 1261–1270) rendert `LandingView` ohne Karte und ohne Zeile. Wer im Begleiter auf „⌂ Start" tippt, findet keinen direkten Rückweg außer der Kachel „Begleiter". Änderung: im `home`-Zweig zwischen `Header` und `LandingView` bei bestehender Sitzung immer die schmale Zeile, nie die Karte:

```
{hasSession && !urlParams.massnahme && !urlParams.nonop && !urlParams.kb && (
  <FortsetzenZeile session={session} onFortsetzen={function(){ setFortsetzen(true); }} />
)}
```

Tippen auf „Weiter ›" muss aus `?home=1` in den Begleiter führen. Heute greift `fortsetzen` dort nicht, weil der `home`-Zweig (Z. 1261) vor dem Begleiter-Zweig steht und `fortsetzen` nicht prüft. Einfachster Weg: die Bedingung in Z. 1261 auf `urlParams.home === "1" && !fortsetzen` erweitern; dann fällt die Anzeige nach dem Tippen in den Begleiter-Zweig wie beim Aufruf ohne Parameter (dort gilt bereits `!hasValidUrlParams && hasSession && !fortsetzen`, Z. 1423). Wenn die Code-Sitzung einen anderen Weg wählt (etwa `history.replaceState` ohne `home`), bitte in der Vollzugsmeldung nennen. Die Ausblendungsregel `karteZeigen` bleibt unberührt; die Karte selbst erscheint weiterhin nur beim Aufruf ohne Parameter.

## 5. Nichts anderes

`KarteDialog`, `karteZeigen`, `FortsetzenZeile`, `resetSession`, Deep-Links, Phasenlogik, `phasen.json` unverändert. Chip „Neu" vor „Bitte OP-Datum eintragen" und das Rot `#C62828` bleiben (Entscheidung des Autors 19.09.2026).

## Abnahme

Cowork-Prüfstand (393 px, Sitzung `chevron/einfach` gestellt): (1) `elementFromPoint` in der X-Spalte trifft bei y = 4, 10, 18, 26 und 34 px jeweils `.fs-x`; ein Tipp auf die X-Mitte öffnet den Dialog, nicht den Begleiter. (2) Nicht-OP „Frische Außenbandverletzung OSG": Titel vollständig auf zwei Zeilen, Leiste bündig mit dem Kartenrand, obere Ecken rund, sticky beim Scrollen; Krankheitsbild und Eingriffswahl ebenso. (3) Wegweiser: genau ein „Beschwerde-Wegweiser" (in der Leiste), kein `h1`. (4) `?home=1` mit Sitzung: schmale Zeile „Ihr OP-Begleiter: Chevron/Akin-Osteotomie · Weiter ›", nie die Karte; Tippen führt in den Begleiter; ohne Sitzung keine Zeile. Aufruf ohne Parameter: Karte wie bisher. Keine Konsolenfehler, 393 und 1280 px.

Abnahme des Autors am Handy: Startseite mit laufendem Begleiter → X in der Mitte tippen → Dialog „Hinweis zum Begleiter" (nicht der Begleiter) → „Nur ausblenden" → schmale Zeile; im Begleiter „⌂ Start" → Startseite mit schmaler Zeile → „Weiter ›" → Begleiter. Wegweiser öffnen: Titel nur einmal. Infomaterial → „Frische Außenbandverletzung OSG": Titel vollständig.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern der vier Änderungen.
