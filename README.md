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
Desafio-Dados/
│
├── Base_Membros_Desempenho.csv              # Base original (despadronizada)
├── Base_Membros_Desempenho_Tratada.xlsx     # Base tratada (Excel)
├── Base_Membros_Desempenho_Tratada.csv      # Base tratada (CSV)
├── desafio1.py                              # Script Python de tratamento
└── README.md                                # Este arquivo
```

## 🚀 Como Executar

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
Os arquivos tratados conterão:
- **Valores nulos tratados:** Todos preenchidos com média ou moda
- **Novas colunas criadas:** Score_Desempenho e Status_Membro
- **Membros classificados:** "Em Destaque" ou "Padrão"

### Estatísticas (exibidas ao executar o script)
- Média Avaliação Técnica
- Média Avaliação Comportamental  
- Média Engajamento PIGs
- Moda Nível Senioridade

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **openpyxl** - Exportação para Excel

## 📋 Arquivos de Entrega
1. ✅ `Base_Membros_Desempenho_Tratada.xlsx` - Base tratada (formato Excel)
2. ✅ `Base_Membros_Desempenho_Tratada.csv` - Base tratada (formato CSV)
3. ✅ `desafio1.py` - Script Python

## 📅 Data
30 de outubro de 2025
