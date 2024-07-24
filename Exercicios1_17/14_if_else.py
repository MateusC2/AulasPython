#Como identificar o maior de 2 (dois) números 
import time

#Ler dois numeros
numero1 = int(input("Digite o primeiro numero (inteiro): "))
numero2 = int(input("Digite o segundo numero (inteiro): "))

#Verificando qua o maior numero
if numero1 > numero2:
    numeroMaior = numero1
elif numero1 == numero2:
    numeroMaior = "São iguais"
else:
    numeroMaior = numero2
print("O numero maior é:", numeroMaior)

#Outra notação de if else em Python
if numero1 > numero2: numeroMaior = numero1
else: numeroMaior = numero2


time.sleep(5)