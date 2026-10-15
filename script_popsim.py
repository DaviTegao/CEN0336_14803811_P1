#!/usr/bin/env python3
import sys

print('Preencha os valores a seguir para o cálculo do tamanho da população') # Frase guia
pi = input('Tamanho inicial da população:') # Pede a população inicial desejada para o cálculo
r = input('Taxa de crescimento anual (colocar em formato decimal):') # Pede a taxa de crescimento anual desejada
t = input('Numero de anos:') # Pede o tempo desejado

if pi.isdigit() == True: # Verifica se o numero inserido para a população inicial é um numero inteiro
   pi = int(pi) # Se sim, converte a string para esse formato
else: # Se não, apresenta uma mensagem de erro
   print('O valor para o tamanho inicial da população deve ser um numero inteiro')
   sys.exit() # Encerra o codigo

def isdecimal (valor): # Cria uma função que verifica se um numero é decimal (float)
   try:
      float(valor) # Tenta converter aquele numero para o formato 'float()'
   except ValueError: # Se der erro, resulta em 'False'
      return False 
   return True # Se não der erro, resulta em 'True'

if isdecimal(r) == True: # Verifica se o numero inserido  para a taxa de crescimento anual é um numero decimal, utilizando a função criada anteriormente
   r = float(r)  # Se sim, converte a string para float
else: # Se não, apresenta uma mensagem de erro
   print('O valor para a taxa de crescimento anual deve ser um numero decimal')
   sys.exit() # Encerra o codigo

if t.isdigit() == True: # Verifica se o numero inserido para o tempo em anos é um numero inteiro
   t = int(t) # Se sim, converte a string para int
else: # Se não, apresenta uma mensagem de erro
   print('O valor para o numero de anos deve ser um numero inteiro')
   sys.exit() # Encerra o codigo

for ano in range(1, t+1): # Gera um loop 'for' para cada ano, dentro do tempo inserido anteriormente
   pop = round(pi*((1+r)**ano)) # Calcula a formula, com os numeros inseridos anteriormente, para cada valor de t
   print(f'População no ano {ano}: {pop}') # Imprime o valores de população para cada ano
