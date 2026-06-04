# Preço Médio de Ativos

Projeto em Python para cálculo de preço médio de ativos da bolsa de valores utilizando operações de compra e venda através de arquivos CSV.

O sistema:

* Lê operações de compra e venda
* Calcula:

  * quantidade em carteira
  * custo total
  * preço médio
* Gera histórico anual dos ativos
* Preenche automaticamente anos faltantes até o ano atual
* Exporta os resultados em JSON

---

# Tecnologias utilizadas

* Python 3
* Pandas

---

# Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/renan-git/preco-medio.git
```

---

## 2. Entre na pasta do projeto

```bash
cd preco-medio
```

---

## 3. Crie a virtual environment

### Windows

```bash
py -m venv .venv
```

### Linux/macOS

```bash
python3 -m venv .venv
```

---

## 4. Ative a virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 5. Instale as dependências

```bash
pip install pandas
```

---

## 6. Execute o projeto

```bash
py main.py
```

---

# Como adicionar suas operações

Basta modificar os arquivos:

* `compras.csv`
* `vendas.csv`

com as suas operações reais.

Você pode:

* adicionar novos ativos
* remover ativos
* incluir compras
* incluir vendas
* alterar datas
* utilizar quantas operações quiser

---

# Estrutura do CSV

## compras.csv

```csv
data,ativo,quantidade,preco_unidade,taxa
2020-01-10,PETR4,10,20.00,0.00
2021-02-20,ITSA4,20,10.00,0.00
```

---

## vendas.csv

```csv
data,ativo,quantidade,preco_unidade,taxa
2021-12-10,PETR4,5,25.00,0.00
2022-07-15,ITSA4,10,11.00,0.00
```

---

# Significado das colunas

| Coluna        | Descrição            |
| ------------- | -------------------- |
| data          | Data da operação     |
| ativo         | Código do ativo      |
| quantidade    | Quantidade negociada |
| preco_unidade | Preço por ação/cota  |
| taxa          | Taxa da corretora    |

---

# Resultado gerado

O projeto gera dois arquivos:

## carteira.json

Estado atual da carteira.

Exemplo:

```json
{
    "PETR4": {
        "quantidade": 5,
        "custo_total": 100.0,
        "preco_medio": 20.0
    },
    "ITSA4": {
        "quantidade": 10,
        "custo_total": 100.0,
        "preco_medio": 10.0
    }
}
```

---

## historico.json

Histórico anual completo dos ativos.

O sistema:

* cria automaticamente anos faltantes
* replica a posição do último ano conhecido
* mantém o histórico preenchido até o ano atual

Exemplo:

```json
{
    "PETR4": {
        "2020": {
            "quantidade": 10,
            "custo_total": 200.0,
            "preco_medio": 20.0
        },
        "2021": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        },
        "2022": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        },
        "2023": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        },
        "2024": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        },
        "2025": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        },
        "2026": {
            "quantidade": 5,
            "custo_total": 100.0,
            "preco_medio": 20.0
        }
    },
    "ITSA4": {
        "2021": {
            "quantidade": 20,
            "custo_total": 200.0,
            "preco_medio": 10.0
        },
        "2022": {
            "quantidade": 10,
            "custo_total": 100.0,
            "preco_medio": 10.0
        },
        "2023": {
            "quantidade": 10,
            "custo_total": 100.0,
            "preco_medio": 10.0
        },
        "2024": {
            "quantidade": 10,
            "custo_total": 100.0,
            "preco_medio": 10.0
        },
        "2025": {
            "quantidade": 10,
            "custo_total": 100.0,
            "preco_medio": 10.0
        },
        "2026": {
            "quantidade": 10,
            "custo_total": 100.0,
            "preco_medio": 10.0
        }
    }
}
```

---

# Regras utilizadas

## Compras

* aumentam a quantidade
* aumentam o custo total
* recalculam o preço médio

---

## Vendas

* reduzem apenas a quantidade
* o preço médio permanece o mesmo
* o custo total é recalculado com:

```txt
quantidade * preco_medio
```

---

# Observações

* O sistema arredonda valores monetários para 2 casas decimais
* O histórico anual é preenchido automaticamente até o ano atual
* O projeto suporta múltiplos ativos
* Os arquivos CSV podem ser modificados livremente para representar sua carteira real

