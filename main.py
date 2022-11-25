import random
import datetime
import os
from pathlib import Path

def genData():
    return random.randint(500000,1000000)

def genDoc():
    return str(random.randint(1000000000, 9999999999))

def genDate():
    mes = random.randint(1,12)
    año = random.randint(2000,2005)
    if mes == 1 or mes == 3 or mes ==  5 or mes == 7 or mes == 8 or mes == 10 or mes ==  12:
        dia = random.randint(1,31)
    elif mes == 2:
        if año == 2004:
            dia = random.randint(1,29)
        else:    
            dia = random.randint(1,28)
    else:
        dia = random.randint(1,30)
    return str(dia) + '/' + str(mes) + '/' + str(año)

def genGender():
    return random.choice(['Masculino','Femenino'])

def genBen():
    return random.choice(['Si','No'])

def genLoc():
    return str(random.randint(1,16))

if __name__ == '__main__':
    current_time = datetime.datetime.now()
    path = os.getcwd()
    fileToCreate = str(current_time)+'.csv'
    Path(fileToCreate).touch()
    ans = ""
    datos = genData()
    print(f"La cantidad de registros es: {datos}")
    f = open(f"{fileToCreate}", 'w')
    f.write("DI;FECHA;GENERO;BENEFICIARIO PD;BENEFICIARIO PPI;BENEFICIARIO PEA;LOCALIDAD\n")
    for i in range(0, datos):
        ans = genDoc() + ";" + genDate() + ";" + genGender() + ";" + genBen() + ";" + genBen() + ";" + genBen() + ";" + genLoc() + "\n"
        f.write(ans)
    f.close()

