import json
import time

class Historico:

    def __init__(self):
        self.anos = {}

    def inicializa_historico(self, ano, dados, ativo):
        if ativo not in self.anos:
            self.anos[ativo] = {}

        self.anos[ativo][ano] = {
            'quantidade': dados['quantidade'],
            'custo_total': dados['custo_total'],
            'preco_medio': dados['preco_medio']
        }

    def preencher_anos_faltantes(self):
        for ativo, anos in self.anos.items():
            anos_ordenados = sorted(anos.keys())
            for i in range(len(anos_ordenados) - 1):
                ano_atual = anos_ordenados[i]
                proximo_ano = anos_ordenados[i + 1]
                
                if proximo_ano - ano_atual > 1:
                    for ano_faltante in range(ano_atual + 1,proximo_ano):
                        self.anos[ativo][ano_faltante] = (self.anos[ativo][ano_atual].copy())

            ultimo_ano = max(self.anos[ativo].keys())
            ano_atual = time.gmtime().tm_year

            for ano in range(ultimo_ano + 1, ano_atual + 1):
                self.anos[ativo][ano] = (self.anos[ativo][ultimo_ano].copy())
                ultimo_ano = ano

            self.anos[ativo] = dict(sorted(self.anos[ativo].items()))

    def gerar_resumo(self):
        with open('historico.json', 'w') as file:
            json.dump(self.anos, file, indent=4)