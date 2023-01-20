''' O mód random gera coisas aleatórias que podem ser utilizadas'''
#Importando o mód random 
import random

nove_digitos = ''
#Utilizando o mód random com o randint para gerar núm aleatórios inteiro de 0 até 9 e convertendo para string.
for i in range(9):
    nove_digitos += str(random.randint(0, 9)) # Gerando números de 0 a 9 

contador_regressivo_1 = 10 # Contador utilizado para fazer a piteraação pelo CPF

resultado_digito_1 = 0 
for digito_1 in nove_digitos: #O laço para fazer a iteração no CPF.
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 # Variável que armazena os valores da multip 
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10 ) % 11  #Resultado da verificação do resto da divisão do 1 dig.
digito_1 = digito_1 if digito_1 <= 9 else 0 #Operação ternária.

print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0 
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10 ) % 11  #Resultado da verificação do resto da divisão do 2 dig.
digito_2 = digito_2 if digito_2 <= 9 else 0 #Operação ternária.
print(digito_2)

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

print(cpf_gerado)