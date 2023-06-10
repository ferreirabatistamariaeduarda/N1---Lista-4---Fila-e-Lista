#Escreva um programa que leia uma lista de números inteiros e crie uma lista encadeada circular com esses 
#números em ordem crescente. Sua classe lista deve conter métodos/funções para mostrar o primeiro e ultimo elemento da lista. 

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def adicionar_elemento(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.head = novo_item
            self.tail = self.head
            self.tail.proximo = self.head  
        else:
            atual = self.head
            while atual.proximo != self.head:
                if valor < atual.proximo.valor:
                    break
                atual = atual.proximo
            novo_item.proximo = atual.proximo
            atual.proximo = novo_item
            if valor > self.tail.valor:
                self.tail = novo_item

    def primeiro_elemento(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        return self.head.valor

    def ultimo_elemento(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        return self.tail.valor


def criar_lista_encadeada():
    lista = ListaCircular()
    numeros = input("Digite a lista de números inteiros separados por espaço: ").split()

    for num in numeros:
        lista.adicionar_elemento(int(num))

    return lista


lista_encadeada = criar_lista_encadeada()
print("Primeiro elemento:", lista_encadeada.primeiro_elemento())
print("Último elemento:", lista_encadeada.ultimo_elemento())
