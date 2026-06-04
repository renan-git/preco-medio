import pandas as pd
import time
import json

compras = pd.read_csv('compras.csv')
vendas = pd.read_csv('vendas.csv')

compras['tipo'] = 'COMPRA'
vendas['tipo'] = 'VENDA'

operacoes = pd.concat([compras, vendas])

operacoes['data'] = pd.to_datetime(operacoes['data'])
operacoes = operacoes.sort_values('data')

carteira = {}
historico = {}

for _, operacao in operacoes.iterrows():
    ativo = operacao['ativo']
    tipo = operacao['tipo']
    ano = operacao['data'].year
    quantidade = operacao['quantidade']
    preco = operacao['preco_unidade']
    taxa = operacao['taxa']
    if ativo not in carteira:
        carteira[ativo] = {
            'quantidade': 0,
            'custo_total': 0,
            'preco_medio': 0
        }
    dados = carteira[ativo]
    if tipo == 'COMPRA':
        custo_compra = (quantidade * preco) + taxa
        dados['custo_total'] += custo_compra
        dados['quantidade'] += quantidade
        dados['preco_medio'] = round(dados['custo_total'] / dados['quantidade'], 2)
    if tipo == 'VENDA':
        dados['quantidade'] -= quantidade
        if dados['quantidade'] == 0:
            dados['custo_total'] = 0
            dados['preco_medio'] = 0
        else:
            dados['custo_total'] = dados['quantidade'] * dados['preco_medio']
    if ativo not in historico:
        historico[ativo] = {}
    historico[ativo][ano] = {
        'quantidade': dados['quantidade'],
        'custo_total': dados['custo_total'],
        'preco_medio': dados['preco_medio']
    }


for ativo in carteira.values():
    ativo['custo_total'] = round(ativo['custo_total'], 2)
    ativo['preco_medio'] = round(ativo['preco_medio'], 2)

anos_operacoes = []
for ativo, anos in historico.items():
    for ano, dados in anos.items():
        anos_operacoes.append(ano)
        dados['custo_total'] = round(dados['custo_total'], 2)
        dados['preco_medio'] = round(dados['preco_medio'], 2)
    for ano in range(anos_operacoes[0], time.localtime().tm_year+1):
        if ano in historico[ativo]:
            continue
        else:
            historico[ativo][ano] = historico[ativo][ano-1]
    historico[ativo] = dict(sorted(historico[ativo].items()))

with open('carteira.json', 'w') as file:
    json.dump(carteira, file, indent=4)
print(carteira)

with open('historico.json', 'w') as file:
    json.dump(historico, file, indent=4)
print(historico)