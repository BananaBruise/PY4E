# prompts user for Celsius temperature
# and convert to Fahrenheit
temp_c = float(input("Celcius temp: "))
temp_f = (temp_c * 9/5) + 32
print("Fahrenheit temperature:", round(temp_f,2))