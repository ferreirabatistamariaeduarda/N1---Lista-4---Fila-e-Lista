class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
    
class Lista:
    def __init__(self):
        self.cabeca = None
        self.calda = None
        self.tamanho = 0
    
    def is_empty(self):
        return self.cabeca is None

    def inserirInicio(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.cabeca = novo_item
            self.calda = novo_item
        else:
            novo_item.proximo = self.cabeca
            self.cabeca.anterior = novo_item
            self.cabeca = novo_item
        self.tamanho += 1
        
    def inserirFim(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.cabeca = novo_item
            self.calda = novo_item
        else:
            novo_item.anterior = self.calda
            self.calda.proximo = novo_item
            self.calda = novo_item
        self.tamanho += 1
        
    def removerInicio(self):
        if self.is_empty():
            print('A lista está vazia')
        elif self.cabeca.proximo is None:
            self.cabeca = None
            self.calda = None
        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
        self.tamanho -= 1
        
    def removerFim(self):
        if self.is_empty():
            print('A lista está vazia')
        elif self.cabeca.proximo is None:
            self.cabeca = None
            self.calda = None
        else:
            self.calda = self.calda.anterior
            self.calda.proximo = None
        self.tamanho -= 1
        
    def mostrar(self):
        if self.is_empty():
            print('A lista está vazia')
        else:
            atual = self.cabeca
            while atual is not None:
                print(atual.dado, end=' ')
                atual = atual.proximo
            print()
            
    def mostrarInverso(self):
        if self.is_empty():
            print('A lista está vazia')
        else:
            atual = self.calda
            while atual is not None:
                print(atual.dado, end=' ')
                atual = atual.anterior
            print()
            
def alfabetica():
    lista = Lista()

    for i in range(3):
        nome = input(f'Digite o {i+1}º nome: ')
        lista.inserirFim(nome)
        
    lista.mostrar()
    lista.mostrarInverso()
        
alfabetica()
