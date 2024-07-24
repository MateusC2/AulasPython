import time
print("Digite 1 para converter Milhas em KM")
print("Digite 2 para converter Km em Milhas")
convert=float(input("Escolha o numero: "))
if convert < 1:
    print("ERROR!!!")
    print("Tente outra vez!")
if convert > 2:
    print("ERROR!!!")
    print("Tente outra vez!")
if convert == 1:
    milhas = float(input("Digite a quantidade de Milhas: "))
    milhas = milhas * 1.6 //1
    print("O valor será aproximandamente: ", milhas, "KM")
if convert == 2:
    KM = float(input("Digite a quantidade de KM: "))
    KM = KM / 1.6 //1
    print("O valor será aproximadamente: ", KM, "KM")


    time.sleep(5)