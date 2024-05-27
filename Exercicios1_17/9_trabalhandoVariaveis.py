#Acionando a função time
import time
import os

print("Iniciando o sistema")
time.sleep(3)
os.system("cls")
var = 1
print(var)
var = var + 10
print(var)



#Imprimir 10 vezes a palavra Amor pulando quebrando a linha
var = "Amor"
var = (var + "\n") *10
print(var)
print()
print()
#--------------------------------------------------------------
#definindo o valor das variaveis
a=3.
b=4. #É o mesmo que 4.0
c = (a ** 2 + b ** 2) ** 0.5
print(c)

os.system('cls') #Limpa a tela
#Ecpressões completa
x=2
y=3

x = x * 2 #Numero x 2
print(x)#4
y=y+1 #Numero + 1 (incrementp)
print(y)#4

#Forma abreviada (atalho) Multiplicação
x*=2
print(x)#8

#Forma abreviada (atalho do incremento) 

y+= 1
print(y)#5

y-=1
print(y)

print("-------------------------------")

os.system('cls')
#Arredondando um valor
_decimal = 54.6
print(round(_decimal))


print("-------------------------------")

#Testando o INPUT
# anything= float(input("Digite um número: "))
# something = anything ** 2.
# print(anything, "elevado a 2 é: ", something)

os.system('cls')


valor=100
print("Valor: ", valor)

#Qual o TIPO de valor?
print("Tipo da variavel: ",type(valor))

#Convertendo valor para string
print("Tipo novo da variavel: ", type(str(valor)))
print("Novo valor: ", valor)
print("Valor x 2: ", valor*2)

valor=str(valor)
print(type(valor))
print("Valor x 2(???): ", valor * 2)




#Espera de 5 segundos para execução do código
time.sleep(5)