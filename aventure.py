import random
import time

# Variables globales
resources = {
    "wood": 10,
    "food": 5,
    "water": 5
}
health = 60
day = 1
shelter_upgrades = 0
game_over = False
revenge_list = []  # Liste des représailles

# Fonction d'attente avec narration
def narrate(text, delay=2):
    for line in text.split("\n"):
        print(line)
        time.sleep(delay / len(text.split("\n")))

# Tutoriel
def tutorial():
    narrate("""
    Bienvenue dans le tutoriel ! Ici, vous apprendrez les bases du jeu.
    Vous devrez gérer vos ressources (bois, nourriture, eau) pour survivre.
    Vous pouvez effectuer les actions suivantes :

    - Récupérer des ressources (1)
      Cela vous permet de collecter du bois, de la nourriture et de l'eau.
    - Améliorer votre abri (2)
      Utilisez du bois pour renforcer votre abri contre les dangers.
    - Passer une journée (3)
      Passez au jour suivant, mais assurez-vous d'avoir assez de nourriture et d'eau !
    - Explorer les environs (4)
      Une fois par jour, partez explorer pour découvrir des ressources ou des événements uniques.
    - Se réfugier (5)
      Utilisez du bois pour vous protéger d'événements imprévus, mais cela consomme des ressources.
    - Voler (6)
      Prenez le risque de voler des ressources lors d'explorations, mais attention aux conséquences.

    Si vous êtes prêts, vous pouvez sauter ce tutoriel en appuyant sur 'q'.
    """)
    while True:
        narrate("Voulez-vous suivre le tutoriel ? (o/n)")
        choice = input("> ").lower()
        if choice == "o":
            narrate("""
            Excellent choix ! Vous allez commencer par apprendre à récupérer des ressources.
            Tapez 1 pour essayer maintenant.
            """)
            input("> ")
            gather_resources()

            narrate("""
            Bien joué ! Vous avez récupéré des ressources pour survivre.
            Passons maintenant à l'amélioration de votre abri. Tapez 2 pour essayer.
            """)
            input("> ")
            upgrade_shelter()

            narrate("""
            Votre abri est maintenant plus solide. Dernier point : explorer !
            Tapez 4 pour partir à l'aventure.
            """)
            input("> ")
            explore()

            narrate("""
            Vous pouvez également apprendre à vous réfugier et à voler. Essayez 5 pour vous réfugier.
            """)
            input("> ")
            take_shelter()

            narrate("""
            Enfin, tapez 6 pour tenter de voler des ressources.
            """)
            input("> ")
            steal_resources()

            narrate("""
            Bravo ! Vous connaissez maintenant les bases. Bonne chance, survivant !
            """)
            break
        elif choice == "n":
            narrate("Vous avez choisi de passer le tutoriel. Bonne chance dans le jeu principal !")
            break
        else:
            narrate("Choix invalide. Veuillez répondre par 'o' ou 'n'.")

# Introduction avec le narrateur
def introduction():
    narrate("""
    Dans un monde ravagé par une apocalypse mystérieuse, la civilisation s'est effondrée.
    Vous vous réveillez seul(e) dans un abri en ruine, sans souvenir de ce qui s'est passé.
    La survie est votre seul objectif.
    Prenez soin de vos ressources et préparez-vous aux dangers imprévisibles de cet environnement hostile.
    """)

# Afficher le statut
def status():
    print(f"\n--- Jour {day} ---")
    print(f"Santé : {health}")
    print("Ressources :")
    for resource, amount in resources.items():
        print(f"  - {resource.capitalize()}: {amount}")
    print(f"Améliorations de l'abri : {shelter_upgrades}")
    print("-------------------")

# Récupérer des ressources
def gather_resources():
    narrate("Vous partez dans l'inconnu à la recherche de ressources...")
    wood_found = random.randint(2, 5)
    food_found = random.randint(1, 3)
    water_found = random.randint(1, 3)
    narrate(f"Après plusieurs heures de fouilles, vous trouvez :\n- {wood_found} bois\n- {food_found} nourriture\n- {water_found} eau.")
    resources["wood"] += wood_found
    resources["food"] += food_found
    resources["water"] += water_found

# Construire ou améliorer l'abri
def upgrade_shelter():
    global shelter_upgrades
    if resources["wood"] >= 10:
        narrate("Vous décidez de renforcer votre abri fragile...")
        shelter_upgrades += 1
        resources["wood"] -= 10
        narrate(f"Votre abri est maintenant plus solide (niveau {shelter_upgrades}).")
    else:
        narrate("Vous n'avez pas assez de bois pour améliorer l'abri.")

# Explorer les environs
def explore():
    narrate("Vous partez explorer les alentours...")
    time.sleep(2)
    outcomes = [
        "Vous trouvez une source d'eau potable.",
        "Vous rencontrez un marchand ambulant qui propose des échanges.",
        "Vous tombez dans une embuscade et perdez quelques ressources.",
        "Vous trouvez des traces d'autres survivants, mais aucun signe direct."
    ]
    result = random.choice(outcomes)
    narrate(f"Exploration : {result}")

    if result == "Vous trouvez une source d'eau potable.":
        water_found = random.randint(3, 6)
        resources["water"] += water_found
        narrate(f"Vous collectez {water_found} eau.")
    elif result == "Vous rencontrez un marchand ambulant qui propose des échanges.":
        narrate("Le marchand vous propose un échange. Que voulez-vous faire ?")
        print("1. Échanger 2 nourritures contre 5 bois")
        print("2. Échanger 2 bois contre 3 nourritures")
        print("3. Ne rien échanger")
        choice = input("> ")
        if choice == "1" and resources["food"] >= 2:
            resources["food"] -= 2
            resources["wood"] += 5
            narrate("Vous échangez 2 nourritures contre 5 bois.")
        elif choice == "2" and resources["wood"] >= 2:
            resources["wood"] -= 2
            resources["food"] += 3
            narrate("Vous échangez 2 bois contre 3 nourritures.")
        else:
            narrate("Échange impossible ou annulé.")
    elif result == "Vous tombez dans une embuscade et perdez quelques ressources.":
        wood_lost = random.randint(1, 3)
        resources["wood"] = max(0, resources["wood"] - wood_lost)
        narrate(f"Vous perdez {wood_lost} bois dans l'attaque.")

