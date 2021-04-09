qtdSegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = qtdSegundos // 86400

qtdSegundos = qtdSegundos % 86400

horas = qtdSegundos // 3600

qtdSegundos = qtdSegundos % 3600

minutos = qtdSegundos // 60

segundosFinais = qtdSegundos % 60

print(dias , "dias," ,horas, "horas," , minutos , "minutos e" , segundosFinais ,"segundos.")
