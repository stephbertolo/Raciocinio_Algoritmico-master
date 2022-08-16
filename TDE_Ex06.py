import math

catetoUm = float(input("Digite o cateto um: "))
catetoDois = float(input("Digite o cateto dois: "))
somaCatetos = (catetoUm ** 2) + (catetoDois ** 2)
somaCatetos =math.sqrt(somaCatetos)

print("A hipotenusa é: " +str(somaCatetos))