
## here we have a escape handling sequence which is useful when we are writing a code or a part of code and we are not sure that it will,
# retutrn a mistake.We so to protect the code we are using the Escape Handling in Python.
# when we are using the escape handling it starts with try and must have a except also.

try:
  
  print("Proigarm zur berechnuhg eiine Durchnittstempeartur \n") 
  print("Geben sie bitte drei Temperature in °C ein! ")
  temperatur1 = float(input("1, Wert: ")) # the 1 variable
  temperatur2 = float(input("2, Wert: ")) #  the 2 variable
  temperatur3 = float(input("3, Wert: ")) # the 3 variable
  durchnittstemperatur = (temperatur1 + temperatur2 + temperatur3) / 3 # varibale for calculating the average temperature.
  # print funktion with 3 place holders {} for the arguments,that are passed to the format.
  # .format is a string method that replaces placeholders witha actual values.
  print("Sie haben folgende Tempearturen eingegeben: {0} °C, , {1} °C, {2} °C".format(temperatur1, temperatur2, temperatur3))  

  print("Die durchnittstemperatur beträg6t: {0:.2f} °C".format(durchnittstemperatur))
 
except Exception as e:
 ## \n - to print the cursor in a new line,+ is a string concatenation, e.args[0] - access the first element of the exception object.
 print("Es ist folgender Fehler aufgetreten: \n" + e.args[0]) 

