# Kurs Python Basic
## Übungsaufgaben
Mit den folgenden Aufgaben wird das bisher erlente geprüft.

### Aufgabe 1 

Erstelle ein Skript, welches man mit einem Parameter aufrufen kann.
Als Parameter wird der Name eines Kunden übergeben. Dieser soll anstelle des Platzhalters {% Kundenname %} in den 
folgenden Text eingefügt werden. Als Resultat wird eine Datei mit dem Namen "Brief_< datum: d_m_y >_< Kundenname >.txt" und 
dem Textinhalt geschrieben.


##### Brieftext
```
Sehr geehrter Herr {% Kundenname %}

Besten Dank für Ihre Bestellung!
Wir werden uns in kürze bei Ihnen melden um den Auslieferungstermin zu vereinbaren.

Freundliche Grüsse
Ihr Heizungsspezialist
```

##### Hilfe
Für Datum verwende den folgenden Import

`from datetime import datetime`

### Aufgabe 2

Erstelle ein Skript, dass regelmässig (1xpro Minute) den Speicherplatz der Festplatte prüft und den noch freien Speicherplatz 
in eine Log-Datei schreibt.

##### Hilfe
Für die Speicherplatzprüfung können sie die library shutil nutzen

`import shutil`