#!/usr/bin/env python

# Exercicio que checa uma palavra, retira os dois ultimos caracteres e faz a contagem de letras restantes

# Funcao checa a palavra  e retorna a qtde de caracteres exceto os 2 ultimos
def checa_palavra(palavra):
	palavra_sem_dois_ultimos_caracteres = palavra[0:-2]

  # Contar o total de letras da palavra sem os 2 ultimos caracteres
	total_de_letras = 0
	for i in palavra_sem_dois_ultimos_caracteres:
		total_de_letras = total_de_letras + 1 # resumido: total_de_letras += 1

	# Agora vamos checar o tamanho total das letras contadas e retorna a mensagem definida	
	if total_de_letras <= 10:
		return "Menor que 10! Palavra: %s" % palavra_sem_dois_ultimos_caracteres
	elif total_de_letras <= 50:
		return "Menor que 50! Palavra: %s" % palavra_sem_dois_ultimos_caracteres
	elif total_de_letras >= 100:
		return "Maior que 100! Palavra: %s" % palavra_sem_dois_ultimos_caracteres
	else:
		return "Menor que 100! Palavra: %s" % palavra_sem_dois_ultimos_caracteres

# Mensagem que obtem a palavra e joga na variavel
recebe_palavra = raw_input('Digite a palavra: ')

# Imprime o retorno da funcao
print checa_palavra(recebe_palavra)
