precoProduto = float(input("Digite o preço do produto aqui: "))
tresParcelas = precoProduto / 3
jurosParcelas = (tresParcelas / 100) * 5
duasParcelas = precoProduto / 2
aVista = precoProduto - ((precoProduto / 100) * 5)

print("Três parcelas com juros: " +str(jurosParcelas) +"\n" +
      "Duas parcelas sem juros: " +str(duasParcelas) + "\n" +
      "À vista: " +str(aVista))
