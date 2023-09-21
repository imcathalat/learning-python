p1 = []
p2 = []

soma_p1 = 0
soma_p2 = 0

notas_p1 = int(input("Quantas notas você deseja cadastrar em p1? "))

for i in range(0, notas_p1):
    notap1 = float(input("Nota: "))
    p1.append(notap1)
    soma_p1 = notap1 + soma_p1

media_p1 = soma_p1/float(notas_p1)

notas_p2 = int(input("Quantas notas você deseja cadastrar em p2? "))

for index in range(0, notas_p2):
    notap2 = float(input("Nota: "))
    p2.append(notap2)
    soma_p2 = notap2 + soma_p2

media_p2 = soma_p2/float(notas_p2)

print("\nApuração\nMedia na prova 1: {}    Media na prova 2: {}".format(media_p1, media_p2))

if media_p1 > media_p2:
    print("A turma obteve a melhor média na prova 1\n")
elif media_p2 > media_p1:
    print("A turma obteve a melhor média na prova 1\n")
else:
    print("As médias nas duas provas coincidem\n")

dif = media_p1 - media_p2