#Escreva um programa que leia uma sequência de números inteiros 
#e insira-os em uma fila até que um número negativo seja digitado. 
#Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.


class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.head = novo_item
            self.tail = novo_item
        else:
            self.tail.proximo = novo_item
            self.tail = novo_item
        self.tamanho += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')
        valor = self.head.valor
        self.head = self.head.proximo
        if self.head is None:
            self.tail = None
        self.tamanho -= 1
        return valor

def sequencia():
    fila = Queue()

    while True:
        valor = int(input("Digite um número inteiro: "))
        if valor < 0:
            break
        else:
            fila.enqueue(valor)
            
    while not fila.is_empty():
        valor = fila.dequeue()
        print(valor)

sequencia()
