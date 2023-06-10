#Crie uma função que receba duas listas de números e retorne uma nova lista contendo apenas os elementos que estão 
#presentes em ambas as listas.

def listas():
    lista1 = []
    lista2 = []
    lista3 = []
    
    print('Lista 1')
    
    for num in range(3):
        num = input(f'Digite o {num+1} numero: ')
        lista1.append(num)
        
    print('Lista 2')
       
    for num in range(3):
        num = input(f'Digite o {num+1} numero: ')
        lista2.append(num)
        
    lista3.append(lista1)
    lista3.append(lista2)
    print(lista3)
        

print('Digite duas listas de numeros')
listas()
