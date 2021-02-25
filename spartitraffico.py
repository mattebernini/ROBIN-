import csv 

def getDizionario():
    nuovoDizionario = {}
    with open("./memoria/dizionario.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        keys = [
            (riga[0]) for riga in lettore 
        ]
         
    with open("./memoria/dizionario.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        values = [
            (riga[1]) for riga in lettore 
        ]
        
    c = 0
    for i in keys:
        nuovoDizionario[i] = values[c]
        c += 1
    return nuovoDizionario

def eliminaDoppioni(lista):
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
    return lista

def getConta():
    nuovoDizionario = {}
    with open("./memoria/dizionario.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        keys = [
            (riga[1]) for riga in lettore 
        ]
    keys = eliminaDoppioni(keys)
    for i in keys:
        nuovoDizionario[i] = 0
    return nuovoDizionario


def scegli(domanda):
    parole = domanda.split(" ")
    MioDizionario = getDizionario()
    conta = getConta()

    #if parole[0].lower() != "robin":
    #   return "non valido!"

    for i in parole:
        for key in MioDizionario.keys():
            if i.lower() == key:
                conta[MioDizionario[key]] += 1

    # scelgo il comando che ha il conta più alto
    conta_max = 0
    comando = "niente"
    for key in conta.keys():
        if conta[key] > conta_max:
            conta_max = conta[key]
            comando = key 
    return comando.lower()