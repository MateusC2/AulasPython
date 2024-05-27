import time
import os

ano = int(input("Escreva o ano desejado:"))

if ano % 4 != 0:
    print("É um ano comum")
    if ano % 100 != 0:
        print()

time.sleep(3)
os.system('cls')