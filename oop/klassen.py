
class Mitarbeiter:
    lohn = 0
    name = ""

    def __init__(self, n):
        self.name = n
        print(f"Mitarbeiter {self.name} erstellt")

    def eingabe_lohn(self, lohn):
        self.lohn = lohn
        print(f"Mitarbeiter {self.name} erhält {self.lohn} CHF")

    def __del__(self):
        print("Mitarbeiter zerstört")

class Verkauf(Mitarbeiter):
    bonus = 0

    def eingabe_bonus(self, bonus):
        self.bonus += bonus
        print(f"{self.name} hat einen Bonus von {self.bonus} bei einem Lohn von {self.lohn}")