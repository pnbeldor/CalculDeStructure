__author__ = 'pierrebeldor'

#from Chargement import Chargement
from ChargeConcentree import ChargeConcentree
from ChargeUniforme import ChargeUniforme

class Poutre:
    def __init__(self, type_appui, longueur, chargement):
        self.__type_appui = type_appui
        self.__longueur = longueur
        self.__chargement = chargement      # a 2 dimensional list where the first element
        # is the charge and the second element is the type of charge ex:[120, 1]
        self.__reaction_a = 0.0
        self.__reaction_b = 0.0
        self.__moment = {}              # create an empty dictionary

    #       Getters and setters
    def set_type_appui(self, type_appui):
        self.__type_appui = type_appui

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_chargement(self, chargement):
        self.__chargement = chargement

    def set_reaction_a(self, reaction_a):
        self.__reaction_a = reaction_a

    def set_reaction_b(self, reaction_b):
        self.__reaction_b = reaction_b

    def get_type_appui(self):
        return self.__type_appui

    def get_longueur(self):
        return self.__longueur

    def get_chargement(self):
        return self.__chargement

    def get_reaction_a(self):
        return self.__reaction_a

    def get_reaction_b(self):
        return self.__reaction_b

    def calculer_poutre(self):
        for index in range(0, int(self.__longueur + 1), 1):
            self.__moment[index] = 0.0

        self.__moment[self.__longueur / 2.0] = 0.0

        for charge in self.__chargement:
            # La charge est de la forme [type, charge] pour la charge uniforme
            # et [type, charge,a] pour la charge concentree
            if charge[0] == 1:
                chargement = ChargeConcentree(charge[1], charge[2])
            elif charge[0] == 2:
                chargement = ChargeUniforme(charge[1])

            self.__reaction_a += chargement.calcul_reaction_a(self.__longueur, self.__type_appui)
            self.__reaction_b += chargement.calcul_reaction_b(self.__longueur, self.__type_appui)

            for key in self.__moment:
                new_val = chargement.calcul_moment(self.__longueur, key, self.__type_appui)
                self.__moment[key] += new_val

    def __str__(self):
        print '========================================='
        print '                    POUTRE'
        print '========================================='
        print
        print 'Longueur = ', self.__longueur
        print 'Type d\'appui = ', self.__type_appui
        print 'Reaction A = ', self.__reaction_a
        print 'Reaction B = ', self.__reaction_b
        print ''
        print '------- Moments----------------'
        for key in self.__moment:
            print 'X = ', key, '\t  M = ', self.__moment[key]
        print
        print '-------------END---------------'
        return '  '
