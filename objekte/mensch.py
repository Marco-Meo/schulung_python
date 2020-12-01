class Mensch:
    alter = 0
    lohn = 0

    def eingabe_lohn(self, mitarbeiter_lohn):
        self.lohn = mitarbeiter_lohn + 5000
        print(f"Mitarbeiter {self.name} hat einen Lohn von {self.lohn}")