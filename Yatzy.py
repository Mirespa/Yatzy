import random

# Nopan luvut ja niiden tallenus
min = 1
max = 6
heitot = []
noppien_pito = {"1":False, "2":False, "3":False, "4":False, "5":False}
taulukko = {"ykköset":"", "kakkoset":"", "kolmoset":"", "neloset":"", "vitoset":"", "kutoset":"", "bonus":"", "yksi pari":"", "kaksi paria":"", "kolmoisluku":"", "neloisluku":"", "pieni suora":"", "iso suora":"", "mökki":"", "sattuma":"", "yatzy":""}
heitto_määrä = 3

# Nopanheitto
def nopanheitto():
    for i in range(1,6):
        nopan_heitto = random.randint(min,max)
        heitot.append(nopan_heitto)
    return heitot

# Ykköset
def ykköset():
    määrä = heitot.count(1)
    pisteet = määrä * 1
    taulukko["ykköset"] = int(pisteet)
    return pisteet

# Kakkoset
def kakkoset():
    määrä = heitot.count(2)
    pisteet = määrä * 2
    taulukko["kakkoset"] = int(pisteet)
    return pisteet

# Kolmoset
def kolmoset():
    määrä = heitot.count(3)
    pisteet = määrä * 3
    taulukko["kolmoset"] = int(pisteet)
    return pisteet

# Neloset
def neloset():
    määrä = heitot.count(4)
    pisteet = määrä * 4
    taulukko["neloset"] = int(pisteet)
    return pisteet

# Vitoset
def vitoset():
    määrä = heitot.count(5)
    pisteet = määrä * 5
    taulukko["vitoset"] = int(pisteet)
    return pisteet

# Kutoset
def kutoset():
    määrä = heitot.count(6)
    pisteet = määrä * 6
    taulukko["kutoset"] = int(pisteet)
    return pisteet

# Välisumma
# Jos pisteet yli 63 niin 50 pisteen bonus
def bonus():
    summa = taulukko["ykköset"] + taulukko["kakkoset"] + taulukko["kolmoset"] + taulukko["neloset"] + taulukko["vitoset"] + taulukko["kutoset"]
    if summa >= 63:
        taulukko["bonus"] = int(50)
    else:
        taulukko["bonus"] = int(0)

# Yksi pari
def yksi_pari():
    pisteet = 0
    parittomat = []
    parilliset = []
    for i in heitot:
        if i not in parittomat:
            parittomat.append(i)
        else:
            parilliset.append(i)
    if parilliset != []:
        parilliset.sort()
        luku = parilliset[-1]
        pisteet = luku * 2
    taulukko["yksi pari"] = int(pisteet)
    return pisteet

# Kaksi paria
def kaksi_paria():
    pisteet = 0
    parittomat = []
    parilliset = []
    for i in heitot:
        if i not in parittomat:
            parittomat.append(i)
        else:
            parilliset.append(i)
    if len(parilliset) > 1:
        parilliset.sort()
        luku1 = parilliset[-1]
        luku2 = parilliset[-2]
        pisteet = luku1 * 2 + luku2 * 2
    taulukko["kaksi paria"] = int(pisteet)
    return pisteet

# Kolmoisluku
def kolmoisluku():
    pisteet = 0
    yksi_luku = []
    kaksi_lukua = []
    kolme_lukua = []
    for i in heitot:
        if i not in yksi_luku:
            yksi_luku.append(i)
        elif i in yksi_luku and i not in kaksi_lukua:
            kaksi_lukua.append(i)
        else:
            kolme_lukua.append(i)
    if kolme_lukua != []:
        pisteet = kolme_lukua[0] * 3
    taulukko["kolmoisluku"] = int(pisteet)
    return pisteet

# Neloisluku
def neloisluku():
    pisteet = 0
    yksi_luku = []
    kaksi_lukua = []
    kolme_lukua = []
    neljä_lukua = []
    for i in heitot:
        if i not in yksi_luku:
            yksi_luku.append(i)
        elif i in yksi_luku and i not in kaksi_lukua:
            kaksi_lukua.append(i)
        elif i in yksi_luku and i in kaksi_lukua and i not in kolme_lukua:
            kolme_lukua.append(i)
        else:
            neljä_lukua.append(i)
    if neljä_lukua != []:
        pisteet = neljä_lukua[0] * 4
    taulukko["neloisluku"] = int(pisteet)
    return pisteet

