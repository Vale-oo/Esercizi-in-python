import random



nome = input ("Come ti chiami? ")


for i in range (1, 10):
    num1 = random.randint(-100000000, 100000000)
    print (i)

print ("Piacere", nome,", io sono", num1)

print ("Fine")