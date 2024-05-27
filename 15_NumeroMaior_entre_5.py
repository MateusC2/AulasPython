import time
numero1 = int(input("Digite o primeiro numero (inteiro): "))
numero2 = int(input("Digite o segundo numero (inteiro): "))
numero3 = int(input("Digite o terceiro numero (inteiro): "))
numero4 = int(input("Digite o quarto numero (inteiro): "))
numero5 = int(input("Digite o quinto numero (inteiro): "))

#Assumir que o primeiro numero é maior
numeroMaior = numero1

#Verificar se o segundo numero é maior que o primeiro
if(numero2 > numeroMaior):
    numeroMaior = numero2
if(numero3 > numeroMaior):
    numeroMaior = numero3
if(numero4 > numeroMaior):
    numeroMaior = numero4
if(numero5 > numeroMaior):
    numeroMaior = numero5



print("Numero maior é:", numeroMaior)
#Utilizando uma forma mais direta com a função interna do Python chamada max
numeroMaior2 = max(numero1, numero2, numero3, numero4, numero5)

print("O maior valor com MAX é: ", numeroMaior2)



time.sleep(5)