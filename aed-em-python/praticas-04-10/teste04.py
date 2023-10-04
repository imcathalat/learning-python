from array import *

temperaturas_celsius = array('d', [])
dia_mes = array('i', [])
temperaturas_abaixo_media = array('d', [])
dia_temps_abaixo_media = array('i', [])

soma_temperaturas = 0
primeira = 1
maior_temp = 0
menor_temp = 0
media = 0

for coletar_temperatura_e_dia in range(1, 4):
    temperatura = float(input("Entre com a temperatura: "))
    dia = int(input("Entre com o dia que essa temperatura bateu (1 a 31): "))
    temperaturas_celsius.append(temperatura)
    dia_mes.append(dia)

    soma_temperaturas += temperatura

media = soma_temperaturas/7

for temp in range(len(temperaturas_celsius)):
    
    if primeira == 1:
        maior_temp = temperaturas_celsius[temp]
        menor_temp = temperaturas_celsius[temp]
        primeira = 2

    if temperaturas_celsius[temp] > maior_temp:
        maior = temperaturas_celsius[temp]

    if temperaturas_celsius[temp] < menor_temp:
        menor = temperaturas_celsius[temp]

    if temperaturas_celsius[temp] < media:
        temperaturas_abaixo_media.append(temperaturas_celsius[temp])
        dia_temps_abaixo_media.append(dia_mes[temp])

# For para imprimir informações na tela

print(f"""\nMedia das temperaturas: {media}\n""")

for index in range(len(temperaturas_celsius)):
    print(f"temperatura: {temperaturas_celsius[index]} - dia: {dia_mes[index]}")

print(f"\n Maior temperatura verificada: {maior_temp} || Menor temperatura verificada: {menor_temp}")


