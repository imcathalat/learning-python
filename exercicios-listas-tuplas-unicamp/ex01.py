

lista = []

n = int(input("Qual tamanho da sua lista? "))


for i in range(0,n):
    num = int(input("Digite um numero pra lista: "))
    lista.append(num)


for lista2 in lista:
    if lista2 % 2 == 0:
        lista.remove(lista2)

print(lista)



