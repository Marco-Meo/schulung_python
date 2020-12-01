from .mensch import Mensch
from .mitarbeiter import Mitarbeiter

class Verkauf(Mensch, Mitarbeiter):
    bonus = 0
    
    def eingabe_bonus(self, mitarbeiter_bonus):
        self.bonus = mitarbeiter_bonus
        print(f"Mitarbeiter {self.name} hat einen Bonus von {self.bonus} und einen Lohn von {self.lohn}")



if __name__ == '__main__':
    m = Verkauf("Marco Meo")
    m.eingabe_lohn(90000)
    m.eingabe_bonus(10000)
    m.alter = 30
    # m.lohn = 100000
    print(m.alter)
    m = 1
    print(m)