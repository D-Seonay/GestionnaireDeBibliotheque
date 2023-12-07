import json
class Livre:
    def __init__(self, titre, auteur, categorie):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.emprunte_par = None

    def disponible(self):
        return self.emprunte_par is None

    def emprunter(self, utilisateur):
        if self.disponible():
            self.emprunte_par = utilisateur
            return True
        else:
            return False

    def retourner(self):
        self.emprunte_par = None

class LivreRomance(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Romance")

class LivreFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Fiction")
    
class LivreNonFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Non-Fiction")

class LivreHorreur(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Horreur")

class LivreBiographie(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Biographie")

class LivreAutobiographie(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Autobiographie")

class LivreScienceFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Science fiction")
        





class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
class UtilisateurMineur(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.autorisation_parentale = False

class UtilisateurMajeur(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.autorisation_parentale = True



class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def retirer_livre(self, livre):
        if livre in self.livres:
            self.livres.remove(livre)

    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
        
    def supprimer_utilisateur(self, utilisateur):
        if utilisateur in self.utilisateurs:
            self.utilisateurs.remove(utilisateur)
    
    def livres_par_categorie(self, categorie):
        livres_par_cat = [livre for livre in self.livres if livre.categorie == categorie]
        if livres_par_cat:
            print(f"Liste des livres dans la catégorie '{categorie}':")
            for livre in livres_par_cat:
                print(f"- {livre.titre} par {livre.auteur}")
        else:
            print(f"Aucun livre trouvé dans la catégorie '{categorie}'.")
            
    def emprunter_livre(self, livre, utilisateur):
        if livre.emprunter(utilisateur):
            print(f"L'utilisateur {utilisateur.prenom} {utilisateur.nom} a emprunté le livre {livre.titre} par {livre.auteur}.")
            
        else:
            print(f"Le livre {livre.titre} par {livre.auteur} n'est pas disponible.")
            
    def retourner_livre(self, livre):
        livre.retourner()
    
    def afficher_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.disponible()]
        if livres_disponibles:
            print("Liste des livres disponibles :")
            for i, livre in enumerate(livres_disponibles):
                print(f"{i+1}. {livre.titre} par {livre.auteur}")
        else:
            print("Aucun livre disponible.")
            
    def afficher_livres_empruntes(self):
        livres_empruntes = [livre for livre in self.livres if not livre.disponible()]
        if livres_empruntes:
            print("Liste des livres empruntés :")
            for i, livre in enumerate(livres_empruntes):
                print(f"{i+1}. {livre.titre} par {livre.auteur}")
        else:
            print("Aucun livre emprunté.")
            
    def afficher_utilisateurs(self):
        print("Liste des utilisateurs :")
        for i, utilisateur in enumerate(self.utilisateurs):
            print(f"{i+1}. {utilisateur.prenom} {utilisateur.nom}")

            
    def choix_utilisateur(self):
        self.afficher_utilisateurs()
        choix = input("Entrez le numéro de l'utilisateur : ")
        try:
            choix = int(choix)
            return self.utilisateurs[choix - 1]
        except (ValueError, IndexError):
            print("Veuillez choisir un utilisateur existant.")
            return self.choix_utilisateur()
        
    def rechercher_livre(self):
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        livre_existe = False
        for livre in self.livres:
            if livre.titre == titre or livre.auteur == auteur:
                livre_existe = True
                break
        if livre_existe:
            print("Le livre existe.")
            print(f"Titre : {livre.titre}")
            print(f"Auteur : {livre.auteur}")
            print(f"Categorie : {livre.categorie}")
            if livre.disponible():
                print("Le livre est disponible.")
                print("Vous pouvez l'emprunter.")
                if input("Voulez-vous l'emprunter ? (O/N) : ").upper() == "O":
                    self.emprunter_livre(livre, biblio.choix_utilisateur())
                else:
                    print("Vous n'avez pas emprunté le livre.")
            else:
                print("Le livre n'est pas disponible.")
                print(f"Emprunté par : {livre.emprunte_par.prenom} {livre.emprunte_par.nom}")
                
            
        else:
            print("Le livre n'existe pas.")
            
    def sauvegarder_etat_bibliotheque(self, data_file):
                etat = {
                    "livres": [],
                    "utilisateurs": []
                }
                    
                for livre in self.livres:
                    etat_livre = {
                        "titre": livre.titre,
                        "auteur": livre.auteur,
                        "categorie": livre.categorie,
                        "disponible": livre.disponible(),
                        "emprunte_par": None
                    }
                        
                    if not livre.disponible():
                            etat_livre["emprunte_par"] = {
                                "nom": livre.emprunte_par.nom,
                                "prenom": livre.emprunte_par.prenom
                            }
                        
                    etat["livres"].append(etat_livre)
                    
                for utilisateur in self.utilisateurs:
                        etat_utilisateur = {
                            "nom": utilisateur.nom,
                            "prenom": utilisateur.prenom
                        }
                        
                        etat["utilisateurs"].append(etat_utilisateur)
                    
                with open(data_file, "w") as fichier:
                        json.dump(etat, fichier)
            
    def charger_etat(self, data_file):
            with open(data_file, "r") as fichier:
                etat = json.load(fichier)

                for livre_data in etat["livres"]:
                    livre = Livre(
                        livre_data["titre"],
                        livre_data["auteur"],
                        livre_data["categorie"]
                    )
                    livre.emprunte_par = livre_data["emprunte_par"]  # Mettre à jour l'emprunteur si le livre n'est pas disponible
                    self.ajouter_livre(livre)

                for utilisateur_data in etat["utilisateurs"]:
                    utilisateur = Utilisateur(
                        utilisateur_data["nom"],
                        utilisateur_data["prenom"]
                    )
                    self.enregistrer_utilisateur(utilisateur)
  
def choisir_categorie():
    print("Choisissez une catégorie :")
    print("1. Fiction")
    print("2. Non-Fiction")
    print("3. Autobiographie")
    print("4. Biographie")
    print("5. Horreur")
    print("6. Romance")
    print("7. Science fiction")
    choix = input("Votre choix : ")
    
    if choix == "1":
        return "Fiction"
    elif choix == "2":
        return "Non-Fiction"
    elif choix == "3":
        return "Autobiographie"
    elif choix == "4":
        return "Biographie"
    elif choix == "5":
        return "Horreur"
    elif choix == "6":
        return "Romance"
    elif choix == "7":
        return "Science fiction"
    else:
        print("Choix invalide !")
        return choisir_categorie()

# Utilisation d'un dictionnaire pour simuler le "switch"
actions = {
    'ajouter_livre': Bibliotheque.ajouter_livre,
    'retirer_livre': Bibliotheque.retirer_livre,
    'enregistrer_utilisateur': Bibliotheque.enregistrer_utilisateur,
    # Ajoutez d'autres actions ici
}

biblio = Bibliotheque()
biblio.charger_etat("etat_bibliotheque.json")



while True:
    print("Que voulez-vous faire ?")
    print("1. Rechercher un livre")
    print("2. Ajouter un livre")
    print("3. Retirer un livre")
    print("4. Afficher les livres par catégorie")
    print("5. Afficher les utilisateurs")
    print("6. Enregistrer un utilisateur")
    print("7. Supprimer un utilisateur")
    print("8. Afficher les livres disponibles")
    print("9. Afficher les livres empruntés")
    print("10. Emprunter un livre")
    print("11. Retourner un livre")
    print("12. Sauvegarder l'état de la bibliothèque")
    print("13. Quitter")
    choix = input("Votre choix : ")
    
    if choix == "1":
        biblio.rechercher_livre()
    
    elif choix == "2":
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        categorie = choisir_categorie()
        if categorie == "Fiction":
            livre = LivreFiction(titre, auteur)
        elif categorie == "Non-Fiction":
            livre = LivreNonFiction(titre, auteur)
        elif categorie == "Autobiographie":
            livre = LivreAutobiographie(titre, auteur)
        elif categorie == "Biographie":
            livre = LivreBiographie(titre, auteur)
        elif categorie == "Horreur":
            livre = LivreHorreur(titre, auteur)
        elif categorie == "Romance":
            livre = LivreRomance(titre, auteur)
        elif categorie == "Science fiction":
            livre = LivreScienceFiction(titre, auteur)
        else:
            print("Catégorie invalide !")
            continue
        
        biblio.ajouter_livre(livre)  # Ajout du livre créé à la bibliothèque
        print("Livre ajouté !")
        print(f"Nombre de livres de la catégorie {categorie} : {len([livre for livre in biblio.livres if livre.categorie == categorie])}")

    elif choix == "3":
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        categorie = choisir_categorie() 
        if categorie == "Fiction":
            livre = LivreFiction(titre, auteur)
        elif categorie == "Non-Fiction":
            livre = LivreNonFiction(titre, auteur)
        elif categorie == "Autobiographie":
            livre = LivreAutobiographie(titre, auteur)
        elif categorie == "Biographie":
            livre = LivreBiographie(titre, auteur)
        elif categorie == "Horreur":
            livre = LivreHorreur(titre, auteur)
        elif categorie == "Romance":
            livre = LivreRomance(titre, auteur)
        elif categorie == "Science fiction":
            livre = LivreScienceFiction(titre, auteur)
        else:
            print("Catégorie invalide !")
            continue
        biblio.retirer_livre(livre)
        print("Livre retiré !")
    elif choix == "4":
        categorie = choisir_categorie()
        biblio.livres_par_categorie(categorie)
        
    elif choix == "5":
        biblio.afficher_utilisateurs()
        
    elif choix == "6":
        nom = input("Nom de l'utilisateur : ")
        prenom = input("Prénom de l'utilisateur : ")
        utilisateur = Utilisateur(nom, prenom)
        biblio.enregistrer_utilisateur(utilisateur)
        print("Utilisateur enregistré !")
    
    elif choix == "7":
        biblio.afficher_utilisateurs()
        choix_utilisateur = input("Entrez le numéro de l'utilisateur : ")
        try:
            choix_utilisateur = int(choix_utilisateur)
            suprim_utilisateur = [utilisateur for utilisateur in biblio.utilisateurs][choix_utilisateur - 1]
            biblio.supprimer_utilisateur(suprim_utilisateur)
            print(f"Vous avez supprimé l'utilisateur {suprim_utilisateur.prenom} {suprim_utilisateur.nom}.")
        except (ValueError, IndexError):
            print("Choix invalide.")
        
    
    elif choix == "8":
        biblio.afficher_livres_disponibles()
    
    elif choix == "9":
        biblio.afficher_livres_empruntes()
        
    elif choix == "10":
        biblio.afficher_livres_disponibles()
        choix_livre = input("Entrez le numéro du livre que vous souhaitez emprunter : ")
        try:
            choix_livre = int(choix_livre)
            livre_choisi = [livre for livre in biblio.livres if livre.disponible()][choix_livre - 1]
            # Demandez les détails de l'utilisateur pour l'emprunt
            biblio.afficher_utilisateurs()
            utilisateur = biblio.choix_utilisateur()
            if livre_choisi.emprunter(utilisateur):
                print(f"Vous avez emprunté '{livre_choisi.titre}' par {livre_choisi.auteur}.")
            else:
                print("Ce livre n'est pas disponible pour l'emprunt.")
        except (ValueError, IndexError):
            print("Choix invalide.")
            
            
    elif choix == "11":
        biblio.afficher_livres_empruntes()
        choix_livre = input("Entrez le numéro du livre que vous souhaitez retourner : ")
        try:
            choix_livre = int(choix_livre)
            livre_choisi = [livre for livre in biblio.livres if not livre.disponible()][choix_livre - 1]
            livre_choisi.retourner()
            print(f"Vous avez retourné '{livre_choisi.titre}' par {livre_choisi.auteur}.")
        except (ValueError, IndexError):
            print("Choix invalide.")
    elif choix == "12":
        biblio.sauvegarder_etat_bibliotheque("etat_bibliotheque.json")
    
    elif choix == "13":
        biblio.sauvegarder_etat_bibliotheque("etat_bibliotheque.json")
        break
        
    else:
        print("Choix invalide !")