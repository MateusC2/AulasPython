import time
# etapa 1
beatles = []
print("Etapa 1:", beatles)

time.sleep(0.5)
# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

time.sleep(0.5)
# etapa 3
for i in range(2):
    beatles.append(input("Digite os novos membros da banda: "))
print("Etapa 3:", beatles)

time.sleep(0.5)
# etapa 4
del beatles [-2]
del beatles [-1]
print("Etapa 4:", beatles)
time.sleep(0.5)
# passo 5
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)


time.sleep(2)
# testando o tamanho da lista

print("o fabuloso", len(beatles))

