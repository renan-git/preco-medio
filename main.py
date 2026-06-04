import pandas as pd
from Carteira import Carteira
from Historico import Historico

compras = pd.read_csv('acoes/SULA11_RDOR3/compras.csv')
vendas = pd.read_csv('acoes/SULA11_RDOR3/vendas.csv')

compras['tipo'] = 'COMPRA'
vendas['tipo'] = 'VENDA'

operacoes = pd.concat([compras, vendas])

operacoes['data'] = pd.to_datetime(operacoes['data'])
operacoes = operacoes.sort_values('data')

carteira = Carteira()
historico = Historico()

for _, operacao in operacoes.iterrows():
    ativo = operacao['ativo']
    tipo = operacao['tipo']
    ano = operacao['data'].year
    quantidade = operacao['quantidade']
    preco = operacao['preco_unidade']
    taxa = operacao['taxa']

    if ativo not in carteira.ativos:
        carteira.inicializa_ativo(ativo)

    if tipo == 'COMPRA':
        carteira.compra(ativo=ativo, quantidade=quantidade, preco=preco, taxa=taxa)

    elif tipo == 'VENDA':
        carteira.venda(ativo=ativo, quantidade=quantidade)

    historico.inicializa_historico(ano=ano, dados=carteira.ativos[ativo], ativo=ativo)

carteira.arredondar_valores_monetarios()
carteira.gerar_resumo()
historico.preencher_anos_faltantes()
historico.gerar_resumo()

print('Jsons gerados com sucesso!')
