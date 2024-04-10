A = 70

def printA():
    print("As esu nauja printA() funkcija")
    print("Dar vienas pakeitimas pypupypu")




class Vehicle():
    def __init__(self, pavadinimas, rida): 
        self.pavadinimas = pavadinimas
        self.rida = rida
class Car(Vehicle):
    def __init__(self, pavadinimas, rida ,seats): 
        super().__init__(pavadinimas, rida)
        self.seats = seats
    def getSeats(self):
        return self.seats

car = Car("pavadinimas" ,5, 20)



class Bus(Vehicle):
    def __init__(self, pavadinimas, rida ,seats): 
        super().__init__(pavadinimas, rida)
        self.seats = seats
    def getSeats(self):
        return self.seats
    
bus = Bus("Pavadinimas",5,20)



class Train(Vehicle):
    def __init__(self, pavadinimas, rida ,seats): 
        super().__init__(pavadinimas, rida)
        self.seats = seats
    def getSeats(self):
        return self.seats    
    

train = Train("Pavadinimas",5,20)






class Txtreader:
    """
    labai kieta mano klase
    """

    def __init__(self, failopavadinimas):
        self.failopavidinimas = failopavadinimas
        self.I = []
        self.U = []
        self.j = []
        self.P = []
    
    def skaitytojas(self):
        """
        labai kieta mano klase2: eros pabaiga
        """
        failas = open(self.failopavidinimas, mode= "r")
        tekstas = failas.readlines()
        failas.close()

        for eilute in tekstas[1:]:
            u =float(eilute.split(";")[0])
            self.U.append(u)
            i =float(eilute.split(";")[1])
            self.I.append(i)
            J =float(eilute.split(";")[2])
            self.j.append(J)
            p =float(eilute.split(";")[3])
            self.P.append(p)

    def maksimalusP(self):
        maximumas = max(self.P)
        return maximumas
    
    def pce(self):
        maximumas = self.maksimalusP()
        ats = maximumas / 1000 * 100
        return ats
    



class Mokinys():
    def __init__(self, vardas , pavarde , pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def vidurkisf(self):
        vidurkis = sum(self.pazymiai) / len(self.pazymiai)
        return vidurkis
    
    def didziausiaspazymysf(self):
        dickis = min(self.pazymiai)
        return dickis
    
    def maizausiaspazymysf(self):
        mazius = max(self.pazymiai)
        return mazius    
    
class Abiturientas(Mokinys):
    def __init__(self, vardas , pavarde , pazymiai , egzaminas):
        super().__init__(vardas , pavarde , pazymiai)
        self.egzaminas = egzaminas

    def vidurkissuegzaminuf(self):
        pazymiaisuegazimu = self.pazymiai + self.egzaminas
        # self.pazymiaisuegzaminu = pazymiaisuegazimu
        vidurkissuegzaminu = sum(pazymiaisuegazimu) / len(pazymiaisuegazimu)
        return vidurkissuegzaminu

class Mokykla():
    def __init__(self):
        self.Mokiniai = []

    def addmokinys(self, mokinys):
        self.Mokiniai.append(mokinys)
    
    def removeMokinys(self, mokinys):
        self.Mokiniai.remove(mokinys)

    def VisumokiniuVidurkis(self):
        VisumokiniuPazymiai = []
        for mokinys in self.Mokiniai:
            VisumokiniuPazymiai.extend(mokinys.pazymiai)
        VisumokiniuVidurkis = sum(VisumokiniuPazymiai) / len(VisumokiniuPazymiai)
        return VisumokiniuVidurkis
    
mokinys = Mokinys("Mantvydas" , "Vorobjovas" , [7,8,9,10,7,4,9])
mokinys2 = Mokinys("Vardenis2" , "Pavardenis2" , [7,8,9,10,7,4,9])
mokinys3 = Mokinys("Vardenis3" , "Pavardenis3" , [7,2,5,10,7,4,5])

abiturientas = Abiturientas("Mantvydas" , "Vorobjovas" , [7,8,9,5],[6,9])

