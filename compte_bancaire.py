class CompteBancaire:
    def __init__(self, titulaire: str, solde: float=0):
        self.titulaire = titulaire 
        self._journal = [] #Protected
        self.__solde = solde #Private
    
    def deposer(self, montant: float) -> None:
        if montant <=0:
            raise ValueError("Le montant doit être positif")
        self.__solde += montant
        self._journal.append(("depot", montant))
    
    def retirer(self, montant: float) -> None:
        if montant > self.__solde:
            raise ValueError("Solde insuffisant")
        self.__solde -= montant
        self._journal.append(("retrait", montant))
    
    def consulter_solde(self) -> float:
        return self.__solde
    
# c = CompteBancaire("La Morsure", 100000)
# c.deposer(50000)
# print(f"Votre solde est de : {c.consulter_solde()} FCFA")
# c.retirer(75000)
# print(f"Vous solde est de : {c.consulter_solde()} FCFA")

depot = float(input("Entrez le montant du depot svp -> "))
c = CompteBancaire(depot) 
c.deposer(depot)

requete = str(input("Voulez-vous faire un retrait ? (Oui/Non)"))
if requete == 'Oui':
    retrait = float(input("Entrez le montant du retrait svp -> "))
    c.retirer(retrait)
    print(f"Votre nouveau solde est de : {c.consulter_solde()} FCFA")
elif requete ==  'Non':
    print(f"OK voici le recapitulatif de votre compte : {c.consulter_solde()} FCFA ")