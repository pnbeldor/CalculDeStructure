__author__ = 'Pierre Beldor'
import poutre


class Main():
    # La charge est de la forme [type, charge] pour la charge uniforme
            # et [type, charge,a] pour la charge concentree
    # type = 1 pour la charge concentree et 2 pour la charge uniforme
    charge1 = [1, 72.0, 15.0]
    charge2 = [1, 72.0, 15.0]
    charge3 = [2, 200]
    # charge_list = [charge3]
    charge_list = [charge1, charge2, charge3]

    # 1 pour 2 appuis simple
    # 2 pour cantilever
    # 3 pour encastree en A and simplement suportee an B
    # 4 pur encastree aux 2 extremites

    poutre1 = poutre.Poutre(3, 5.0, charge_list)

    poutre1.calculer_poutre()

    print (poutre1)

Main()