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

quantidade_galao_final_arredondada = 0
quantidade_lata_final_arredondada = 0

quantidade_galao_sem_arredondar = 0
quantidade_lata_sem_arredondar = 0

desperdicio_galao = 0
deperdicio_lata = 0

custo_compra_galoes = 0
custo_compras_latas = 0

metros_pintar = float(input("Quantos metros quadrados serão pintados? "))

QUANTIDADE_LITROS_NECESSARIOS = metros_pintar * COBERTURA_METROS_LITRO

quantidade_galao_sem_arredondar = QUANTIDADE_LITROS_NECESSARIOS / GALAO_TINTA_LITROS

custo_compra_galoes = quantidade_galao_sem_arredondar * PRECO_GALAO

print("Para pintar ", metros_pintar , "m2")
if isinstance( quantidade_galao_sem_arredondar, int):
    print("Usando somente galões de 3.6 L :")
    print("Quantidade de galões necesarios: " , quantidade_galao_sem_arredondar)
    print("Valor gasto com galões: " , custo_compra_galoes)
    
else:
    quantidade_galao_final_arredondada = math.ceil(quantidade_galao_sem_arredondar)    
    desperdicio_galao = quantidade_galao_final_arredondada - quantidade_galao_sem_arredondar
    print("Usando somente galões de 3.6 L :")
    print("Quantidade de galões necesarios: " ,  quantidade_galao_final_arredondada)
    print("Valor gasto com galões: " , custo_compra_galoes)
    print("Desperdício de tinta é de: ", desperdicio_galao)


#print("Para pintar o(s) ", metros_pintar ," serão nescessários " , QUANTIDADE_LITROS_NECESSARIOS)
#print("Usando galões, serão nescessários ", quantidade_galao_sem_arredondar , "galões de tinta")
