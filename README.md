# Desafio 1 - Tratamento de Dados de Membros e Desempenho

## 📌 Sobre o Projeto

Este projeto faz parte do **Desafio 1** do time de Gente e Gestão, onde realizei o tratamento e padronização de uma base de dados sobre performance dos membros da organização.

## 🎯 Objetivo

Analisar, padronizar e enriquecer a base de dados `Base_Membros_Desempenho.csv`, realizando:
- Padronização de dados categóricos e numéricos
- Tratamento de valores nulos
- Cálculo de métricas de desempenho
- Classificação de status dos membros

## 📂 Estrutura do Projeto

```
Desafio1_Dados/
│
├── Base_Membros_Desempenho.csv              # Base original (despadronizada)
├── Base_Membros_Desempenho_Tratada.xlsx     # Base tratada (Excel)
├── Base_Membros_Desempenho_Tratada.csv      # Base tratada (CSV com vírgula decimal)
├── desafio1.py                              # Script Python de tratamento
├── RESUMO_TRATAMENTO_DADOS.md               # Documento de entrega com passo a passo
└── README.md                                # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11 ou superior
- Bibliotecas: pandas, openpyxl

### Instalação

1. Clone ou baixe este repositório

2. Crie um ambiente virtual (opcional, mas recomendado):
```powershell
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:
```powershell
pip install pandas openpyxl
```

### Execução

Execute o script de tratamento:
```powershell
python desafio1.py
```

O script irá:
1. Ler o arquivo `Base_Membros_Desempenho.csv`
2. Aplicar todas as transformações
3. Gerar os arquivos tratados (`.xlsx` e `.csv`)
4. Exibir um resumo das estatísticas

## 📊 Transformações Realizadas

### 1. Nivel_Senioridade
- Padronização para: 'Júnior', 'Pleno', 'Sênior'
- Preenchimento de nulos com a moda

### 2. Avaliacao_Tecnica e Avaliacao_Comportamental
- Conversão para valores numéricos (0-10)
- Aceitação de vírgula ou ponto decimal
- Preenchimento de nulos com a média aritmética

### 3. Engajamento_PIGs
- Conversão de porcentagem para decimal (ex: '90%' → 0.9)
- Tratamento de valores 'N/A'
- Preenchimento de nulos com a média aritmética

### 4. Score_Desempenho (nova coluna)
- Fórmula: `(Avaliacao_Tecnica × 0.5) + (Avaliacao_Comportamental × 0.5)`

### 5. Status_Membro (nova coluna)
- 'Em Destaque': Score ≥ 7.0 E Engajamento ≥ 0.8
- 'Padrão': demais casos

## 📈 Resultados

- **Total de registros:** 253
- **Valores nulos após tratamento:** 0
- **Membros "Em Destaque":** 139 (54.9%)
- **Membros "Padrão":** 114 (45.1%)

### Estatísticas
- Média Avaliação Técnica: 7.86
- Média Avaliação Comportamental: 7.95
- Média Engajamento: 81.56%
- Média Score Desempenho: 7.91

## 📝 Documentação

Para entender o passo a passo detalhado de cada transformação realizada, consulte:
- **[RESUMO_TRATAMENTO_DADOS.md](RESUMO_TRATAMENTO_DADOS.md)** - Documento completo com todas as etapas, validações e estatísticas

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.9**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Operações numéricas
- **openpyxl** - Exportação para Excel

## 📋 Arquivos de Entrega

1. ✅ `Base_Membros_Desempenho_Tratada.xlsx` - Base tratada (formato Excel)
2. ✅ `Base_Membros_Desempenho_Tratada.csv` - Base tratada (formato CSV)
3. ✅ `desafio1.py` - Script Python
4. ✅ `RESUMO_TRATAMENTO_DADOS.md` - Documentação detalhada

## 👤 Autor

Desafio realizado para o time de Gente e Gestão

## 📅 Data

30 de outubro de 2025
