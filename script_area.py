#!/usr/bin/env python3
import sys


c1 = sys.argv[1] # Primeiro valor fornecido pelo usuario na linha de comando
c2 = sys.argv[2] # Segundo valor fornecido pelo ususario na linha de comnado

if c1.isdigit() == True: # Verifica se o valor fornecido é um numero
   c1 = int(c1); # Transforma o valor fornecido em um numero inteiro
   if c1 < 500: # Verifica se o numero é menorque 500
      c1 = c1 # Se tudo estiver certo, não faz nada
   else: # Caso o numero não for menor que 500, mostra uma mensagem de erro
      print('Erro: Os valores informados devem ser numeros interiros menores que 500')
      sys.exit() # Encerra o codigo
else: # Caso o valor fornecido não for um numero, mostra uma mensagem de erro
   print('Erro: Os valores informados devem ser numeros interiros menores que 500')
   sys.exit() # Encerra o codigo 

if c2.isdigit() == True: # Verifica se o valor fornecido é um numero
   c2 = int(c2) # Transforma o valor fornecido em um numero inteiro
   if c2 < 500: # Verifica se o numero é menorque 500
      c2 = c2 # Se tudo estiver certo, não faz nada
   else: # Caso o numero não for menor que 500, mostra uma mensagem de erro
      print('Erro: Os valores informados devem ser numeros interiros menores que 500')
      sys.exit() # Encerra o codigo 

else: # Caso o valor fornecido não for um numero, mostra uma mensagem de erro
   print('Erro: Os valores informados devem ser numeros interiros menores que 500')
   sys.exit() # Encerra o codigo 

Area = (c1*c2)/2 # Calcula a area do triangulo com base nos valores fornecidos

print('A área do trinagulo retângulo com lados a =', c1, 'e b =', c2, 'é:', Area)