# Se réfugier
def take_shelter():
    if resources["wood"] >= 5:
        narrate("Vous utilisez vos ressources pour vous mettre à l'abri...")
        resources["wood"] -= 5
        narrate("Vous êtes en sécurité pour la journée.")
    else:
        narrate("Vous n'avez pas assez de bois pour vous réfugier.")

# Voler des ressources
def steal_resources():
    narrate("Vous prenez le risque de voler des ressources...")
    success = random.random() < 0.5
    if success:
        wood_stolen = random.randint(3, 7)
        resources["wood"] += wood_stolen
        narrate(f"Vous réussissez à voler {wood_stolen} bois.")
    else:
        health_loss = random.randint(5, 15)
        global health
        health -= health_loss
        narrate(f"Vous vous faites repérer et subissez {health_loss} points de dégâts.")
        revenge_list.append("groupe de survivants")  # Ajout du groupe à la liste des représailles

# Passer une journée
def pass_day():
    global health, game_over, day
    narrate("Le soleil se couche, et une nuit froide et silencieuse s'installe...")
    food_consumed = 2
    water_consumed = 2

    if resources["food"] >= food_consumed and resources["water"] >= water_consumed:
        resources["food"] -= food_consumed
        resources["water"] -= water_consumed
        narrate("Malgré les conditions difficiles, vous mangez et buvez pour garder vos forces.")
    else:
        health_loss = 5
        health -= health_loss
        narrate(f"Vous manquez de nourriture ou d'eau. La faim et la soif vous affaiblissent (-{health_loss} santé).")

    if revenge_list:
        narrate("Pendant la nuit, ceux que vous avez volés reviennent se venger...")
        for group in revenge_list:
            stolen_wood = random.randint(2, 5)
            stolen_food = random.randint(1, 3)
            stolen_water = random.randint(1, 3)
            resources["wood"] = max(0, resources["wood"] - stolen_wood)
            resources["food"] = max(0, resources["food"] - stolen_food)
            resources["water"] = max(0, resources["water"] - stolen_water)
            narrate(f"Le {group} vous vole :\n- {stolen_wood} bois\n- {stolen_food} nourriture\n- {stolen_water} eau.")
        revenge_list.clear()

    if health <= 0:
        narrate("Vous avez succombé aux rigueurs de ce monde cruel...\nFin du jeu.")
        game_over = True
    else:
        day += 1

# Événement aléatoire
def random_event():
    events = [
        "Un groupe de pillards attaque votre abri.",
        "Vous trouvez une cachette abandonnée avec des ressources.",
        "Un étranger vous propose de l'aide en échange de nourriture.",
        "Une tempête détruit une partie de votre abri."
    ]
    event = random.choice(events)
    narrate(f"\nÉvénement : {event}")

    global health
    if event == "Un groupe de pillards attaque votre abri.":
        health_loss = random.randint(5, 15)
        resources_lost = random.randint(1, 3)
        health -= health_loss
        resources["wood"] = max(0, resources["wood"] - resources_lost)
        narrate(f"Dans la lutte, vous perdez {health_loss} points de santé et {resources_lost} bois.")
    elif event == "Vous trouvez une cachette abandonnée avec des ressources.":
        wood_found = random.randint(5, 10)
        food_found = random.randint(3, 5)
        resources["wood"] += wood_found
        resources["food"] += food_found
        narrate(f"Cette cachette contient :\n- {wood_found} bois\n- {food_found} nourriture.")
    elif event == "Un étranger vous propose de l'aide en échange de nourriture.":
        if resources["food"] >= 3:
            resources["food"] -= 3
            health_gain = random.randint(5, 15)
            health += health_gain
            narrate(f"Vous acceptez l'offre et gagnez {health_gain} points de santé.")
        else:
            narrate("Vous n'avez pas assez de nourriture pour accepter l'offre.")
    elif event == "Une tempête détruit une partie de votre abri.":
        resources["wood"] = max(0, resources["wood"] - 5)
        narrate("La tempête emporte 5 bois de votre abri.")

# Boucle principale du jeu
def main():
    tutorial()
    introduction()
    while not game_over:
        status()
        narrate("\nQue voulez-vous faire ?")
        print("1. Récupérer des ressources")
        print("2. Améliorer l'abri")
        print("3. Passer une journée")
        print("4. Explorer les environs")
        print("5. Se réfugier")
        print("6. Voler des ressources")
        choice = input("> ")

        if choice == "1":
            gather_resources()
        elif choice == "2":
            upgrade_shelter()
        elif choice == "3":
            pass_day()
        elif choice == "4":
            explore()
        elif choice == "5":
            take_shelter()
        elif choice == "6":
            steal_resources()
        else:
            narrate("Choix invalide.")

        if random.random() < 0.4:  # 40%
            random_event()

    narrate("\nMerci d'avoir joué. Prenez soin de vous, survivant.")

# Lancer le jeu
if __name__ == "__main__":
    main()
