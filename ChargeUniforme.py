__author__ = 'pierrebeldor'

import Chargement


class ChargeUniforme(Chargement):
    def __init__(self, charge):
        super(ChargeUniforme, self).__init__(charge)

    def calcul_reaction_a(self, longueur, support_type):
        if support_type == 1 or support_type == 4:
            return self.get_charge() * longueur / 2.0
        elif support_type == 2:
            return self.get_charge() * longueur
        elif support_type == 3:
            return (5.0 / 8.0) * self.get_charge() * longueur
        else:
            print ' Le type de support n\'est pas valide.!!!!!!'
            return 0.0

    def calcul_reaction_b(self, longueur, support_type):
        if support_type == 1 or support_type == 4:
            return self.get_charge() * longueur / 2.0
        elif support_type == 2:
            return 0.0
        elif support_type == 3:
            return 3.0 * self.get_charge() * longueur / 8.0
        else:
            print ' Le type de support n\'est pas valide.!!!!!!'
            return 0.0

    def calcul_moment(self, longueur,  x, support_type):
        if support_type == 1 or support_type == 4:   # poutre sur 2 appuis simple ou poutre encastree aux 2 extremites
            return 0.5 * self.get_charge() * x * (longueur - x)
        elif support_type == 2:     # Cantilever avec l'encastrement en A
            return self.get_charge() * ((longueur - x) ** 2) / (2.0 * longueur)
        elif support_type == 3:   # poutre encastree a l'extremite A et simplement appuiee a l'extremite B
            return self.get_charge() * ((x ** 2.0) / 2.0 - (5.0 / 8.0) * (longueur * x) + (longueur ** 2) / 8.0)
        elif support_type == 4:  # poutre encactree aux 2 extremites
            return self.get_charge() * ((longueur * x / 2.0) - (x ** 2.0) / 2.0 - (longueur ** 2.0) / 12.0)
        else:
            print ' Le type de support n\'est pas valide.!!!!!!'
            return 0.0      # pas encore implementee