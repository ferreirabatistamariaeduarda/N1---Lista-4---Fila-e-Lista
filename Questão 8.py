#Escreva um programa que leia uma lista de números inteiros e crie uma lista encadeada simples com 
#esses números em ordem inversa.


class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def is_empty(self):
        return self.cabeca is None
        
    def inserirInicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.cabeca
        self.cabeca = novo_item
        self.tamanho += 1
        
    def inserirFim(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.cabeca = novo_item
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item
        self.tamanho += 1
        
    def removerInicio(self):
        if self.is_empty():
            print('A lista está vazia!')
        elif self.cabeca.proximo is None:
            self.cabeca = None
        else:
            self.cabeca = self.cabeca.proximo
        self.tamanho -= 1

    def removerFim(self):
        if self.is_empty():
            print('A lista está vazia!')
        elif self.cabeca.proximo is None:
            self.cabeca = None
        else:
            atual = self.cabeca
            anterior = None
            while atual.proximo is not None:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None
        self.tamanho -= 1

    def mostrar(self):
        if self.is_empty():
            print('A lista está vazia!')
        else:
            atual = self.cabeca
            while atual is not None:
                print(atual.dado, end=' ')
                atual = atual.proximo
            print()

def ordemInversa():
    lista = Lista()
    
    print('Digite 5 números:')
    for _ in range(5):
        num = input('Digite um número: ')
        lista.inserirInicio(num)
        
    lista.mostrar()

ordemInversa()
