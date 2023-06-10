#Implemente uma fila simples e as operações básicas: inserir, remover e mostrar o elemento da frente.

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
            self.tail = self.head
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
    
def filaSimples():
    fila = Queue()
    
    for i in range(5):
        fila.enqueue(i)
        
    while not fila.is_empty():
        proximo = None
        if fila.head.proximo is not None:
          proximo = fila.head.proximo.valor
        print(f'Removendo: {fila.dequeue()} Proximo: {proximo}')
        
    print('Valores removidos')

filaSimples()

        