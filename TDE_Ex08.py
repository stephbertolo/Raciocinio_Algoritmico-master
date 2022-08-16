import math

alturaInput = float(input("Escreva a altura do cilíndro: "))
raioInput = float(input("Escreva o raio do cilíndro: "))

precoLata = 50.00
litrosLata = 5
litrosMetro = 3

volumeCilindro = math.pi * (raioInput ** 2) * alturaInput     #volume do cilíndro dado o input do jogador
latasMetro = litrosLata * litrosMetro     #quantidade de latas necessárias para pintar cada metro
precoTotal = precoLata * latasMetro       #preço total das latas necessárias
cilindroMetros = (raioInput ** 2) * alturaInput  #conversão do cilíndro de volume para metros
qtdLatas = cilindroMetros / latasMetro

print("O custo em R$ é: " + str(precoTotal) + " e a quantidade de latas é: " + str(qtdLatas))