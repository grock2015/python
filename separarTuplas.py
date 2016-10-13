# -*- coding: utf-8 -*-
# Definindo as variaveis
minha_tupla = (1,0.3,"vasco")

# Funcao que checa o tipo do elemento e o adiciona a lista correta
# que é convertida em tupla ao final
def separarTuplas(tupla):

	tupla_string = []
	tupla_outros = []

	for item in tupla:
		if type(item) == str:
			tupla_string.append(item)
		else:
			tupla_outros.append(item)
	
	return tuple(tupla_outros), tuple(tupla_string)
	
print separarTuplas(minha_tupla)
