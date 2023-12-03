 # Python Transition Rechner 

import math

nachricht = "Transition mit Höhe H und Radius R - unten Null Grad" 
print (nachricht)

H = float(input("Höhe eingeben:"))
R = float(input("Radius in der selben Einheit eingeben:"))
T = math.sqrt(2*R*H-H*H)
B = R*math.asin(T/R)
phi = 360*B/(2*math.pi*R)

nachricht2 = "Ergebnisse werden in der selben Einheit ausgegeben!" 
print (nachricht2)


#Rechnenoperationen und Ergebnis ausgeben
print("Tiefe der Transition", T)
print("Bogenlänge der Transition", B)
print("Steigungswinkel oben", phi)

