class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk {self.vek}, telefon: {self.telefon}"

class Evidence:
    def __init__(self):
        self.pojisteni = []
        
    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        
    def seznam_pojistenych(self):
        for pojisteny in self.pojisteni:
            print(pojisteny)
            
    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None

def menu():
    evidence = Evidence()
    
    while True:
        print("1. Přidat pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Najít pojištěného")
        print("4. Konec")
        volba = input("Vyberte akci: ")
        
        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefonní číslo: ")
            evidence.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
            
        elif volba == "2":
            evidence.seznam_pojistenych()
            
        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny is not None:
                print(pojisteny)
            else:
                print("Pojištěný nenalezen.")
                
        elif volba == "4":
            break
            
        else:
            print("Neplatná volba.")

menu()