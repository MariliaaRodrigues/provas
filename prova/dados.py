class Jogador:
    def _init_(self, nome, idade, posicao, time):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.time = time

class Time:
    def _init_(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def remover_jogador(self, jogador):
        self.jogadores.remove(jogador)