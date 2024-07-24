import time

numero1 =int(input("Digite um numero: "))
resultado = numero1 % 2
while(numero1 < 0):
    print("ERROR!!!")
    break
if resultado == 0:
        print('""P-A-R!!!""')
if resultado == 1:
        print("Tente outra vez")

time.sleep(4)