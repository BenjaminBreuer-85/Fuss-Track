# Übergabetabelle: Empfehlung → finale URL

Zuordnung der QR-Ziele der Patienten-App. Erzeugt aus `infomaterial.json`,
`bausteine.json`, `nonop.json` und `phasen.json`; Stand siehe Git-Historie.
Diese Datei ist die Übergabe an die Clinic-Sitzung für die Konservativ-Map.

Basis-URL: `https://patienten.fuss-track.de/fusstrack.html`

## Leitkonzept

- **OP indiziert** → ein Code auf die OP-Aufklärung. Krankheitsbild und
  Begleiter sind von dort erreichbar, kein zweiter Code.
- **Keine OP** → ein Code auf den Krankheitsbild-Artikel, mit `thema`-Anker
  auf den konservativen Abschnitt.
- **Der Begleiter bekommt nie einen eigenen Code.**

## Route K — Krankheitsbild (konservativ informieren)

    ?op=<artikel>&modus=aufklaerung&thema=<konservativ-slide>

Der `thema`-Teil ist optional; ohne ihn öffnet der Artikel auf dem Überblick.
Ein unbekannter Anker öffnet den Artikel von Beginn an und zeigt einen
sichtbaren Hinweis — der Artikel geht nicht verloren.

43 der 47 Artikel haben einen eigenständigen konservativen Abschnitt. Bei vier
Artikeln zeigt der Anker auf einen **gemeinsamen Behandlungsabschnitt**, der
konservatives und operatives Vorgehen zusammenfasst — dort landet der Patient
nicht ausschließlich beim nicht-operativen Teil:

