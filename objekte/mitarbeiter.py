class Mitarbeiter:
    lohn = 0
    name = ""

    def __init__(self, mitarbeiter_name):
        self.name = mitarbeiter_name
        print(f"Mitarbeiter {self.name} erstellt")

    def eingabe_lohn(self, mitarbeiter_lohn):
        self.lohn = mitarbeiter_lohn
        print(f"Mitarbeiter {self.name} hat einen Lohn von {self.lohn}")

    def __del__(self):
        print("Mitarbeiter entlassen")