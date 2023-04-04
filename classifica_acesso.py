from dados import carregar_acessos

X,Y = carregar_acessos()

treino_dados = X[:50]
treino_marcacoes = Y[:50]

teste_dados = X[-49:]
teste_marcacoes = Y[-49:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados , treino_marcacoes)

print(modelo.predict([[1,0,1],[0,1,0],
                     [1,0,0], [1,1,0], [1,1,1]]))


resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acerto = [d for d in diferencas if d == 0]
total_de_acertos = len(acerto)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print (taxa_de_acerto)
print(total_de_elementos)