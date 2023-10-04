from array import *

precos = array('d', [])
primeira = 1
somador = 0
menor = 0
maior = 0
diferen_precos = 0

for loja in range(1, 8):
    preco = float(input(f"Preço do produto na loja {loja}: "))
    precos.append(preco)

print("== Preços em todas as lojas ==")
for preco_produto in precos:
    print(f"{preco_produto} ", sep=' ', end=' ')
    
    somador += preco_produto

    if primeira == 1:
        maior = preco_produto
        menor = preco_produto
        primeira = 2

    if preco_produto > maior:
        maior = preco_produto

    if preco_produto < menor:
        menor = preco_produto

diferenca_precos = maior - menor
media = somador/7

print(f"""\n\nMedia dos preços: {media}\n\nMaior preço encontrado: {maior} || Menor preço encontrado:{menor}
Diferença entre maior e menor preço encontrado {diferenca_precos}""")
        
