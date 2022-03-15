'''
IDADE DE CAMILA 

Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.

Entrada
A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma das irmãs.

Saída
Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila.

Restrições
5 ≤ N ≤ 100
'''

lista = []      
contador = 0    

while contador < 3: 

    try:  
        idade = int(input('Digite a idade')) 
        if idade >=5 and idade <= 100:   
            lista.append(idade) 
            contador += 1  
        else:  
            print('O numero digitado não está no intervalo permitido, digite algum valor entre 5 e 100') 
            pass 
    except: 
        print('O valor digitado não foi um numero, tente novamente.')
        pass

lista.remove(max(lista)) 
lista.remove(min(lista))

print(lista[0]) 

'''

---Como eu fiz--- 

A lógica utilizada para retornar a idade da irma do meio foi a seguinte: 
    Armazenar os 3 valores numa lista 
    Remover o maior e o menor valor da lista 

O contador e o try/except serve para garantir que a entrada do usuário esteja correta e o valor inserido seja um número. 

O if foi coloado para assegurar as restrições do enunciado.  

'''