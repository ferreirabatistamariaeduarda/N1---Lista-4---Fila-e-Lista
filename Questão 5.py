#Implemente uma fila circular utilizando um vetor e as operações básicas.

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho_maximo = tamanho
        self.head = None
        self.tail = None
        self.tamanho = 0

    def is_vazia(self):
        return self.head is None

    def is_cheia(self):
        return self.tamanho == self.tamanho_maximo

    def enfileirar(self, valor):
        if self.is_cheia():
            raise Exception("A fila está cheia.")
        novo_item = Item(valor)
        if self.is_vazia():
            self.head = novo_item
            self.tail = self.head
        else:
            self.tail.proximo = novo_item
            self.tail = novo_item
        self.tail.proximo = self.head 
        self.tamanho += 1

    def desenfileirar(self):
        if self.is_vazia():
            raise Exception("A fila está vazia.")
        valor = self.head.valor
        self.head = self.head.proximo
        self.tail.proximo = self.head  
        self.tamanho -= 1
        return valor

    def elemento_frente(self):
        if self.is_vazia():
            raise Exception('A fila está vazia.')
        return self.head.valor


def fila_circular():
    fila = FilaCircular(5)

    for i in range(5):
        fila.enfileirar(i)

    while not fila.is_vazia():
        proximo = None
        if fila.head.proximo is not None:
            proximo = fila.head.proximo.valor
        print(f'Removendo: {fila.desenfileirar()} Próximo: {proximo}')

    print('Valores removidos')


fila_circular()
