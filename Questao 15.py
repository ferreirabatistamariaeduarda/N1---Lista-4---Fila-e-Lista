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

    def is_empty(self):
        return self.head is None

    def is_cheia(self):
        return self.tamanho == self.tamanho_maximo

    def enfileirar(self, valor):
        if self.is_cheia():
            raise Exception("A fila está cheia.")
        novo_item = Item(valor)
        if self.is_empty():
            self.head = novo_item
            self.tail = self.head
        else:
            self.tail.proximo = novo_item
            self.tail = novo_item
        self.tail.proximo = self.head  # Ajuste para tornar a fila circular
        self.tamanho += 1

    def desenfileirar(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")
        valor = self.head.valor
        self.head = self.head.proximo
        self.tail.proximo = self.head  # Ajuste para tornar a fila circular
        self.tamanho -= 1
        return valor

    def elemento_frente(self):
        if self.is_empty():
            raise Exception('A fila está vazia.')
        return self.head.valor

    def inserir_ini(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.head = novo_item
            self.tail = self.head
            novo_item.proximo = self.head  # Ajuste para tornar a fila circular
        else:
            novo_item.proximo = self.head
            self.tail.proximo = novo_item
            self.head = novo_item
        self.tamanho += 1

    def buscar(self, valor):
        if self.is_vazia():
            return False
        atual = self.head
        for _ in range(self.tamanho):
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False


fila = FilaCircular(5)

fila.inserir_ini(4)
fila.inserir_ini(18)
fila.inserir_ini(28)
fila.inserir_ini(22)
fila.inserir_ini(13)

num_sort = int(input('Digite um número para ser sorteado: '))

if fila.buscar(num_sort):
    print('Parabéns você ganhou!')
else:
    print('Voce perdeu')
