fahrenheit = float(input("Enter a temperature in degrees F: "))

def convert_fah_to_cel(f):
    celsius = (f- 32) * (5/9)
    return celsius

celsius_convertidos = convert_fah_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F = {celsius_convertidos} degrees C")

celsius = float(input("\nEnter a temperature in degrees C: "))

def convert_cel_to_fah(c):
    """converte graus celsius para fahrenheit""" #docstring
    fahrenheit = c * (9/5) + 32
    return fahrenheit

fah_convertidos = convert_cel_to_fah(celsius)

print(f"{celsius} degrees C = {fah_convertidos} degrees F")
