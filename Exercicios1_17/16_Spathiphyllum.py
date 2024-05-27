import time
import os

nome = input("Digite o nome da planta: ")
if nome == "Spathiphyllum":
    print("Sim " + nome + " é a melhor planta de todos os tempos")
elif nome == "spathiphyllum":
    print("Não, eu quero a verdadeira Spathiphyllum!!!")
else:
    print("Não é a Spathiphyllum!!!")

time.sleep(3)
os.system('cls')
