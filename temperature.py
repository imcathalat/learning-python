fahrenheit = float(input("Enter with a temperature in Fahrenheit: "))

def convert_fah_to_cel(f):
    celsius = (f- 32) * (5/9)
    return celsius

celsius_convertidos = convert_fah_to_cel(fahrenheit)
print(f"{fahrenheit} graus fahrenheit são {celsius_convertidos} graus celsius")

celsius = float(input("Enter with a temperature in Celsius: "))

def convert_cel_to_fah(c):
    """converte graus celsius para fahrenheit"""
    fahrenheit = c * (9/5) + 32
    return fahrenheit

fah_convertidos = convert_cel_to_fah(celsius)

print(f"{celsius} graus celsius são {fah_convertidos} graus fahrenheit")
