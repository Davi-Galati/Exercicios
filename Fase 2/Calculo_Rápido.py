'''
Cálculo rápido

Algumas pessoas conseguem fazer cálculos matemáticos com uma velocidade impressionante. Laurinha tem essa habilidade! Um cálculo que ela consegue fazer muito rapidamente é, dados três números inteiros S, A, e B, determinar quantos números do intervalo [A, B] têm a soma de seus dígitos igual a S.

Por exemplo, se S = 3, A = 10 e B = 30, então a reposta é 3, pois existem três números no intervalo [10,30] cuja soma dos dígitos é igual a três: 12, 21 e 30.

Sua tarefa é escrever um programa de computador para, dados os três números, tentar calcular a resposta mais rapidamente do que Laurinha consegue.

Restrições

    1 ≤ S ≤ 36
    1 ≤ A ≤ 10 000
    1 ≤ B ≤ 10 000
    A ≤ B 
'''
contador = 0
entradas = []
while True:
  try: 
    numero = int(input('Digite um numero:'))
    if numero < 1 or numero > 36: 
      print('Digite um valor entre 1 e 36')
      continue
    else: 
      entradas.append(numero)
    break
  except: 
    print('A entrada digitada deve ser um valor inteiro')
    continue

while True: 
  if len(entradas)==3:
    break
  else:
    try: 
      numero = int(input('Digite um numero:'))
      if numero < 1 or numero > 10000: 
        print('Digite um valor entre 1 e 10000')
        continue
      else: 
        entradas.append(numero)
    except: 
      print('A entrada digitada deve ser um valor inteiro')
    continue
for valor in range(entradas[1],entradas[2]+1):
  valor = str(valor)
  valor = list(valor)
  new_lista=[int(num) for num in valor]
  if sum(new_lista) == entradas[0]:
    contador += 1 
  else: 
    continue 

print(contador)

'''

Como eu fiz :) 

A lógica utilizada foi a seguinte: 
    Receber 3 valores do usuário 
    Definir o primeiro valor como condição 
    Verificar numero por numero do intervalo entre o index 1 e o index 2 da lista
    Somar os digitos de cada numero verificado e comparar com o index 0 da lista, se for ele aumenta a contagem em 1 do contador
    No final retorna a quantidade de valores que atingiram a condição desejada
O contador e o try/except serve para garantir que a entrada do usuário esteja correta e o valor inserido seja um número. 

Os if's foram coloados para assegurar as restrições do enunciado.  

'''