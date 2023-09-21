l1 = []
l2 = []
l3 = []

tam_l1 = int(input("Tamanho da lista L1: "))

for i in range(0, tam_l1):
    num = input("L1: ")
    l1.append(num)


tam_l2 = int(input("Tamanho da lista L2: "))

for i in range(0, tam_l2):
    num = input("L2: ")
    l2.append(num)


l3 = l1 + l2

print(l1)
print(l2)
print(l3)

crescente = sorted(l3)
decrescente = sorted(l3, reverse=True)

print("\n\nCrescente: {}    Decrescente: {}\n".format(crescente, decrescente))

# pesquisar sobre como identificar e excluir elementos duplicados da lista
