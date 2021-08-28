#Gerar dez números aleatórios e apresentar como saída a soma dos números pares e a soma dos números ímpares
# Importação de bibliotecas
from random import randint

# Função de Sorteio 
def sorteia(lista):
    print('Lista de dez números aleatórios: ', end='')
    for cont in range(0,10): # Escolhe 10 números no total
        n=randint(1,100) # Escolhe os números de 0 - 100
        lista.append(n) # Adiciona na lista geral
        print(f'{n} ', end='', flush=True)
    print('===== Pronto!')

# Função de somar pares
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print (f'Somando os valores pares da lista {lista}, temos {soma}')

# Função de somar ímpares
def somaimpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 1:
            soma += valor
    print (f'Somando os valores ímpares da lista {lista}, temos {soma}')

# Programa Principal
numeros = list ()

# Chamando Funções
sorteia(numeros)
print('='* 30)
somapar(numeros)
print('='* 30)
somaimpar(numeros)