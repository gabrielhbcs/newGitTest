vet = []
resp = 0
qtd = 0
media = 0
total = 0
while True:
    resp = int(input("insira qtd de PTs: \n"))
    if (resp == -1):
        break
    if (resp >= 0):
        qtd += 1
    total += resp
    vet.append(resp)

media = total/qtd
print("Média: " + str(media))
media60 = media
qtd60 = qtd
if media < 60:
    while media60 < 60:
        qtd60 -= 1
        media60 = total/qtd60
    print("Com doações, " + str(qtd60) + " podem participar (media: " + str(media60) + ")")

