# Auftrag Fuss-Track: Kopfzeile „Information" statt „Aufklärung"

Stand 20.09.2026, Cowork-Sitzung. Handy-Abnahme des Autors 20.09.2026 (Artikel „Fehlstellungen der Kleinzehen", in der App geöffnet): In der Kopfzeile steht „Aufklärung". Der Begriff soll in der Patienten-App nicht als Ansichtstitel erscheinen, weil die Texte das ärztliche Aufklärungsgespräch ergänzen und nicht ersetzen. Datei `fusstrack.html`, Ausgangsstand Commit f81f170 (682.510 Byte, Zeilenangabe darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Z. 1415: `<NavLeiste titel={IN_APP_NAV ? "Aufklärung" : "Information"} />`. `IN_APP_NAV` (Z. 1316) ist wahr, wenn der Artikel aus der App heraus geöffnet wird (`nav=1` oder `kb=`), also aus der Infomaterial-Übersicht, dem Begleiter oder über „Mehr zum Krankheitsbild →" (Z. 4255). Beim Aufruf über QR-Code oder Kurzlink steht bereits „Information". Derselbe Artikel trägt also je nach Einstieg zwei Titel. Andere sichtbare Stellen mit „Aufklärung" gibt es nicht (der Umschalter Z. 3061 f. heißt „ⓘ Infomaterial zum Krankheitsbild ansehen" / „→ Zum Patientenbegleiter"; Z. 3260 „Aufklärungsgespräch" meint das Gespräch und bleibt).

## Änderung

Z. 1415: `<NavLeiste titel="Information" />`. Sonst nichts; `IN_APP_NAV` wird weiter für Navigation, Fokus-Kopf und Fußtext gebraucht (Z. 1416–1420).

## Abnahme

Cowork-Prüfstand: `?op=kleinzehen_kb&modus=aufklaerung&nav=1` und ohne `nav=1` zeigen beide „Information"; OP-Artikel `?op=chevron&modus=aufklaerung&nav=1` ebenso; Beschwerde-Wegweiser und Wissen unverändert; keine Konsolenfehler.

Abnahme des Autors am Handy: Infomaterial → Krankheitsbilder → beliebiger Artikel: Kopfzeile „Information".

Vollzugsmeldung bitte mit Commit-Hash.
