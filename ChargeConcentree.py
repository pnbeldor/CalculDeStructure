__author__ = 'Pierre Beldor'

from Chargement import Chargement


class ChargeConcentree(Chargement):
    def __init__(self, charge, dist_from_a):
        self.__dist_from_a = dist_from_a
        Chargement.__init__(self, charge)

    def set_dist_from_a(self, dist):
        self.__dist_from_a = dist

    def get_dist_from_a(self):
        return self.__dist_from_a

    def calcul_moment(self, longueur,  x, support_type):
        if support_type == 1:   # poutre sur 2 appuis simple
            b = longueur - self.__dist_from_a
            if x < self.__dist_from_a:
                return (self.get_charge() * b / longueur) * x
            else:
                return self.get_charge() * self.__dist_from_a * (1.0 - x / longueur)  # Pa(1-x/l)
        elif support_type == 2:     # Cantilever avec l'encastrement en A
            if x <= self.__dist_from_a:
                return -1.0 * self.get_charge() * (self.__dist_from_a - x)
            else:
                return 0.0
        elif support_type == 3:   # poutre encastree a l'extremite A et simplement appuiee a l'extremite B
            a = self.__dist_from_a
            b = longueur - a

            ma = (self.get_charge() * a * (longueur - a) * (2.0 * longueur - a) / (2.0 * longueur))
             #  * ( 1.0 - (x / longueur))
            #        part1 = self.get_charge() * x * (3.0 * b * (longueur ** 2.0) - (b ** 3.0)) \
            # / (2.0 * (longueur ** 3))
            if x <= self.__dist_from_a:
                return ma * (1.0 - x / longueur)
            else:
                return ma * (1.0 - x / longueur) - self.get_charge() * (x - a)
        elif support_type == 4:
            return self.get_reaction_a() * x - (self.get_charge() * self.__dist_from_a
                                                * ((longueur - self.__dist_from_a) ** 2.0) / (longueur ** 2.0))
        else:
            return 0.0      # pas encore implementee

    def calcul_reaction_a(self, longueur, support_type):
        # return self.__charge*(1.0 - self.__dist_from_a / longueur)
        if support_type == 1:  # 2 appuis simple
            return self.get_charge() * (1.0 - (self.__dist_from_a / longueur))
        elif support_type == 2:     # cantilever avec encastrement en A
            return self.get_charge()
        elif support_type == 3:     # encastree aux 2 extremites
            a = self.__dist_from_a
            ra = self.get_charge() * (longueur - a) * (2.0 * (longueur ** 2.0) + 2.0 * a * longueur - (a ** 2.0))/ (2.0 * (longueur ** 3.0))
         #   return self.get_charge() * (3.0 * (self.__dist_from_a ** 2.0) * longueur - (self.__dist_from_a ** 3.0))\
         #  / (2.0 * (longueur ** 2))
            return ra
        elif support_type == 4:         # enccastree a l'extremite A et simplement appuyee a l'extremite B
            b = longueur - self.__dist_from_a
            return self.get_charge() * ((b ** 2.0) * (3.0 * self.__dist_from_a + b)) / (longueur ** 3.0)
         #   return 0.0      # Need to be implemented
        else:
            print ' Le type de support n\'est pas valide.!!!!!!'
            return 0.0

    def calcul_reaction_b(self, longueur, support_type):
        if support_type == 1:
            return self.get_charge() * (self.__dist_from_a / longueur)
        elif support_type == 2:   # Cantilever with encastrement en A
            return 0.0
        elif support_type == 3:      # Encastree a l'extremite A et simplement appuyee a l'extremite
            b = longueur - self.__dist_from_a
            # return self.get_charge() * (3.0 * b * (longueur ** 2.0) - (b ** 3.0)) / (2.0 * (longueur ** 3.0))
            rb = self.get_charge() * (self.__dist_from_a ** 2.0) * (3.0 * longueur - self.__dist_from_a)\
                 / (2.0 * (longueur ** 3.0))
            return rb
        elif support_type == 4:    # encastree aux deux extremitees
            b = longueur - self.__dist_from_a
            return self.get_charge() * ((self.__dist_from_a ** 2.0) * (3.0 * b + self.__dist_from_a)) / (longueur ** 3.0)
        else:
            print ' Le type de support n\'est pas valide.!!!!!!'
            return 0.0