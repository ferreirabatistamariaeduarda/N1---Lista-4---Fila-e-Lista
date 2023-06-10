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
        
def palindromo(palavra):
    fila = Queue()
    pvlrInver = ''
    
    if fila.is_empty():
        for i in palavra:
            fila.enqueue(i)
            
    while not fila.is_empty():
        pvlrInver += fila.dequeue()
        
    return palavra == pvlrInver    
    

palavra = input('Digite números ou palavras: ')
if palindromo(palavra):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
