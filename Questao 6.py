import time

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
    
    def addCliente(self, cliente):
        self.enqueue(cliente)
        
    def proxCliente(self):
        if self.is_empty():
            print('Não há clientes na fila')
        else:
            proxiCliente = self.dequeue()
            print('Atendendo cliente:', proxiCliente)
            
    def simular(self, tempo, intervalo):
        tempoInicial = time.time()
        tempoAtual = tempoInicial
        while tempoAtual - tempoInicial < tempo:
            self.proxCliente()
            time.sleep(intervalo)
            tempoAtual = time.time()
            

supermercado = Queue()

supermercado.addCliente(1)
supermercado.addCliente(2)
supermercado.addCliente(3)
supermercado.addCliente(4)
supermercado.addCliente(5)

supermercado.simular(tempo=10, intervalo=1)
