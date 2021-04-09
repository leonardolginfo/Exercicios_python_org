import math

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

delta = (b**2)-4*a*c

if(delta >= 0):
    delta_teste = math.sqrt(delta)
    #print("Delta =", delta_teste)

if (delta < 0):
    print("Não existe raiz, pois o delta é menor que 0.")
elif (delta_teste == 0):
    print("Como o Delta é igual a 0, teremos duas raizes reais e iguais.")
    raiz1 = (-b + delta_teste)/2*a
    print("As raizes soluções serão:", raiz1, "e,", raiz1)

else:
    print("Como o Delta é maior que 0, teremos duas raízes reais diferentes")
    raiz1 = (-b + delta_teste)/2*a
    raiz2 = (-b - delta_teste)/2*a
    print("As raizes soluções serão:", raiz1, "e", raiz2)
