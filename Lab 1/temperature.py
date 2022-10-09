# Takes a temperature in celsius, does a conversion to fahrenheit and concatenates it with other strings in a print statement.
temp_celsius = int(input("Enter the temperature in Canada (in degrees Celsius): ")) # Asks the user to type in the temperature
temp_fahrenheit = ((temp_celsius * 9)//5) + 32 # Conversion from celsius to fahrenheit
print("" + str(temp_celsius) + " degrees in Canada would be " + str(temp_fahrenheit) + " degrees in Springfield. D'oh!") # Prints out the converted celsius to fahrenheit