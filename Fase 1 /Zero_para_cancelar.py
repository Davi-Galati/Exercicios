'''
ZERO PARA CANCELAR 

eu chefe está ao telefone, nervoso. Ele quer que você compute a soma de uma sequência de números que ele vai falar para você ao telefone, para saber o total das vendas em sua mais recente viagem de negócios.

Infelizmente, de vez em quando seu chefe fala números errados para você ao telefone.

Felizmente, seu chefe rapidamente percebe que falou um número errado e diz "zero", que como combinado previamente quer dizer ignore o último número corrente.

Infelizmente, seu chefe pode cometer erros repetidos, e diz "zero" para cada erro.

Por exemplo, seu chefe pode falar ao telefone "Um, três, cinco, quatro, zero, zero, sete, zero, zero, seis", o que significa uma soma total igual a 7, conforme explicado na tabela abaixo: 

Restrições

    1 ≤ N ≤ 100 000
    0 ≤ Xi ≤ 100, para (1 ≤ i ≤ N)
    0 ≤ resultado ≤ 1 000 000 
'''


val_resultado = False
val_entradas = False 
while val_entradas == False:
  try:
    entradas = int(input('Digite o numero de entradas: '))
    if entradas < 1 or entradas >100000:
      print('Entrada invalida, digite um numéro entre 1 e 100000.')
    else:
      val_entradas = True 
  except: 
    print('A entrada digitada deve ser um número inteiro.')
lista = []
print("Digite os numeros: ")
while val_resultado == False:
  for entrada in range(entradas): 
    try:
      numero = int(input('')) 
      if numero == 0: 
        lista.pop()
      else:
        lista.append(numero)
    except:
      print('O conteudo digitado deve ser um numéro inteiro.')
    
  if sum(lista) < 0 or sum(lista) >1000000:
    print('Resultado invalido, o resultado deve ser entre 0 e 1000000.')
  else: 
    val_resultado = True 
if len(lista) != 0: 
  print(f'Soma dos resultados:{sum(lista)}')
else: 
  print(f'Resultado:{0} ')


  '''

Como eu fiz 

A lógica utilizada foi a seguinte: 
    Receber valores do usuário
    Verificar se esse valor é igual a zero, se não for ele armazena numa lista que terá seus valores somados no final.
    Se for zero ele remove o ultimo valor inserido na lista e não armazena o valor 

O try/except serve para garantir que a entrada do usuário esteja correta e o valor inserido seja um número. 

Os if's foram coloados para assegurar as restrições do enunciado.  

'''