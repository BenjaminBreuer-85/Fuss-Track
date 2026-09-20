# Auftrag Fuss-Track: „‹ Zurück" im fortgesetzten Begleiter führt auf die Startseite

Stand 20.09.2026, Cowork-Sitzung. Anlass: Handy-Abnahme des Autors 20.09.2026: Wer auf der Startseite die schmale Zeile (oder die Karte) tippt, landet im Begleiter; „‹ Zurück" in der Leiste führt dort nicht einen Schritt zurück, sondern aus der App hinaus (bei ihm zurück in die Clinic-App). Datei `fusstrack.html`, Ausgangsstand Commit 2a2b186 (682.260 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Die Leiste des Begleiters (Z. 1457) hat kein `onBack`; `NavLeiste` nimmt dann `navZurVorseite` (Z. 1018–1023): `history.back()`, wenn ein Verlauf da ist, sonst Startseite. Der Wechsel Startseite → Begleiter über „Weiter im Begleiter" oder „Weiter ›" ist aber kein Seitenwechsel, sondern nur `setFortsetzen(true)` (Z. 1270, 1438, 1441); er legt keinen Verlaufseintrag an. `history.back()` springt darum zum vorigen Dokument, und das ist je nach Weg die Aufklärungsseite, die Clinic-App oder eine ganz andere Seite. Die übrigen Zustandswechsel innerhalb der App (Kacheln, Infomaterial, Nicht-OP, Eingriffswahl) geben der Leiste ein eigenes `onBack` und sind nicht betroffen; der Begleiter per Deep-Link (`?op=…&var=…`) ist ein echter Seitenaufruf, dort bleibt `history.back()` richtig.

## Änderung

Z. 1457: `onBack` nur im fortgesetzten Fall setzen:

```
<NavLeiste onBack={fortsetzen ? function(){ setFortsetzen(false); } : undefined} titel={…wie heute…} />
```

`setFortsetzen(false)` bringt die Anzeige in den Zweig zurück, aus dem sie kam: Startseite ohne Parameter (Karte oder Zeile, Z. 1423 ff.) oder `?home=1` (Zeile, Z. 1265 ff.). Kein Verlaufseintrag nötig, keine Adressänderung. Beim Deep-Link-Einstieg ist `fortsetzen` falsch, dort bleibt alles wie heute.

## Nichts anderes

`navZurVorseite`, `navZurStartseite`, `FortsetzenBanner`, `FortsetzenZeile`, `KarteDialog`, `karteZeigen` unverändert.

## Abnahme

Cowork-Prüfstand (393 px, Sitzung gestellt): (1) Aufruf ohne Parameter → Karte → „Weiter im Begleiter" → „‹ Zurück" → Startseite mit Karte, Adresse unverändert. (2) Karte ausgeblendet → Zeile → „Weiter ›" → „‹ Zurück" → Startseite mit Zeile. (3) `?home=1` → Zeile → „Weiter ›" → „‹ Zurück" → Startseite `?home=1` mit Zeile. (4) Deep-Link `?op=chevron&var=einfach` → „‹ Zurück" wie bisher (`history.back()` beziehungsweise Startseite ohne Verlauf). (5) „⌂ Start" im Begleiter weiter auf `?home=1`. Keine Konsolenfehler.

Abnahme des Autors am Handy: Startseite → Zeile oder Karte tippen → Begleiter → „‹ Zurück": Startseite der Patienten-App, nicht die Clinic.

Vollzugsmeldung bitte mit Commit-Hash und der Zeilennummer.
