import random
class ProgramaPS:
    def __init__(self, benDis, benAs):
        self.beneficiosDisponibles = benDis
        self.beneficiosAsignados = benAs

    def crearBeneificio(self):
        self.beneficiosDisponibles+=1
    
    def asignarBeneficio(self, lista):
        ganador = random.randint(0, len(lista)-1)
        lista[ganador].bpps = True
        self.beneficiosAsignados += 1