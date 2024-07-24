import time
while True:
    try:
        value = int(input("Digite um numero natural: "))
        print("O recíproco do", value, "é: ", 1/value)
        print("")
        time.sleep(1)
    except ValueError:
        print("Número inválido!!!")
        print()
        time.sleep(1)
    except ZeroDivisionError:
        print("Zero não é divisor")
        print()
        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        print("Algo de errado não está certo!!!")
time.sleep(3)
