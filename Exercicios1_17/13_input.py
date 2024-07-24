import time 

#Solicita ao usuario a hora de inicio do evento, o valor recebido é convertidoem inteiro na variavel
hour = int(input("Hora de inicio(horas): "))

#O valor recebido é convertido em inteiro, na variavel minutos
mins = int(input("Hora de inicio (minutos): "))

#Seguindo a lógica anterior, a duração é convertida em inteiro
duration = int(input("Duração do evento (minutos): "))

#atualizando o valor de mins 
mins = mins + duration 

#Calculo de horas contidas nos minutos acumulados
hour = hour + mins // 60
#print("Hour:", hour)

#Calculo do restante de minutos apos a conversão das horas
mins = mins % 60
#print("Resto de minutos: ", mins)

#Ajuste da hora para garantia do formato 0 a 23h
hour = hour % 24
#print("Hour % 23:", hour)

#Exibição do resultado do processo
print (hour,":", mins,sep="")


time.sleep(5)