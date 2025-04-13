import random
import time
import os
import sys

# Paramètres du jeu
LARGEUR = 20
HAUTEUR = 10
NB_BOTS = 3
ZONE_RETRAIT = 3

# Cartes et symboles
VIDE = " "
JOUEUR = "🟩"
BORD = "▓"
BALLE = "•"
BOTS = "🟥"
ZONE = "🟦"

# Direction des tirs
DIR_TIR = {
    'z': (-1, 0),
    's': (1, 0),
    'q': (0, -1),
    'd': (0, 1)
}

# Classe représentant le joueur et les bots
class Personnage:
    def __init__(self, x, y, symbole, vie=100):
        self.x = x
        self.y = y
        self.symbole = symbole
        self.vie = vie

    def deplacer(self, dx, dy):
        if 0 <= self.x + dx < LARGEUR and 0 <= self.y + dy < HAUTEUR:
            self.x += dx
            self.y += dy

    def tirer(self, direction):
        dx, dy = DIR_TIR[direction]
        return (self.x + dx, self.y + dy)

# Initialisation du jeu
joueur = Personnage(LARGEUR // 2, HAUTEUR // 2, JOUEUR)
bots = [Personnage(random.randint(0, LARGEUR - 1), random.randint(0, HAUTEUR - 1), BOTS) for _ in range(NB_BOTS)]

# Fonction pour afficher la carte
def afficher():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            if (x, y) == (joueur.x, joueur.y):
                print(JOUEUR, end="")
            elif any((x, y) == (bot.x, bot.y) for bot in bots):
                print(BOTS, end="")
            else:
                print(VIDE, end="")
        print()

# Fonction pour gérer les entrées du joueur
def entree_joueur():
    print("Commandes : z = haut, s = bas, q = gauche, d = droite, t = tirer")
    commande = input("Votre action : ")
    if commande in DIR_TIR:
        return 'tirer', commande
    elif commande == 't':
        return 'tirer', input("Dans quelle direction ? (z/s/q/d) : ")
    else:
        return 'deplacer', commande

# Fonction principale du jeu
def jouer():
    while True:
        afficher()
        action, param = entree_joueur()
        if action == 'deplacer':
            dx, dy = DIR_TIR.get(param, (0, 0))
            joueur.deplacer(dx, dy)
        elif action == 'tirer':
            cible = joueur.tirer(param)
            print(f"Tir effectué en direction {param} vers {cible}")
        time.sleep(0.1)

if __name__ == "__main__":
    jouer()
