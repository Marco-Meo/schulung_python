# Importe
from argparse import ArgumentParser
from datetime import datetime


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.description = "Erstellung Auftragsbestätigung als Brief"
    parser.add_argument("-n", "--name", dest="kunde", default="Musterfirma")
    args = parser.parse_args()

    brieftext = """Sehr geehrter Herr {% Kundenname %}

Besten Dank für Ihre Bestellung!
Wir werden uns in kürze bei Ihnen melden um den Auslieferungstermin zu vereinbaren.

Freundliche Grüsse
Ihr Heizungsspezialist"""

    brieftext = brieftext.replace('{% Kundenname %}', args.kunde)
    datum_heute = datetime.now().strftime("%d_%m_%y")
    datei_name = f'Brief_{datum_heute}_{args.kunde}.txt'
    with open(datei_name, 'w') as file:
        file.writelines(brieftext)
