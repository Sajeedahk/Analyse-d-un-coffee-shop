import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Charge le fichier 
def charger_donnees(fichier_path):
    doc = pd.read_csv(fichier_path, sep=",")
    doc.dropna(inplace=True)
    return doc

#affiche les catégories dans les colonnes
def analyser_categories(doc, colonne):
    nb_categories = doc[colonne].nunique()
    liste_categories = doc[colonne].unique()

    print(f"\n La colonne '{colonne}' contient {nb_categories} catégories différentes :\n")
    for i in liste_categories:
        print(f"- {i}")

#chiffre d'affaire
def chiffre_affaire(doc):
    total = 0
    Bills = doc["Total_Bill"]
    for i in Bills:
        total += i
    print("Chiffre d'affaire = " + str(total))

#chiffre d'affaire par boutique 
def chiffre_affaire_boutique(doc):
    total_par_boutique = doc.groupby("store_location")["Total_Bill"].sum()
    print("Chiffre d'affaire par endroit = \n " + str(total_par_boutique))

    boutiques = total_par_boutique.index.tolist()
    montants = total_par_boutique.values.tolist()

    plt.figure(figsize=(10, 6))
    plt.bar(boutiques, montants, color="chocolate")
    plt.title("Chiffre d'affaires par boutique")
    plt.xlabel("Boutique")
    plt.ylabel("Montant $ ")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def chiffre_affaire_produit(doc):
    total_par_produit = doc.groupby("product_detail")["Total_Bill"].sum()
    print("Chiffre d'affaire par produit = \n" + str(total_par_produit))

    produit = total_par_produit.index.tolist()
    montant = total_par_produit.values.tolist()

    plt.figure(figsize=(10, 6))
    plt.bar(produit, montant, color="blue")
    plt.title("Chiffre d'affaires par produit")
    plt.xlabel("produit")
    plt.ylabel("Montant $ ")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()




#Nombre de transaction
def nbr_transaction(doc):
    total = 0 
    transac = doc["transaction_qty"]
    for  i in transac:
        total += 1
    print("Nombre de transaction = "+str(total))

#boisson les plus consommée
def boisson_la_plus_conso(doc):

    compteur ={}
    for boisson in doc["product_detail"] :
        if boisson in compteur :
            compteur[boisson] += 1
        else :
            compteur[boisson] = 1
    #affiche juste le top 10
    top = dict(sorted(compteur.items(), key=lambda x: x[1], reverse=True)[:10])

 # Tracer le graphique
    labels = list(top.keys())
    sizes = list(top.values())

    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des boissons consommées")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def boisson_moins_conso(doc):
    compteur ={}
    for boisson in doc["product_detail"] :
        if boisson in compteur :
            compteur[boisson] += 1
        else :
            compteur[boisson] = 1
    #affiche les 5 produits les moins vendu
    bottom = dict(sorted(compteur.items(), key=lambda x: x[1])[:5])
    labels = list(bottom.keys())
    sizes = list(bottom.values())
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des boissons les moins consommées")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


   



#affiche les graphique
if __name__ == "__main__": # teste de code
    fichier = charger_donnees(r"C:\Users\sajee_4y670z6\OneDrive\Documents\Informatiques\Python\Analyse transaction coffee shop\transaction.csv")
    #boisson les plus conso 
    boisson_la_plus_conso(fichier)
    #boisson les moins conso
    boisson_moins_conso(fichier)

    #affiche le nombre de catégorie dans une colonne
    analyser_categories(fichier, "product_category")
    analyser_categories(fichier, "store_location")
    analyser_categories(fichier, "product_detail")

    #chiffre d'affaire
    chiffre_affaire(fichier)
    #Nombre de transaction
    nbr_transaction(fichier)
    #Chiffre d'affaire par boutique
    chiffre_affaire_boutique(fichier)
    #Chiffre d'affaire par produit
    chiffre_affaire_produit(fichier)

    
    




import os
print("Répertoire actuel :", os.getcwd())
