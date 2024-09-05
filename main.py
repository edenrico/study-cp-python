class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def aniversario(self):
        self.idade += 1
        self.pab()  # Chama o método para imprimir a mensagem de parabéns
        return self.idade
    
    def pab(self):
        print(f"Parabéns, {self.nome}! Sua idade aumentou para {self.idade}. Parabéns!")




        
        
        