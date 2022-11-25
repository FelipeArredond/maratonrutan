import random
class ProgramaBeneficioPrimeraMilInfancia:
    def __init__(self,beneficiosDisponibles,beneficiosAsignados):
        self.beneficiosDisponibles = beneficiosDisponibles
        self.beneficiosAsignados = beneficiosAsignados

    def crearBeneficio(self):
        self.beneficiosDisponibles += 1
    
    def asignarBeneficio(self, lista):
        ganador = random.randint(0, len(lista)-1)
        lista[ganador].bppi = True
        self.beneficiosAsignados += 1

