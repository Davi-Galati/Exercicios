
'''
Cubo e quadrado

O número 729 tem uma particularidade interessante: é ao mesmo tempo o cubo e o quadrado de um número inteiro ( 729 = 272 e 729 = 93). Outro número com essa particularidade é 4096 (4096 = 642 e 4096 = 163). Sua tarefa é, dados dois números inteiros A e B, determinar quantos números no intervalo entre A e B são ao mesmo tempo cubo e quadrado de um número inteiro.
Entrada
A primeira da entrada contém um inteiro A, o limite inferior do intervalo de interesse, a segunda linha contém um inteiro B, o limite superior do intervalo de interesse (A e B fazem parte do intervalo de interesse).
Saída
Seu programa deve produzir uma única linha na saída, contendo um único inteiro, a quantidade de números que são ao mesmo tempo cubo e quadrado de um número inteiro, para todos os números do intervalo de interesse.
Restrições

    1 ≤ A < B ≤ 100 000 000 

Informações sobre a pontuação

    Para um conjunto de casos de testes valendo 30 pontos, B ≤ 100 000.
    Para um conjunto de casos de testes valendo outros 70 pontos, nenhuma restrição adicional. 


'''

import math

lista_valores = []
ct = 0  
soma = 0
while ct < 2: 
  try: 
    valores = int(input('Digite um numero'))
    if valores < 1 or valores > 100000000:
      print('Numero invalido digite valores entre 1 e 100000000')
    else:     
      lista_valores.append(valores)
      ct += 1 
  except: 
    print('O entrada deve ser um numero inteiro')
for valor in range(lista_valores[0],lista_valores[1]): 
  raiz = valor**(1/2)
  cubo = valor **(1/3)
  if raiz.is_integer() and cubo.is_integer():
    soma = soma + 1 
  else: 
    continue

print(soma)
'''
Como eu fiz 

A lógica utilizada foi a seguinte: 
    Receber valores do usuário para determinar o intervalo de valores que vai ser analisado 

    Achar a raiz e o cubo dos valores desse intervalo elevando respectivamente por (1/2) e (1/3) 

    Somar 1 toda vez que um numero que possui a raiz e o cubo como inteiros (verificação feita atraves da função is_integer())

O try/except serve para garantir que a entrada do usuário esteja correta e o valor inserido seja um número. 

Os if's foram coloados para assegurar as restrições do enunciado.  
'''