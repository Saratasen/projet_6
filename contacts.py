#---------------------------------------------------
import sqlite3

#creation de la table
class CONTACTS:
    def __init__(self,id, nom, prenom, email, adresse, numero):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.adresse =  adresse
        self.numero = numero
        
    def __str__(self):
        return f"{self.id} {self.nom} {self.prenom} {self.email} {self.adresse} {self.numero}"
    
    #------------------------------------------------------
class GestionContact:
    def __init__(self):
        self.connexion = sqlite3.connect("contacts.db")
        self.curseur = self.connexion.cursor()
        self.curseur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, email TEXT UNIQUE, adresse TEXT, numero TEXT UNIQUE)")
        self.connexion.commit()    
        
    def ajouter_contacts(self, contacts):
        self.curseur.execute("INSERT INTO contacts VALUES (?,?,?,?,?)", (contacts.id, contacts.nom_))
        self.connexion.commit() 
        
    def supprimer_contacts(self, id):
        self.curseur.execute("DELETE FROM contact WHERE id=?, " (id,))
        self.connexion.commit()
    
    def modifier_contacts(self, id):
        self.curseur.execute("UPDATE contacts SET nom=? prenom=? email=? adresse=? numero=? WHERE id=?", )
        self.connexion.commit()
        
    def afficher_contacts(self):
        self.curseur.execute("SELECT * FROM contacts")
        contacts = self.curseur.fetchall()
        for contacts in contacts:
            print(contacts(*contacts))
            
#----------------------------------------------------
Gestion_Contact = GestionContact()

# Ajoute un contacts
contact1 =  contact=(1, "Sene", "sarata", "Snesarata@gmail.com", "123456789", "221 Main St")
Gestion_Contact.ajouter_contacts()

# Afficher un contacts 
Gestion_Contact.afficher_contacts()

# Modifier un contacts 
contact2 = contact(2, "Sene", "sarata", "Senesarata@gmail.com")
