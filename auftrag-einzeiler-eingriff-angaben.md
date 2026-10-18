# Auftrag Fuss-Track (Einzeiler): Begleitung nennt den Eingriff „nach Ihren Angaben“ statt „vom Arzt vorausgewählt“

Stand 18.10.2026, Cowork-Sitzung. Datei `fusstrack.html`, Ausgangsstand e20fde5 (700.745 B, md5 df555e88…; Zeilenangaben darauf). Befund aus der Bildschirmaufnahme vom 18.10.2026 (`claude/bewertung-video-begleiter-2026-10-18.md`, Mangel 1), Freigabe des Autors 18.10.2026. Ein Commit, Vollzugsmeldung mit Commit-Hash und Zeilennummern.

## Befund

Die Begleitung (`DatumEingabe`, Z. 4469 ff.) zeigt vor der Terminabfrage „Ihr Eingriff (vom Arzt vorausgewählt)“ (Z. 4485) und „Diese Auswahl wurde von Ihrem Arzt festgelegt“ (Z. 4490), ohne Bedingung. Tatsächlich entsteht die Variante in jedem Weg aus den Antworten des Patienten im Entscheidungsbaum („Welcher Eingriff ist bei Ihnen geplant?“, „Wird zusätzlich an einer Sehne operiert?“, „Welche Belastung hat Ihr Behandler für die ersten Wochen festgelegt?“), auch im QR-Weg aus dem Sprechstundenbrief: Die Kurzlinks tragen `op` und `ctx=begleiter`, aber keine Variante; der Schalter „Zum OP-Begleiter“ führt ohne Variante über `kb` in den Baum (Z. 1432), und `goBegleitung` (Z. 2497–2499) baut die Adresse nur aus `op` und `var`. Es gibt heute keinen Weg, auf dem eine Variante vom Behandler vorgegeben ankommt. Der Satz behauptet also eine ärztliche Festlegung, die so nicht stattgefunden hat.

## Änderung

Z. 4485:

```
        <div className="card-label">Ihr Eingriff (nach Ihren Angaben)</div>
```

Z. 4490:

```
        <div className="preselect-hint">Grundlage ist das, was Ihr Behandler mit Ihnen besprochen hat. Fragen Sie dort nach, wenn etwas nicht passt.</div>
```

Keine Bedingung, kein Sitzungsfeld: Solange keine Variante per Adresse vorgegeben wird, gilt der Satz in allen Wegen. Sollte später ein Brief-QR mit Variante eingeführt werden, kann die alte Formulierung an `urlParams.ctx === "begleiter" && urlParams.var` gebunden zurückkommen; das ist dann ein eigener Auftrag.

## Nichts anderes

Entscheidungsbaum, Terminabfrage, Verlauf, „Ihr Eingriff erfolgt:“ (Z. 4612), Infomaterial, Wegweiser unverändert.

## Abnahme

Prüfstand: Begleiter → OP-Begleiter → Knick-Senk-Fuß → Korrektur des Fersenbeins → Verschiebeosteotomie → Nein → Teilbelastung: Karte zeigt „Ihr Eingriff (nach Ihren Angaben)“ und den neuen Hinweis; Deep-Link `?op=…&var=…` gleich; kein Vorkommen von „vom Arzt vorausgewählt“ oder „von Ihrem Arzt festgelegt“ mehr im Code. JSX transpiliert, keine Konsolenfehler.

Am Handy: denselben Weg wie im Video gehen; die Karte vor der Terminabfrage lesen.

Deploy: Push `fusstrack.html`.
