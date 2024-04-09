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