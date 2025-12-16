""" Write a program that calculates the average fuel consumption of vehicles per 100 km. 
The input should be the kilometers driven and the amount of fuel filled."""

gefaherne_km = float(input("Geben Sie die gefahrenen Kilometer ein: "))  # Input for kilometers driven
getanke_menge = float(input("Geben Sie die getankte Menge an Krafstoff: "))  # Input for the amount of fuel tanked.

durchschnittsverbrauch_kraftstoff = (getanke_menge/gefaherne_km) * 100

print("Die Durchnittsverbrauch für die gegebenen werte ist: ", durchschnittsverbrauch_kraftstoff)

## another way to calculate this with the def funktion....
### def average_fuel_consumption(kilometers, fuel_liters):
    """
    Calculate average fuel consumption per 100 km.
    
    Parameters:
    kilometers (float): Distance driven in kilometers
    fuel_liters (float): Fuel consumed in liters
    
    Returns:
    float: Average fuel consumption (liters per 100 km)
    """
    #if kilometers <= 0:
     #   raise ValueError("Kilometers driven must be greater than zero.")
    
    #consumption = (fuel_liters / kilometers) * 100
    #return consumption


# Example usage:
#km = float(input("Enter kilometers driven: "))
#fuel = float(input("Enter fuel consumed (liters): "))

#avg_consumption = average_fuel_consumption(km, fuel)
#print(f"Average fuel consumption: {avg_consumption:.2f} L/100km")