""" Write a program that calculates the average fuel consumption of vehicles per 100 km. 
The input should be the kilometers driven and the amount of fuel filled."""

gefaherne_km = float(input("Geben Sie die gefahrenen Kilometer ein: "))  # Input for kilometers driven
getanke_menge = float(input("Geben Sie die getankte Menge an Krafstoff: "))  # Input for the amount of fuel tanked.

durchschnittsverbrauch_kraftstoff = (getanke_menge/gefaherne_km) * 100

print("Die Durchnittsverbrauch für die gegebenen werte ist: ", durchschnittsverbrauch_kraftstoff)
