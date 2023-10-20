"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

A - comprar apenas latas de 18 litros;
B - comprar apenas galões de 3,6 litros;
C - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere 
latas cheias.

#PRIMEIRA VERSAO SEM USAR METODOS
"""
import math

GALAO_TINTA_LITROS = 3.6
LATA_TINTA_LITROS = 18
PRECO_LATA = 80
PRECO_GALAO = 25
COBERTURA_METROS_LITRO = 6

metros_pintar = float(input("Quantos metros quadrados serão pintados? "))

QUANTIDADE_LITROS_NECESSARIOS = metros_pintar * COBERTURA_METROS_LITRO

quantidade_galao_sem_arredondar = QUANTIDADE_LITROS_NECESSARIOS / GALAO_TINTA_LITROS
quantidade_lata_sem_arredondar = QUANTIDADE_LITROS_NECESSARIOS / LATA_TINTA_LITROS

custo_compra_galoes = quantidade_galao_sem_arredondar * PRECO_GALAO
custo_compras_latas = quantidade_lata_sem_arredondar * PRECO_LATA

#eh_int_lata = isinstance( quantidade_lata_sem_arredondar, int) or (isinstance(quantidade_lata_sem_arredondar, float) and quantidade_lata_sem_arredondar.is_integer())
print("Latas " , quantidade_lata_sem_arredondar)
print("Litros: ", quantidade_lata_sem_arredondar * LATA_TINTA_LITROS)

eh_int_lata = quantidade_lata_sem_arredondar.is_integer()


if eh_int_lata:
    print("*********INT**********")
    print("Para pintar ", metros_pintar , "m2")
    print("Usando somente LATAS de 18 L :")
    print("Latas: " , quantidade_lata_sem_arredondar)
    print("Litros ",(quantidade_lata_sem_arredondar * LATA_TINTA_LITROS))
    print("Valor gasto com galões: R$", custo_compras_latas)
    
else:
    print("***********float**************")
    quantidade_lata_final_arredondada = math.ceil(quantidade_lata_sem_arredondar)    
    desperdicio_lata = ((quantidade_lata_final_arredondada * LATA_TINTA_LITROS)-(quantidade_lata_sem_arredondar * LATA_TINTA_LITROS))
    print("Usando somente LATAS de 18 L :")
    print("Latas: " , quantidade_lata_final_arredondada)
    print("Litros ",(quantidade_lata_final_arredondada * LATA_TINTA_LITROS))
    print("Valor gasto com galões: R$" , custo_compras_latas)
    print("Desperdício de tinta é de: ", desperdicio_lata)    
    
    
    
'''
if isinstance( quantidade_galao_sem_arredondar, int):
    print("Usando somente galões de 3.6 L :")
    print("Quantidade de galões necesarios: " , quantidade_galao_sem_arredondar)
    print("Serão necessarios ",(quantidade_galao_sem_arredondar * GALAO_TINTA_LITROS ))
    print("Valor gasto com galões: " , custo_compra_galoes)
else:
    quantidade_galao_final_arredondada = math.ceil(quantidade_galao_sem_arredondar)    
    desperdicio_galao = quantidade_galao_final_arredondada - quantidade_galao_sem_arredondar
    print("float")
    print("Usando somente galões de 3.6 L :")
    print("Quantidade de galões necesarios: " ,  quantidade_galao_final_arredondada)
    print("Serão necessarios ",(quantidade_galao_final_arredondada * GALAO_TINTA_LITROS ), " L")
    print("Valor gasto com galões: " , custo_compra_galoes)
    print("Desperdício de tinta é de: ", desperdicio_galao)
    '''


#print("Para pintar o(s) ", metros_pintar ," serão nescessários " , QUANTIDADE_LITROS_NECESSARIOS)
#print("Usando galões, serão nescessários ", quantidade_galao_sem_arredondar , "galões de tinta")
