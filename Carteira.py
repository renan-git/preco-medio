import json

class Carteira:

    def __init__(self):
        self.ativos = {}

    def inicializa_ativo(self, ativo):
        self.ativos[ativo] = {
            'quantidade': 0,
            'custo_total': 0,
            'preco_medio': 0
        }
    
    def compra(self, ativo, quantidade, preco, taxa):
        custo_compra = (quantidade * preco) + taxa
        self.ativos[ativo]['custo_total'] += custo_compra
        self.ativos[ativo]['quantidade'] += quantidade
        self.ativos[ativo]['preco_medio'] = round(self.ativos[ativo]['custo_total'] / self.ativos[ativo]['quantidade'], 2)

    def venda(self, ativo, quantidade):
        self.ativos[ativo]['quantidade'] -= quantidade
        if self.ativos[ativo]['quantidade'] == 0:
            self.ativos[ativo]['custo_total'] = 0
            self.ativos[ativo]['preco_medio'] = 0
        else:
            self.ativos[ativo]['custo_total'] = self.ativos[ativo]['quantidade'] * self.ativos[ativo]['preco_medio']

    def arredondar_valores_monetarios(self):
        for ativo in self.ativos.values():
            ativo['custo_total'] = round(ativo['custo_total'], 2)
            ativo['preco_medio'] = round(ativo['preco_medio'], 2)

    def gerar_resumo(self):
        with open('carteira.json', 'w') as file:
            json.dump(self.ativos, file, indent=4)