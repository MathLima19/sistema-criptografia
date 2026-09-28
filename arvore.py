class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir(self.raiz, novo_no)

    def _inserir(self, atual, novo_no):
        if novo_no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir(atual.esquerda, novo_no)

        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir(atual.direita, novo_no)

    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)
