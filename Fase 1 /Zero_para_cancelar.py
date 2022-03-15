'''
ZERO PARA CANCELAR 
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