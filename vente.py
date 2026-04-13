# 🔹 Importation des bibliothèques
import csv                     # Pour lire/écrire des fichiers CSV
import matplotlib.pyplot as plt  # Pour créer le graphique

# 🔹 Listes pour stocker les données du graphique
ids = []        # contiendra les ID des produits
ca_nets = []    # contiendra les CA Net

# 🔹 Ouverture du fichier CSV en mode lecture
with open("ventes.csv", "r") as fichier:

    # Création du lecteur CSV (séparateur ;)
    lecteur = csv.reader(fichier, delimiter=";")

    # 🔹 Lecture de la première ligne (entête)
    entete = next(lecteur)

    # 🔹 Affichage de l'entête + nouvelles colonnes
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        *entete, "CA_Brut", "CA_Net", "TVA"
    ))

    # 🔹 Initialisation des variables
    total = 0       # somme des CA Net
    max_ca = 0      # plus grand CA Net trouvé
    id_max = ""     # ID du produit le plus rentable

    # 🔹 Liste pour stocker les résultats (pour export CSV)
    resultats = []

    # 🔹 Parcours dynamique de toutes les lignes du fichier
    for ligne in lecteur:

        # 🔹 Récupération des données
        prix = float(ligne[1])
        quantite = int(ligne[2])
        remise = float(ligne[3])

        # 🔹 Calculs
        CA_Brut = prix * quantite
        CA_Net = CA_Brut * (1 - remise / 100)
        TVA = CA_Net * 0.20

        # 🔹 Ajout au total
        total += CA_Net

        # 🔹 Affichage ligne par ligne (format tableau)
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            *ligne, CA_Brut, CA_Net, TVA
        ))

        # 🔹 Stockage pour le graphique
        ids.append(ligne[0])
        ca_nets.append(CA_Net)

        # 🔹 Stockage pour le fichier final
        resultats.append(ligne + [CA_Brut, CA_Net, TVA])

        # 🔹 Recherche du produit le plus rentable
        if CA_Net > max_ca:
            max_ca = CA_Net
            id_max = ligne[0]

    # 🔹 Affichage des résultats globaux
    print("\nCA Total de l'entreprise =", total)
    print("Produit avec le plus grand bénéfice :", id_max)

# 🔹 Création du graphique (CA Net par produit)
plt.figure(figsize=(10,6))  # 🔹 taille du graphique

plt.bar(ids, ca_nets)

plt.title("CA Net par produit", fontsize=14)
plt.xlabel("ID Produit")
plt.ylabel("CA Net")



plt.grid(axis='y')  # 🔹 grille horizontale

# 🔹 afficher les valeurs au-dessus des barres
for i in range(len(ids)):
    plt.text(i, ca_nets[i], round(ca_nets[i], 1), ha='center', va='bottom')

plt.bar(ids, ca_nets, color="#7EB5EC")
plt.title("Analyse du chiffre d'affaires net par produit",)
plt.show()


# 🔹 Création du fichier CSV final
with open("resultats_final.csv", "w", newline="") as fichier_sortie:

    ecrivain = csv.writer(fichier_sortie, delimiter=";")

    # 🔹 Écriture de l'entête
    ecrivain.writerow(entete + ["CA_Brut", "CA_Net", "TVA"])

    # 🔹 Écriture des lignes
    for ligne in resultats:
        ecrivain.writerow(ligne)
