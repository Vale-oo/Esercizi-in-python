#scrivere cicli di iterazione for e while

import random
sommaPos=0
contaPos=0
sommaNeg=0
contaNeg=0
contaZeri=0

for i in range (0, 10):
    contatore = random.randint(-1000, 1000)
    print("Numero in posizione", i+1, "e'", contatore)

    if contatore > 0 :
        sommaPos += contatore
        contaPos+=1
    elif contatore < 0:
        sommaNeg += contatore
        contaNeg+=1
    elif contatore == 0:
        contaZeri+=1

mediaPos=sommaPos/contaPos
mediaNeg=sommaNeg/contaNeg

print(" ")
print("I numeri positivi comparsi sono in totale:", contaPos)
print("La somma dei numeri positivi è:", sommaPos)
print("La media dei numeri positivi è:", mediaPos)
print(" ")

print("I numeri negativi comparsi sono in totale:", contaNeg)
print("La somma dei numeri negativi è:", sommaNeg)
print("La media dei numeri negativi è:", mediaNeg)
print(" ")

print("Le volte che è uscito 0 come numero randomico:", contaZeri)