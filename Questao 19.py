#Implemente uma função que receba uma lista de palavras e retorne a palavra mais longa presente na lista.

def palavra_mais_longa(lista):
    maisLonga = ''
    for palavra in lista:
        if len(palavra) > len(maisLonga):
            maisLonga = palavra
    return maisLonga

frase = input('Digite uma frase: ')
lista = frase.split()
palavra = palavra_mais_longa(lista)
print('A palavra mais longa é:', palavra)
