 # Python Transition Radius Rechner 

import math

print ("Alle Eingaben müssen in der selben Einheit erfolgen!")
print ("Programm berechnet den Radius aus Sekantenstücklänge L und Abstand a der Sekantenmitte zur Transition")
L = float(input("Sekantenabschnitt L = "))
a = float(input("Abstand Mitte zur Transition a = "))

R = a/2+L**2/(8*a)


#Radius ausgeben
print("Radius - in der selben Einheit wie Daten - beträgt R = ", R)

#Programmpause
input("Enter drücken um Messfehler zu berechnen")

#Fehlerberechnung für den Radius
print("Fehlerberechnung für den Radius. Dazu Messfehler für Sekantenstücklänge L und Abstand a der Sekantenmitte zur Transition eingeben - Alle Eingaben müssen in der selben Einheit angeben werden.")
DeltaL = float(input("Fehler Sekantenabschnitt = "))
Deltaa = float(input("Fehler Abstand Mitte zur Transition = "))

dRdL = L/(4*a)
dRda = 1/2-L**2/(8*a**2)
DeltaR = math.sqrt((dRda*Deltaa)**2+(dRdL*DeltaL)**2)

#Messfehler Radius ausgeben
print("Ungenauigkeit beim Radius beträgt", DeltaR)
