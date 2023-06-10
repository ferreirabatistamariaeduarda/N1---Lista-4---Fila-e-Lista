#Implemente uma função que receba uma lista de strings e retorne uma nova lista contendo 
#apenas as strings que possuem mais de 5 caracteres.


def strings(frase):
    palavras = frase.split()
    lista = []
    for palavra in palavras:
        if len(palavra) > 5:
            lista.append(palavra)
    return lista

frase = input('Digite uma frase: ')
resultado = strings(frase)
print(resultado)

