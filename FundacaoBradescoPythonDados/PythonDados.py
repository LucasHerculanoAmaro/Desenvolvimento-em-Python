# Primeiro Exemplo


# Cria uma lista com sete elementos.
#minha_lista = ['alfa','beta','teta', 'gama','sigma','delta','iota']

# Mostra os elementos da lista.
#print(minha_lista)

# Conta o número de elementos da lista.
#print(len(minha_lista))

"""
Resultado no Console:

    ['alfa', 'beta', 'teta', 'gama', 'sigma', 'delta', 'iota']
    7

O código print(minha_lista) irá apresentar no conlose o que está dentro do array minha_lista.
O código print(len(minha_lista)) irá apresentar a quantidades de itens que há no array minha_lista.
"""

# Segundo Exemplo


# Cria uma string e a carrega em uma variável.
#s = ['Banco', 'de', 'Dados']

# Acessa o segundo caractere e o exibe na tela.
#print (s[0])

"""
Você tem 3 posições dentro do array (0, 1 e 2), onde: 
    0 representa 'Banco', 
    1 representa 'de',
    2 representa 'Dados'.
    
Quando você adiciona 'print (s[n])' e substitui o 'n' por '1', '2' ou '3', os valores apresentados serão os valores contidos no array em suas determinadas posições.
Lembrando que, em uma lista, as posições são baseadas em números, por exemplo:
    minha_lista = [posição 0, posição 1, posição 2, posição 3...]
"""

# Exemplo 3

#Criando uma lista com dois elementos numéricos em uma lista
lista=[8,9]

#Inserindo um número a lista
lista.append(10)
lista.append('palavra')

#Mostrando a nova lista
print(lista)

"""
Até aqui utilizando 'lista.append(10)', os valores apresentados na lista é:
    [8, 9, 10]
"""

"""
Ao adicionar o script 'lista.append('palavra)', o resultado será:
     [8, 9, 10, 'palavra']
"""
