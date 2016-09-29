#!/usr/bin/env python

# Exercicio que checa uma palavra
# retira os dois ultimos caracteres 
# e retorna a mensagem definida

# Funcao checa a palavra  e retorna a qtde de caracteres exceto os 2 ultimos
def checa_palavra(palavra):
	palavra_sem_dois_ultimos_caracteres = palavra[0:-2]

  	# Contar a quantidade de letras e armazena o resultado
	total_de_letras = 0
	for i in palavra_sem_dois_ultimos_caracteres:
		total_de_letras += 1

	# Retorna a mensagem de acordo com o total de letras
	if total_de_letras <= 10:
		return "Menor que 10!"
	elif total_de_letras <= 50:
		return "Menor que 50!"
	elif total_de_letras >= 100:
		return "Maior que 100!"
	else:
		return "Menor que 100!"

# Obtem a palavra e armazena
recebe_palavra = raw_input('Digite a palavra: ')

# Resultado
print checa_palavra(recebe_palavra)
