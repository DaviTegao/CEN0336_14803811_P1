#!/usr/bin/env python3
import sys

seq = sys.argv[1].upper() # Primeiro argumento do sys, que deve ser a sequência de DNA. O upper() aqui serve para corrigir caso a sequencia seja inserida em letras minusculas
n1 = sys.argv[2] # Segundo argumento sys, que deve ser n1
n2 = sys.argv[3] # Terceiro argumento sys, que deve ser n2
n3 = sys.argv[4] # Quarto argumento sys, que deve ser n3
n4 = sys.argv[5] # Quinto argumento sys, que deve ser n4
n5 = sys.argv[6] # Sexto argumento sys, que deve ser n5
n6 = sys.argv[7] # Setimo argumento sys, que deve ser n6

coun = int(len(seq)) # Realiza a contagem do numero de pares de bases na sequência, antes, convertendo para o formato 'int()'

if isinstance(seq, str) == True and seq.isdigit() == False: ## Verifica se o valor da sequencia é do tipo str() e se não é um numero
   seq = seq  # Se sim, nada acontece
else: # Se não, apresenta uma mensagem de erro
   print('A primeira variável deve ser a sequência de DNA, no formato de string')
   sys.exit() # Encerra o código

if n1.isdigit() == True and int(n1) < coun: # Verifica se é um numero inteiro, e se é menor que o comprimento total da sequência
   n1 = int(n1) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n1 deve ser um numero inteiro, menor que o comprimento da sequência')
   sys.exit() # Encerra o código

if n2.isdigit() == True and int(n2) < coun: # Verifica se é um numero inteiro, e se é menor que o comprimento total da sequência
   n2 = int(n2) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n2 deve ser um numero inteiro, menor que o comprimento da sequência')
   sys.exit() # Encerra o código

if n3.isdigit() == True and int(n3) < coun: # Verifica se é um numero inteiro, e se é menor que o comprimento total da sequência
   n3 = int(n3) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n3 deve ser um numero inteiro, menor que o comprimento da sequência')
   sys.exit() # Encerra o código

if n4.isdigit() == True and int(n4) < coun: # Verifica se é um numero inteiro, e se é menor que o comprimento total da sequência
   n4 = int(n4) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n4 deve ser um numero inteiro, menor que o comprimento da sequência')
   sys.exit() # Encerra o código

if n5.isdigit() == True and int(n5) < coun: # Verifica se é um numero inteiro, e se é menor que o comprimento total da sequência
   n5 = int(n5) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n5 deve ser um numero inteiro, menor que o comprimento da sequência')
   sys.exit() # Encerra o código

if n6.isdigit() == True and int(n6) <=  coun: # Verifica se é um numero inteiro, e se é menor ou igual o comprimento total da sequência
   n6 = int(n6) # Se sim, converte o numero para o formato 'int()'
else: # Se não, apresenta uma mensagem de erro
   print('n6 deve ser um numero inteiro, menor ou igual o comprimento da sequência')
   sys.exit() # Encerra o código


CDS = {} # Gera um dicionario vazio para inserir os CDSs
seql = list(seq) # Transforma seq (que antes era string) em uma lista

CDS['CDS1'] = seql[(n1-1): n2] # Separa os valores entre n1 e n2 na chave CDS1 dentro do dicionario vazio
CDS['CDS2'] = seql[(n3-1): n4] # Separa os valores entre n3 e n4 na chave CDS2 dentro do dicionario
CDS['CDS3'] = seql[(n5-1): n6] # Separa os valores entre n5 e n6 na chave CDS3 dentro do dicionario

CDS1 = list(CDS['CDS1']) # Transforma o valor da chave CDS1 do dicionario em uma lista de mesmo nome
CDS2 = list(CDS['CDS2']) # Transforma o valor da chave CDS2 do dicionario em uma lista de mesmo nome
CDS3 = list(CDS['CDS3']) # Transforma o valor da chave CDS3 do dicionario em uma lista de mesmo nome
 
if CDS1[:3] ==  ['A', 'T', 'G']: # Verifica se os três primeiros valores de CDS1 são ATG
   print('CDS 1 inicia com uma metionina (ATG), e pode ser o começo da síntese de uma proteína')
else:
   print('CDS 1 não se inicia com uma metionina (ATG), e portanto não da início a síntese de uma proteína')
   sys.exit() # Encerra o código

codpar = [['T', 'A', 'A'], ['T', 'G', 'A'], ['T', 'A', 'G']] # Cria uma lista com os códons de parada

if CDS3[-3:] in codpar: # Verifica se os ultrimos três valores de CDS3 são algum códon de parada
   print('CDS3 termina com um códon de parada, e portanto, pode codificar uma proteína')
else:
   print('CDS3 não termina com um códom de pararda. e portanto, não pode codificar uma proteína')
   sys.exit()

print('A sequência completa é:')
print(' '.join(CDS1 + CDS2 + CDS3)) # Concatena os três CDSs e transforma o resultado em uma string
