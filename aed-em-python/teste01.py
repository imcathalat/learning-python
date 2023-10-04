flag = 's'
joao = 0
paulo = 0
maria = 0
nulo = 0

def mais_e_menos_votados(joao, paulo, maria):
    if joao>paulo and paulo>maria:
        var_mais_votado = "Candidato joao foi o mais votado com {} votos e candidata maria foi a menos votada com {} votos".format(joao, maria)
    elif joao>maria and maria>paulo:
        var_mais_votado = "Candidato joao foi o mais votado com {} votos e candidato paulo foi o menos votado com {} votos".format(joao, paulo)
    elif paulo>joao and joao>maria:
        var_mais_votado = "Candidato paulo foi o mais votado com {} votos e candidata maria foi a menos votada com {} votos".format(paulo, maria)
    elif paulo>maria and maria>joao:
        var_mais_votado = "Candidato paulo foi o mais votado com {} votos e candidato joao foi o menos votado com {} votos".format(paulo, joao)
    elif maria>joao and joao>paulo:
        var_mais_votado = "Candidata maria foi a mais votada com {} votos e candidato paulo foi o menos votado com {} votos".format(maria, paulo)
    elif maria>paulo and paulo> joao:
         var_mais_votado = "Candidata maria foi a mais votada com {} votos e candidato joao foi o menos votado com {} votos".format(maria, joao)
    else:
        var_mais_votado = "empate"
    
    return var_mais_votado

while flag == 's':
    voto = int(input("\nCandidatos: (1)João (2)Paulo (3)Maria (4)Nulo\nSeu voto: "))
    if voto == 1:
        joao += 1
    elif voto == 2:
        paulo += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        nulo += 1
    
    flag = input("Deseja contabilizar outro voto? s/n ")

apuracao_final = mais_e_menos_votados(joao, paulo, maria)

print(f"\n=== APuração ===\nJoão: {joao} Paulo: {paulo} Maria: {maria} Nulos: {nulo}\n{apuracao_final}")

