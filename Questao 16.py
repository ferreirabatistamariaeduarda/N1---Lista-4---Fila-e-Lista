#Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.

def soma(nums):
    lista = []
    soma = 0
    for num in nums:
        lista.append(num)
        soma += num
    return soma

print('Digite uma lista de números:')
numeros = []
for i in range(5):
    num = int(input(f'Digite o {i+1}° número: '))
    numeros.append(num)
resultado = soma(numeros)
print(resultado)

    
     