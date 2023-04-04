import csv
from re import X
#define a funcao e cria as string para dados e marcacoes
def carregar_acessos():
    X = []
    Y = []
#abre o arquivo dos dados e le com reader()
    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)
    #cria as classes e define os valores
    for home, como_funciona, contato, comprou in leitor:

        #utiliza append() para add os dados nas classes
        X.append([int(home),
            int(como_funciona),
            int(contato)])
        Y.append(int(comprou))

    return X, Y

        
def carregar_buscas():
    X = []
    Y = [] 

    #abre o arquivo dos dados e le com reader()
    arquivo = open('buscas.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home, busca, logado, comprou in leitor:
        dado = [int(home),str(busca), int(logado)]
        X.append(dado)
        Y.append(int(comprou))
        

    return X, Y

   