def stampaDizionario(diz):
    for key,value in diz.items():
        print("la chiave è ..."+key)
        print("il valore è ..."+str(value))

def totaleOre(dict):
    somma=0
    for key, value in dizionario.items():
     somma = somma + value
    return (somma)

def cattedraPiena(contatore):
    contatore=0
    for key, value in dizionario.items():
        if value == 18:
            contatore+=1


def modifica(diz,prof,ore):
    if prof in diz:
        diz[prof]=ore

#def scalaOre(diz, prof, ore):
   # if ore in prof and prof in diz:






dizionario = {"rossi":18, "bianchi":16, "verdi":6}
#inserire un elemento dentro al dizionario
dizionario["viola"]=14
print(dizionario)
#modificare una coppia chiave valore
dizionario["bianchi"]=18 
print(dizionario)

modifica(dizionario,"rossi",6)
print(dizionario)

#iterare sul dizionario
#for key,value in dizionario.items():
   # print("la chiave è ..."+key)
   # print("il valore è ..."+str(value))

#calcolare il totale delle ore del dizionario
somma=0
for key, value in dizionario.items():
    somma = somma + value
print("la somma delle ore è"+str(somma))

#numero degli insegnanti con cattedra piena (18)
contatore=0
for key, value in dizionario.items():
    if value == 18:
        contatore+=1

print("il numero degli insegnanti con cattedra piena sono"+str(contatore))

stampaDizionario(dizionario)



