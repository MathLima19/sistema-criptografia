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

    def pos_ordem(self, no, resultado=None):

        if resultado is None:
            resultado = []

        if no is not None:

            self.pos_ordem(no.esquerda, resultado)

            self.pos_ordem(no.direita, resultado)

            resultado.append(no.valor)

        return resultado
