# Vorschlag: Achilles-Serie (Begleiter + Artikel-Abgleich) — Stand 14.08.2026

## ✅ ENTSCHEIDUNGEN BENJAMIN (14.08.)
- haglund_split: Woche 1–2 bereits 20 kg Teilbelastung (wenn Wunde gut und durch
  Behandler freigegeben); Isometrie ab Woche 3 entfällt → betrifft auch die
  Artikel-Slides op_haglund_split_nachbehandlung + op_fhl_nachbehandlung (Entwürfe im Chat)
- (1) Naht: frühe Vollbelastung im Spitzfuß-Walker wie vorgeschlagen
- (2) achilles_nekrose: EIGENER Begleiter (gleiche Bausteine)
- (3) fhl_transfer → Ziel wie haglund_split komplex
- (4) tendoskopie: Vorlauf gekürzt
- NEU: Aufenthalts-Modulator ambulant/stationär für ALLE Begleiter (umgesetzt 14.08.,
  siehe Abschnitt E) — die Achilles-Bausteine werden direkt mit beiden Fassungen gebaut

## E. Aufenthalts-Modulator (14.08. technisch umgesetzt)
- Jeder Begleiter zeigt oben „Ihr Eingriff erfolgt: [Stationär] [Ambulant]";
  Voreinstellung je Eingriff über `aufenthalt_default` in phasen.json, Auswahl wird in
  der Session gespeichert; QR kann optional `&aufenthalt=` mitgeben
- Datenmodell: Bausteine können `intro_ambulant`/`text_ambulant` tragen (Fallback =
  Standardtext); `AUFENTHALT_ERSATZ` tauscht ganze Phasen (Entlassung Tag 2 stationär ↔
  Entlassung am OP-Tag ambulant); Phasen können `nur: stationaer|ambulant` tragen
- Neuer Baustein `entlassung_ambulant` (Entwurf im Chat, Freigabe offen)
- Defaults (Vorschlag, bitte prüfen): ambulant = Vorfuß-/Vollbelastungs-Serie
  (chevron, scarf, youngswick, cheilektomie, mtp1_arthrodese, kleinzehen_pip, dmmo,
  weil, morton, plantarfascie, gastroc, calcaneoplastie, arthrorise, coalitio_cn);
  stationär = alle übrigen 17 (Arthrodesen, TEP, Band, Calcaneus, Knorpel, SMOT, TMT)

Grundlage sind die bestehenden, teils freigegebenen Artikel. Als „Vorlage" gilt das
detaillierte Stufenschema aus op_haglund_split_nachbehandlung und op_fhl_nachbehandlung
(Spitzfußwalker 120°, wochenweises Entfernen der Fersenkeile, 20 kg ab Woche 3,
Vollbelastung im Walker ab Woche 7–8, eigener Schuh mit Silikon-Fersenkeil ab Woche 8,
Rad ab Woche 10, freie Bewegung ab Woche 12).

Evidenz-Check (PubMed): Frühfunktionelle Nachbehandlung mit früher Belastung und
Mobilisierung nach Achillessehnennaht ist sicher und beschleunigt Rückkehr zu Arbeit
und Sport (Massen 2022, doi 10.1530/EOR-22-0072; McCormack 2015, doi
10.1136/bjsports-2015-094935; Netzwerk-Metaanalyse Pisano 2025, doi 10.1002/ksa.12686 —
Re-Ruptur nach offener Naht ~2 %). Nach offener Haglund-OP fand eine große Duke-Kohorte
keinen Outcome-Unterschied zwischen Belastungsprotokollen (Hinton 2025, doi
10.1177/24730114251316554) — das klinikeigene 20-kg-Schema ist damit gut gedeckt.

## A. Vorgeschlagene Begleiter (3 neue Schlüssel)

### 1. haglund_split — „Haglund-OP mit Sehnen-Refixation" (Stufenschema = Vorlage)
- einfach „Refixation allein": Haglund-Abtragung, Sehnen-Split, Refixation
- komplex „mit FHL-Transfer": zusätzlich FHL-Sehnentransfer; identisches Stufenschema,
  ab Woche 8 Kräftigungs-Schwerpunkt kurze Fußbeuger/FHL (aus op_fhl_nachbehandlung)
- Timeline (Tage): 0 Spitzfußwalker-Anlage 120°, Tag+Nacht / 2 Entlassung / 14 Fäden /
  21 Stufe 2 + 20 kg Teilbelastung + Isometrie/Koordination / 35 Stufe 1 / 40 Narbenpflege /
  49 Stufe 0 (90°), Vollbelastung im Walker / 56 eigener Schuh + Silikon-Fersenkeil,
  Physiotherapie ohne forcierte Dorsalflexion / 70 Rad/Ergometer, dosiertes Krafttraining /
  84 freie Bewegung (non-impact), Kontrolle