# Pieni suora
def pieni_suora():
    pisteet = 0
    if 1 in heitot and 2 in heitot and 3 in heitot and 4 in heitot and 5 in heitot:
        pisteet = 15
    taulukko["pieni suora"] = int(pisteet)
    return pisteet

# Iso suora
def iso_suora():
    pisteet = 0
    if 2 in heitot and 3 in heitot and 4 in heitot and 5 in heitot and 6 in heitot:
        pisteet = 20
    taulukko["iso suora"] = int(pisteet)
    return pisteet

# Täyskäsi eli mökki
def mökki():
    pisteet = 0
    yksi_luku = []
    kaksi_lukua = []
    kolme_lukua = []
    for i in heitot:
        if i not in yksi_luku:
            yksi_luku.append(i)
        elif i in yksi_luku and i not in kaksi_lukua:
            kaksi_lukua.append(i)
        else:
            kolme_lukua.append(i)
    if len(kaksi_lukua) == 2 and len(kolme_lukua) == 1:
        if kolme_lukua[0] == kaksi_lukua[0]:
            pisteet = kolme_lukua[0] * 3 + kaksi_lukua[1] * 2
        else:
            pisteet = kolme_lukua[0] * 3 + kaksi_lukua[0] * 2
    taulukko["mökki"] = int(pisteet)
    return pisteet

# Sattuma
def sattuma():
    pisteet = 0
    for i in heitot:
        pisteet += i
    taulukko["sattuma"] = int(pisteet)
    return pisteet

# Yatzy
def yatzy():
    pisteet = 0    
    yksi_luku = []
    kaksi_lukua = []
    kolme_lukua = []
    neljä_lukua = []
    viisi_lukua = []
    for i in heitot:
        if i not in yksi_luku:
            yksi_luku.append(i)
        elif i in yksi_luku and i not in kaksi_lukua:
            kaksi_lukua.append(i)
        elif i in yksi_luku and i in kaksi_lukua and i not in kolme_lukua:
            kolme_lukua.append(i)
        elif i in yksi_luku and i in kaksi_lukua and i in kolme_lukua and i not in neljä_lukua:
            neljä_lukua.append(i)
        else:
            viisi_lukua(i)
    if viisi_lukua != []:
        pisteet = 50
    taulukko["yatzy"] = int(pisteet)
    return pisteet

