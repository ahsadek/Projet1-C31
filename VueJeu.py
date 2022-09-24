from Modele import Matrix

class AireDeJeu: 
# adj pour 'aire de jeu'
    def __init__(self):
        self.ligne = Matrix.LONGUEUR

    def afficherMatrix(self, matrix):
        for i in range(0, Matrix.LONGUEUR * Matrix.LARGEUR):
            # a chaque 8 valeur change de ligne
            if i % self.ligne == 0:
                if i != 0:
                    print('\033[0;37;40m\n')

            if matrix.array[i] == 1:
                print('\033[0;37;46m  ', end = '\033[0;37;40m ')
            elif matrix.array[i] == 2:
                print('\033[0;37;41m  ', end = '\033[0;37;40m ')
            elif matrix.array[i] == 3:
                print('\033[0;37;43m  ', end = '\033[0;37;40m ')
            else:
                print('\033[0;37;47m  ', end = '\033[0;37;40m ')
            
        print("\n")

#class VueMenu
class VueMenu:
    def afficherMenu(self) :
        print("Jeu des Daleks")
        print("\n")
        #print("Inserer nom :")
        self.nom = input("Nom du joueur:")
        #print(self.nom)
        print("Choisir mode de jeu pour commencer")#-> Va determiner le mode de teleportage
        print("1 - Facile \n")#si facile le teleporteur transporte docteur sur une case vide  ayant au moins deux cases de distance des Daleks le plus proche
        print("2 - Moyen\n")#  idem mais on ne vérifie pas la proximité de Daleks 
        print("3 - Difficile")#téléportage est complètement aléatoire et donc on peut atterrir sur un Dalek
        self.niveau = input("choix niveau: ")