- Platzhalter THROMBOSE_WOCHEN = 8 (Ruhigstellung bis Ende Woche 8)

### 2. achilles_naht — „Naht der gerissenen Achillessehne" (frühfunktional)
- einfach „perkutane/minimal-invasive Naht", komplex „offene Naht" — NACHBEHANDLUNG IDENTISCH
  (beide Artikel nennen dasselbe Vacoped-Schema); Varianten nur zur sauberen QR-Zuordnung
- Schema wie Vorlage, aber frühere Belastung: Vollbelastung im Spitzfuß-Walker bereits ab
  Woche 1–2 nach Maßgabe der Behandler (statt 2 Wochen Entlastung) — deckt sich mit
  kb_asr_behandlung („frühe Belastung im Stiefel") und der Evidenz oben. ⚠ ENTSCHEIDUNG:
  stimmt das so für eure Klinik, oder erst 20 kg wie bei Haglund?
- Übriger Verlauf identisch zur Vorlage (Keile Wo 3/5/7, Schuh+Keil Wo 8, Rad Wo 10, Wo 12 frei)

### 3. tendoskopie_achilles — „Achillessehnen-Tendoskopie" (frühfunktional, leicht)
- EINE Variante „Standard"; kurzer Verlauf nach op_tendoskopie_achilles_nachbehandlung:
  0 OP-Tag / 1 Mobilisierung mit Aufbau zur Vollbelastung über 2 Wochen an Stützen, früh
  Narbenmassage + tägliche Dehnübungen / 14 Fäden + Beginn exzentrischer Kräftigung /
  28 sportliche Steigerung (4–8 Wochen, individuell) / 84 Kontrolle
- Vorlauf gekürzt wie bei Morton/Plantarfaszie (ohne Häuslichkeits-/Hilfsmittel-Phasen)?
  ⚠ ENTSCEIDUNG + Frage ambulant/stationär

### Nicht als eigener Begleiter vorgesehen
- achilles_nekrose (offene Sanierung): Nachbehandlung = bei Refixation exakt das
  Haglund-Stufenschema → QR könnte auf haglund_split-Begleiter zeigen ODER eigener
  Schlüssel mit denselben Bausteinen. ⚠ ENTSCHEIDUNG (Toolbox hat aktuell kein Mapping)
- fhl (FHL-Transfer isoliert): über haglund_split komplex abgedeckt; Clinic-Mapping
  fhl_transfer könnte auf haglund_split&var=komplex zeigen. ⚠ ENTSCHEIDUNG
- haglund_mini → calcaneoplastie-Begleiter existiert bereits (Vollbelastungs-Serie)

## B. Neue Bausteine (~10, Wortlaut-Entwürfe folgen nach Strukturfreigabe)
walker_spitzfuss_anlage · entlastung_spitzfuss (Wo 1–2, keine Bewegungsübungen) ·
stufe_spitzfuss_1 (Keil raus, 20 kg, Isometrie) · stufe_spitzfuss_2 · stufe_spitzfuss_3
(90°, VB im Walker) · schuh_fersenkeil (+ defensiver Thromboseschutz-Übergang) ·
training_rad_kraft · freigabe_bewegung_achilles (Wo 12) + kontrolle · fhl_kraeftigung
(nur komplex) · mobilisierung_fruehfunktional_tendoskopie (+ dehnung/exzentrik).
Wiederverwendet: op_tag_ruhiggestellt, abschwellung, entlassung_stationaer,
faden_standard, narbenpflege, hygiene_walker.

## C. Artikel-Änderungen gegenüber den Vorlagen (nur 3 Slides!)
UNVERÄNDERT: op_haglund_split_nachbehandlung, op_fhl_nachbehandlung (= die Vorlage),
op_tendoskopie_achilles_nachbehandlung, alle 5 KB-Artikel (kb_asr_behandlung passt).
GEÄNDERT (Entwürfe im Chat):
1. op_achilles_naht_nachbehandlung — bisher 3 Zeilen → volles Stufenschema
2. op_achilles_perkutan_nachbehandlung — identisch zu 1.
3. op_achilles_nekrose_nachbehandlung — bisher 3 Zeilen → Stufenschema der Refixation
   (= Vorlage) mit Hinweis auf FHL-Variante

## D. Flags
- Artikel fhl, achilles_naht, achilles_perkutan stehen noch auf _entwurf:true —
  Freigabe der GESAMTEN Artikel steht aus, nicht nur der Nachbehandlungs-Slides
- Toolbox-QR: as_naht→achilles_naht und haglund_as_split→haglund_split existieren;
  KEIN OPS/QR-Weg für tendoskopie_achilles, achilles_perkutan, achilles_nekrose
  (Begleiter dann nur über App-Auswahl erreichbar — wie Weil)
- Clinic PATIENT_VARIANTEN für die neuen Schlüssel folgen nach Freigabe