# Itse peli
while taulukko["ykköset"] == "" or taulukko["kakkoset"] == "" or taulukko["kolmoset"] == "" or taulukko["neloset"] == "" or taulukko["vitoset"] == "" or taulukko["kutoset"] == "" or taulukko["yksi pari"] == "" or taulukko["kaksi paria"] == "" or taulukko["kolmoisluku"] == "" or taulukko["neloisluku"] == "" or taulukko["pieni suora"] == "" or taulukko["iso suora"] == "" or taulukko["mökki"] == "" or taulukko["sattuma"] == "" or taulukko["yatzy"] == "":
    if heitot != []:
        # Mahdolliset vaihtoehdot
        print("")
        print(f"Noppasi ovat {heitot}.")
        print(f"Heittoja jäljellä {heitto_määrä}")
        print("Valinnat")
        print("0 = heitä kaikki uudelleen")
        print("00 = heitä valitut uudelleen")
        if taulukko["ykköset"] == "":
            print("1 = ykköset")
        if taulukko["kakkoset"] == "":
            print("2 = kakkoset")
        if taulukko["kolmoset"] == "":
            print("3 = kolmoset")
        if taulukko["neloset"] == "":
            print("4 = neloset")
        if taulukko["vitoset"] == "":
            print("5 = vitoset")
        if taulukko["kutoset"] == "":
            print("6 = kutoset")
        if taulukko["yksi pari"] == "":
            print("7 = yksi pari")
        if taulukko["kaksi paria"] == "":
            print("8 = kaksi paria")
        if taulukko["kolmoisluku"] == "":
            print("9 = kolmoisluku")
        if taulukko["neloisluku"] == "":
            print("10 = neloisluku")
        if taulukko["pieni suora"] == "":
            print("11 = pieni suora")
        if taulukko["iso suora"] == "":
            print("12 = iso suora")
        if taulukko["mökki"] == "":
            print("13 = mökki")
        if taulukko["sattuma"] == "":
            print("14 = sattuma")
        if taulukko["yatzy"] == "":
            print("15 = yatzy")
        valinta = input("Mitä aiot tehdä? ")


    else:
        print("")
        valinta = input("Heitä noppia painamalla 0 ")

    # Vaihtoehtojen seurakset
    if valinta == "0" and heitto_määrä != 0:
        heitot = []
        heitot = nopanheitto()
        heitto_määrä -= 1

    if heitot != []:
        if valinta == "0" and heitto_määrä == 0:
            print("Et voi enää heittää.")

        while valinta == "00" and heitto_määrä != 0:
            print("")
            print("0 = palaa takaisin.")
            vaihdettavat = input("Mitkä nopista haluat heittää uudelleen? (esim. 1,4): ")
            if vaihdettavat == "0":
                break
            vaihdettavat = vaihdettavat.replace(" ","").split(",")
            for i in vaihdettavat:
                noppien_pito[i] = not noppien_pito[i]
            for i in noppien_pito:
                if noppien_pito[str(i)] == True:
                    heitot[int(i)-1] = random.randint(1,6)
            heitto_määrä -= 1
            noppien_pito = {"1":False, "2":False, "3":False, "4":False, "5":False}
            break
        
        if valinta == "00" and heitto_määrä == 0:
            print("Et voi enää heittää.")

        if valinta == "1":
            if taulukko["ykköset"] == "":
                if ykköset() == 1:
                    print(f"Sait ykkösiin {ykköset()} pisteen.")
                else:
                    print(f"Sait ykkösiin {ykköset()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "2":
            if taulukko["kakkoset"] == "":     
                print(f"Sait kakkosiin {kakkoset()} pistettä.")
                heitot = []    
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "3":
            if taulukko["kolmoset"] == "":        
                print(f"Sait kolmosiin {kolmoset()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "4":
            if taulukko["neloset"] == "":        
                print(f"Sait nelosiin {neloset()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "5":
            if taulukko["vitoset"] == "":        
                print(f"Sait vitosiin {vitoset()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "6":
            if taulukko["kutoset"] == "":        
                print(f"Sait kutosiin {kutoset()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "7":
            if taulukko["yksi pari"] == "":
                print(f"Sait yhteen pariin {yksi_pari()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "8":
            if taulukko["kaksi paria"] =="":
                print(f"Sait kahteen pariin {kaksi_paria()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "9":
            if taulukko["kolmoisluku"] =="":
                print(f"Sait kolmeen lukuun {kolmoisluku()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "10":
            if taulukko["neloisluku"] == "":
                print(f"Sait neljään lukuun {neloisluku()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "11":
            if taulukko["pieni suora"] == "":
                print(f"Sait pieneen suoraan {pieni_suora()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "12":
            if taulukko["iso suora"] == "":
                print(f"Sait isoon suoraan {iso_suora()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "13":
            if taulukko["mökki"] == "":
                print(f"Sait mökkiin {mökki()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "14":
            if taulukko["sattuma"] == "":
                print(f"Sait sattumaan {sattuma()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

        if valinta == "15":
            if taulukko["yatzy"] == "":
                print(f"Sait yatzyyn {yatzy()} pistettä.")
                heitot = []
                heitto_määrä = 3
            else:
                print("Olet käyttänyt tämän vaihtoehdon jo!")

# Kun kaikki kategoriat ovat täynnä
bonus()
loppu_pisteet = 0
for i in taulukko:
    loppu_pisteet += taulukko[i]
print("")
print(f"Lopulliset pisteesi ovat {loppu_pisteet}.")
print(f"Taulokkosi {taulukko}")
