numerador = 1
denominador = int(input("Entre com um numero inteiro: "))
soma = 1
fatorial = 1

for i in range(1, denominador+1):
    print(f"denominador: {denominador} i: {i}")
    for y in range(1, i+1):
        fatorial = (numerador/y) * fatorial
        print(f"denominador: {i} y: {y} numerador: {numerador} fatorial: {fatorial}")
    
    soma += fatorial
    print(f"soma {soma}")

