# Importando a base de dados
import pandas as pd
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# Alterando todos os nomes da coluna produtos para Maiusculo
minha_funcao = lambda x: str.upper(x)
nomes_maiusculos = list(map(minha_funcao,tabela["Produtos"]))
print('Produtos em Maiúsculo',nomes_maiusculos)



# Fazendo a soma de todos os produtos
from functools import reduce

def f_soma(a,b):
    return a+b
resultado = reduce(f_soma,tabela['Preço Base Reais'])
print("Soma Total do preço base Reais = ",resultado)