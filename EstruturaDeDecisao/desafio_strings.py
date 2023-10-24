#Primeira versão
"""
numero_de_testes = int(input("Quantos testes?"))

controlador = 0

while(controlador < numero_de_testes):
    entrada = input("Entrada 1:").split(" ")
  
    entrada_a = entrada[0]
    entrada_b = entrada[1]

    ehMaior = entrada_b > entrada_a
    termina = entrada_a.endswith(entrada_a)    
    
    if(ehMaior and termina):
        print("encaixa")
    else:
        print("nao encaixa")    
controlador+=1    

"""
#segunda versão
numero_de_testes = int(input("Quantos testes deseja?"))

for i in range(numero_de_testes):
  entrada = input("Digite em sequência e com um espaço entre os dois lotes de números, ex 123456987 1587").split(" ")
  
  entrada_a = entrada[0]
  entrada_b = entrada[1]

  a_eh_Maior = len(entrada_a) >= len(entrada_b)
  termina = entrada_a.endswith(entrada_b)    
    
  if a_eh_Maior and termina:
    print("encaixa")
  else:
      print("nao encaixa")    
