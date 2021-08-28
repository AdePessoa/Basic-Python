# Importação de bibliotecas
from random import randint
from time import sleep

# Função de Sorteio com Sleep
def sorteia(lista):
    print('Sorteando lista de números aleatórios: ', end='')
    for cont in range(0,10): # Escolhe 10 numeros no total
        n= randint(1,100) # Escolhe os numeros de 0 - 100
        lista.append(n) # Adiciona na lista geral
        print(f'{n} ', end='', flush=True)
        sleep(0.3) # Tempo de sorteio (0,3 segundos)
    print('PRONTO')


# Função de somar par
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print (f'Somando os valores pares da lista {lista}, temos {soma}')

# Função de somar impar
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