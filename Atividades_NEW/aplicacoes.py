import time

#Encontrar o maior valor na lista - Exemplo 1
lista = [17,3,11,5,1,9,7,15,18]
maior_numero = lista[0] #Recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]
print("O Maior numero da lista é: ", maior_numero)

#Exemplo2
my_list = [17,3,11,5,1,9,7,15,18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2: ", maior)

#Exemplo3:
ultima_lista = my_list[:]
mel = ultima_lista
for i in ultima_lista[1:]:
    mel = i
print("Maior valor 3:", mel)

#Enontrar a localização de um determinado elemento dentro de uma lista
frutas = ["Abacaxi", "Maça", "pera", "mamão", "Uva", "Melancia"]
elemento = "Melancia"
achado = False
for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break
if achado:
    print("Elemento encontrado no indice: ", i)
else:
    print("Não encontrado!!!")

#Conferidor de apostas em loteria
sorteados = [5,11,9,42,3,49]
apostados = [3,7,11,42,34,49]
acertos = 0
for numero in sorteados:
    if numero in apostados:
        acertos += 1
print(acertos)

#Remoção de numeros repetidos em uma lista 
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista Original: ", lista)

#Lista de apoio
vistos = []

#Interar pela lista original de tras para frente
for i in range(len(lista) - 1,-1, -1):
    #Se o numero ja esta na lista "vistos", removê-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        #Caso contrario, adicionar a lista "Vistos"
        vistos.append(lista[i])
#Exibir a lista original modificada
print("Lista modificada:", lista)

#listas avançadas 
#20 - Listas aninhadas bidimensionais
tabela = [[":(", ":)",":|",";-;"],
         [";-;", ":|", ":)",":("],
         [":|",":)",";-;",":("]]
print(tabela[2][2])
print(tabela)

#30 - Matriz Tridimencional
cubo = [[[":(","y","z"],[":)","y","z"],[":|","y","z"]],
        [["amor","Odio","caridade"],["paz","esperança","ferias"],["tina","prior","pp"]],
        [["Restinga","patrocionio","rifaina"],["Amazonence","Fluminence", "santos"],["pizza","lasanha","pastel"]]]
print(cubo)
print(cubo[1])
print(cubo[1][0])



time.sleep(3)