- `achilles_riss_kb` → `kb_asr_behandlung` („Behandlung")
- `osteoporose_kb` → `kb_ost_behandlung` („Behandlung")
- `plantarer_fersenschmerz_kb` → `kb_pfs_behandlung` („Diagnostik & Behandlung")
- `usg_arthrose` → `usg_umschalter` („Behandlung nach betroffenem Gelenk")

| Krankheitsbild | Artikel-Key | Konservativ-Anker |
|---|---|---|
| Achillessehne — Mid-Portion-Tendinopathie | `achilles_midportion_kb` | `kb_amid_konservativ` |
| Achillessehne — insertionsnahe Tendinopathie | `achilles_insertional_kb` | `kb_ains_konservativ` |
| Achillessehneninsuffizienz | `achilles_insuffizienz_kb` | `kb_asi_konservativ` |
| Achillessehnenriss (akute Ruptur) | `achilles_riss_kb` | `kb_asr_behandlung` |
| Achillodynie (Achillessehnenschmerz) | `achillodynie_kb` | `kb_achillo_konservativ` |
| Arthrose des unteren Sprunggelenks | `usg_arthrose` | `usg_umschalter` |
| Baxter-Neuropathie | `baxter_kb` | `kb_baxter_konservativ` |
| CRPS am Fuß | `crps_kb` | `kb_crps_konservativ` |
| Chronische OSG-Instabilität | `clai_kb` | `kb_clai_konservativ` |
| Coalitio | `coalitio_kb` | `kb_coalitio_konservativ` |
| Fraktur des Processus anterior calcanei | `proc_ant_calc_kb` | `kb_pac_konservativ` |
| Frische Außenbandruptur des OSG | `aussenbandruptur_kb` | `kb_ablr_konservativ` |
| Gicht (am Fuß / Podagra) | `gicht_kb` | `kb_gicht_konservativ` |
| Hallux limitus | `hallux_limitus_kb` | `kb_hlimitus_konservativ` |
| Hallux rigidus | `hallux_rigidus` | `hr_konservativ` |
| Hallux valgus | `hallux_valgus` | `hv_konservativ` |
| Hohlfuß (Pes cavus) | `hohlfuss_kb` | `kb_cavo_konservativ` |
| Jogger's Foot | `jogger_kb` | `kb_jogger_konservativ` |
| Kindlicher Knick-Senk-Fuß (Pes planovalgus) | `kindl_ppv_kb` | `kb_kppv_konservativ` |
| Kindlicher/juveniler Hallux valgus | `juveniler_hv_kb` | `kb_jhv_konservativ` |
| Knick-Senk-Fuß / Pes planovalgus (Erwachsene) | `ppv_ksf` | `ppv_konservativ` |
| Metatarsalgie | `metatarsalgie_kb` | `kb_metatarsalgie_konservativ` |
| Metatarsus primus elevatus | `mpe_kb` | `kb_mpe_konservativ` |
| Morbus Köhler I (Kahnbein-Osteonekrose) | `koehler1_kb` | `kb_k1_konservativ` |
| Morbus Köhler-Freiberg (Mittelfußkopf-Osteonekrose) | `freiberg_kb` | `kb_frb_konservativ` |
| Morbus Ledderhose | `ledderhose_kb` | `kb_ledder_konservativ` |
| Morbus Renander (Sesambein-Osteonekrose) | `renander_kb` | `kb_ren_konservativ` |
| Morbus Sever (Fersen-Apophysitis) | `sever_kb` | `kb_sev_konservativ` |
| Morton-Neurom | `morton_neurom_kb` | `kb_mn_konservativ` |
| Müller-Weiss-Syndrom | `mueller_weiss_kb` | `kb_mw_konservativ` |
| OSG-Arthrose | `osg_arthrose` | `osg_behandlung` |
| Os peroneum / POPS | `pops_kb` | `kb_pops_konservativ` |
| Os tibiale externum | `ote_kb` | `kb_ote_konservativ` |
| Osteochondrale Läsion des Talus | `olt_kb` | `kb_olt_konservativ` |
| Osteoporose und Osteopenie | `osteoporose_kb` | `kb_ost_behandlung` |
| Peronealsehnen-Luxation | `peroneal_luxation_kb` | `kb_plux_konservativ` |
| Peronealsehnen-Riss | `ptr_kb` | `kb_ptr_konservativ` |
| Plantarer Fersenschmerz | `plantarer_fersenschmerz_kb` | `kb_pfs_behandlung` |
| Plantarfasziitis (Fersensporn) | `plantarfasziitis_kb` | `kb_pf_konservativ` |
| Proximale Fraktur des 5. Mittelfußknochens | `mfk5_fraktur_kb` | `kb_mfk5_konservativ` |
| Stressfraktur & Knochenmarködem | `stressfraktur_kmoe_kb` | `kb_stressfx_konservativ` |
| TMT-I-Instabilität (erster Strahl) | `tmt1_instabilitaet_kb` | `kb_tmt1_konservativ` |
| Tarsaltunnelsyndrom | `tarsaltunnelsyndrom_kb` | `kb_tts_konservativ` |
| Tibialis-anterior-Sehnenruptur | `tibialis_ant_ruptur_kb` | `kb_tar_konservativ` |
| Turf Toe (Großzehengrundgelenk-Verletzung) | `turf_toe_kb` | `kb_turf_konservativ` |
| Unguis incarnatus (eingewachsener Nagel) | `unguis_incarnatus_kb` | `kb_ung_konservativ` |
| Vorderes Tarsaltunnelsyndrom | `vorderes_tts_kb` | `kb_vtts_konservativ` |

## Route O — Operation

    ?op=<eingriff>&var=<variante>&modus=aufklaerung&kbinfo=<kb-artikel>

`op`+`var` schalten den Schalter „→ Zum Patientenbegleiter" frei.
`kbinfo` erzeugt den Rückweg „← Zum Krankheitsbild: …" und wandert beim
Wechsel in den Begleiter mit.

| Eingriff | QR-Ziel | `kbinfo` |
|---|---|---|
| Chevron/Akin-Osteotomie | `?op=chevron&var=einfach&modus=aufklaerung` | `hallux_valgus` |
| Chevron/Akin-Osteotomie mit Zusatzeingriff | `?op=chevron&var=komplex&modus=aufklaerung` | `hallux_valgus` |
| OSG-Arthrodese — Teilbelastung | `?op=osg_arthrodese&var=einfach&modus=aufklaerung` | `osg_arthrose` |
| OSG-Arthrodese — Entlastung | `?op=osg_arthrodese&var=komplex&modus=aufklaerung` | `osg_arthrose` |
| OSG-Prothese | `?op=osg_tep&var=einfach&modus=aufklaerung` | `osg_arthrose` |
| OSG-Prothese mit Zusatzeingriff | `?op=osg_tep&var=komplex&modus=aufklaerung` | `osg_arthrose` |

Für OP-Artikel **ohne** Begleiter lautet die Route
`?op=<artikel>&modus=aufklaerung&kbinfo=<kb-artikel>` ohne `var`.
Der Begleiter-Schalter erscheint dort nicht (geprüft).

## Konservative Maßnahmen

    ?massnahme=<key>

| Maßnahme | Key | verweist auf Programm |
|---|---|---|
| Allgemeine Maßnahmen bei Verschleiß (Arthrose) | `allg_verschleiss` | — |
| Botulinumtoxin (Botox) bei Plantarfasziitis | `botox_plantar` | — |
| Eigenübungen bei Plantarfasziitis / Fersensporn | `uebungen_plantarfasziitis` | `plantarfasziitis` |
| Eigenübungen beim Hallux valgus | `uebungen_hallux_valgus` | `hallux_valgus` |
| Eigenübungen beim Knick-Senk-Fuß | `uebungen_knicksenkfuss` | `knicksenkfuss` |
| Einlagen | `einlagen` | — |
| Entspannungstechniken | `entspannung` | — |
| Ernährung bei Erkrankungen des Bewegungsapparates | `ernaehrung_bewegung` | — |
| Ernährung bei Gicht | `ernaehrung_gicht` | — |
| Exzentrische Kräftigung der Achillessehne (Tendoloading) | `achilles_tendoloading` | — |
| Hyaluronsäure-Injektion (=Spritze ins Gelenk) | `hyaluronsaeure` | — |
| Iloprost und Bisphosphonate (bei Osteochondrosis dissecans) | `iloprost_bisphosphonate` | — |
| Infiltrationen und Injektionen | `infiltrationen` | — |
| LIPUS (=niederintensiver gepulster Ultraschall) | `lipus` | — |
| Low-Level-Lasertherapie (LLLT) | `lllt` | — |
| Nachtschiene | `nachtschiene` | — |
| Nahrungsergänzungsmittel | `nahrungsergaenzung` | — |
| Naturheilkundliche Schmerztherapie (Phytoanalgesie) | `phytoanalgesie` | — |
| Neuromuskuläres Training | `neuromuskulaer_aussenband` | `aussenband_konservativ` |
| PRP/ACP (plättchenreiches Plasma / autologes konditioniertes Plasma) | `prp_acp` | — |
| Radiosynoviorthese (RSO) | `rso` | — |
| Schmerztherapie bei und nach einer Operation | `schmerztherapie_op` | — |
| Short-Foot-Übungen | `short_foot` | — |
| Stoßwellentherapie (extrakorporale Stoßwelle, ESWT) | `stosswelle` | — |
| Vitamin-D3-Therapie | `vitamin_d3` | — |
| Wadenmuskeldehnung | `waden_dehnung` | `wadenmuskeldehnung` |

## Übungsprogramme (Non-OP-Begleiter)

    ?nonop=<key>

| Programm | Key | erreichbar aus |
|---|---|---|
| Frische Außenbandverletzung OSG | `aussenband_konservativ` | `aussenbandruptur_kb` |
| Achillodynie nicht-insertional | `achillodynie_midportion` | `achilles_midportion_kb` |
| Achillodynie insertional | `achillodynie_insertion` | `achilles_insertional_kb` |
| Knick-Senk-Fuß | `knicksenkfuss` | Maßnahme `uebungen_knicksenkfuss` |
| Hallux valgus | `hallux_valgus` | Maßnahme `uebungen_hallux_valgus` |
| Plantarfasziitis | `plantarfasziitis` | Maßnahme `uebungen_plantarfasziitis` |
| Wadenmuskeldehnung | `wadenmuskeldehnung` | Maßnahme `waden_dehnung` |
| Chronische Sprunggelenkinstabilität | `sprunggelenk_instabilitaet` | `clai_kb` |
| Hallux rigidus (Frühstadium) | `hallux_rigidus` | `hallux_rigidus` |
| Sprunggelenkarthrose | `sprunggelenk_arthrose` | `osg_arthrose` |

## Fehlerverhalten

| Fall | Verhalten |
|---|---|
| `?massnahme=`, `?nonop=`, `?kb=` mit unbekanntem Wert | Auffangseite |
| `?op=` mit unbekanntem Wert im Aufklärungs-Modus | Auffangseite |
| `?thema=` mit unbekanntem Anker | Artikel ab Seite 1 + sichtbarer Hinweis |
| `?kbinfo=` mit unbekanntem Wert | Rückweg-Link entfällt still |

## Redaktionsnotizen

**1. Key-Diskrepanz `neuromuskulaer_aussenband`.** Die Maßnahme heißt
inzwischen „Neuromuskuläres Training" und ist nicht mehr außenbandspezifisch;
der Key trägt den alten Namen weiter. Nach den Kurzlink-Regeln wird er **nicht**
umbenannt. Für die Clinic-Seite: Titel und Key stimmen hier nicht überein.

**2. `op=` ist auch der Träger konservativer Artikel.** Die Krankheitsbild-
Artikel werden über `?op=<artikel>&modus=aufklaerung` adressiert, obwohl es
um keine Operation geht. Das ist gewollt und bleibt so — der Parameter ist die
etablierte, stabile Adresse aller Artikel. Nicht als Fehler behandeln.

**3. Klasse B — Krankheitsbilder mit OP-Verweis, aber ohne Begleiter (19).**
Nach Leitkonzept zeigt der Code bei OP-Indikation auf die OP-Aufklärung; ein
Nachbehandlungs-Begleiter existiert dahinter jedoch nicht. Inhaltslücke, keine
Verlinkungslücke:

- Achillessehne — Mid-Portion-Tendinopathie (`achilles_midportion_kb`)
- Achillessehne — insertionsnahe Tendinopathie (`achilles_insertional_kb`)
- Achillessehneninsuffizienz (`achilles_insuffizienz_kb`)
- Achillessehnenriss (akute Ruptur) (`achilles_riss_kb`)
- Chronische OSG-Instabilität (`clai_kb`)
- Coalitio (`coalitio_kb`)
- Frische Außenbandruptur des OSG (`aussenbandruptur_kb`)
- Hohlfuß (Pes cavus) (`hohlfuss_kb`)
- Kindlicher Knick-Senk-Fuß (Pes planovalgus) (`kindl_ppv_kb`)
- Knick-Senk-Fuß / Pes planovalgus (Erwachsene) (`ppv_ksf`)
- Morton-Neurom (`morton_neurom_kb`)
- Os peroneum / POPS (`pops_kb`)
- Os tibiale externum (`ote_kb`)
- Osteochondrale Läsion des Talus (`olt_kb`)
- Peronealsehnen-Luxation (`peroneal_luxation_kb`)
- Peronealsehnen-Riss (`ptr_kb`)
- Plantarfasziitis (Fersensporn) (`plantarfasziitis_kb`)
- TMT-I-Instabilität (erster Strahl) (`tmt1_instabilitaet_kb`)
- Tarsaltunnelsyndrom (`tarsaltunnelsyndrom_kb`)

**4. Uneinheitliche Beschriftungen.** Dasselbe Ziel
`?massnahme=uebungen_hallux_valgus` heißt in fünf OP-Artikeln anders:
„Fußgymnastik" (`chevron_akin`, `lapidus`), „Fußgymnastik zur Kräftigung der
Fußmuskulatur" (`scarf`, `mica`), „Eigenübungen beim Hallux valgus"
(`juveniler_hv_kb`). Im Artikel `hallux_valgus` ist auf „Zum Übungsprogramm
beim Hallux valgus" vereinheitlicht. Bewusst nicht angeglichen.

**5. Drei tote Slide-Keys (Bestand, nicht aus dieser Arbeit).** Die folgenden
Slides sind in `infomaterial.json` gelistet, fehlen aber in `bausteine.json`
und werden beim Laden still verworfen — die Seite fehlt im Artikel:

- `osg_arthrose` → `osg_op_arthrodese`
- `osg_arthrodese_op` → `osg_arthrodese_quellen`
- `hallux_rigidus` → `hr_quellen` (Artikel zeigt 5 statt 6 Seiten)

**6. Gleiche Schlüssel in verschiedenen Namensräumen.** Ein Schlüssel allein
sagt nicht, worauf er zeigt — erst der Parameter entscheidet. Beim Erzeugen der
Codes deshalb nie nur den Schlüssel übernehmen:

| Schlüssel | Artikel (`?op=`) | Programm (`?nonop=`) | Begleiter-Einstieg (`?kb=`) |
|---|---|---|---|
| `hallux_valgus` | ja | ja | ja |
| `hallux_rigidus` | ja | ja | nein |
| `osg_arthrose` | ja | nein | ja |

`?op=hallux_valgus` öffnet den Krankheitsbild-Artikel, `?nonop=hallux_valgus`
das Übungsprogramm, `?kb=hallux_valgus` die OP-Variantenauswahl im Begleiter.

**7. Zurückgestellt.** Abschnitts-Anker innerhalb der Maßnahmen und
Stufen-Adressen innerhalb der Begleiter-Programme sind bewusst nicht gebaut.
