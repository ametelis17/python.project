

class Catalog:
    lista_obiecte = []
    clasa = ""
    subclasa = ""

    def __init__(self, pret, consum, producator, cod_produs):
        self.pret = pret
        self.consum = consum
        self.producator = producator
        self.cod_produs = cod_produs

        Catalog.lista_obiecte.append(self)

     def sorteaza_dupa_pret(self):
         for obiect in sorted(Catalog.lista_obiecte, key = lambda self: self.pret):
             obiect._afiseaza_rezultate()



             pass

      def sorteaza_dupa_consum(self):
          for obiect in sorted(Catalog.lista_obiecte, key - lambda self: self.consum):
              obiect._afiseaza_rezultate()


     def cauta_dupa_producator(self,producator):
         for obiect in lista_obiecte:
             if producator == obiect.producator:
                 print producator


class Electrocasnice_mici(Catalog):
    def __init__(self, pret = 100, consum = "3kwh", producator = " ",cod_produs = 223,adancime, latime, inaltime):
        super(Catalog).__init__(pret, consum, producator)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime

        pass

        
class Electrocasnice_mari(Catalog):
    def __init__(self, pret,consum,producator,cod_produs,lungime_cablu,baterie):
    super(Catalog).__init__(pret, consum, producator)
    self.lungime_cablu = lungime_cablu
    self.baterie = baterie
    pass

class 

class Frigider(Electrocasnice_mari):
   clasa = "Electrocasnice Mari"
   subclasa = "Frigider"
   def __init__(self, pret, consum,producator,cod_produs,lungime_cablu,baterie,capacitate_congelator,capacitate_frigider):
       super(Catalog).__init__(pret, consum, producator)
       super(Electrocasnice_mari).__init__(lungime_cablu,baterie)
       self.capacitate_frigider = capacitate_frigider
       self.capacitate_congelator = capacitate_frigider
       pass

class Aragaz(Electrocasnice_mari):
    clasa = "Electrocasnice mari"
    subclasa = "Aragaz"

    def __init__(self, pret, consum,producator,cod_produs,lungime_cablu,baterie,capacitate_congelator,capacitate_frigider,nr_arzatoare):
    super(Catalog).__init__(pret, consum, producator)
    super(Electrocasnice_mari).__init__(lungime_cablu,baterie)
    self.nr_arzatoare = nr_arzatoare
    pass

class Mixer(Electrocasnice_mici):
clasa = "Electrocasnice mici"
subclasa = "Mixer"
    def __init__(self, pret = 100, consum = "3kwh", producator = " ",cod_produs = 223,adancime, latime, inaltime,rotatii_min)
    super(Catalog).__init__(pret, consum, producator)super(Catalog).__init__(pret, consum, producator)
    super(Electrocasnice_mici).__init__(adancime,latime,inaltime)
    self.rotatii_min = rotatii_min
    pass

class Fier_calcat(Electrocasnice_mici):
clasa = "Electrocasnice mici"
subclasa = "Fier calcat"
    def __init__(self, pret = 100, consum = "3kwh", producator = " ",cod_produs = 223,adancime, latime, inaltime,rezervor)
    super(Catalog).__init__(pret, consum, producator)super(Catalog).__init__(pret, consum, producator)
    super(Electrocasnice_mici).__init__(adancime,latime,inaltime)
    self.rezervor = rezervor
    pass

frigider_cu_congelator = Frigider()
frigider_fara_congelator = Frigider()

plita = Aragaz()
maner = Aragaz()

maner = Mixer()
mixer_200w = Mixer()

    

    
    

    
   
