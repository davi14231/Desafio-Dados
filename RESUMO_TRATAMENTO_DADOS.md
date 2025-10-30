# Resumo do Tratamento de Dados - Base de Membros e Desempenho

**Analista:** Desafio 1 - Time de Gente e Gestão  
**Data:** 30 de outubro de 2025  
**Arquivo Original:** `Base_Membros_Desempenho.csv`  
**Arquivos Gerados:**
- `Base_Membros_Desempenho_Tratada.xlsx` (arquivo Excel com dados numéricos)
- `Base_Membros_Desempenho_Tratada.csv` (arquivo CSV com vírgulas decimais)
- `desafio1.py` (script Python utilizado)

---

## 📋 OBJETIVO DO DESAFIO

Padronizar e enriquecer a base de dados de performance dos membros, realizando:
1. Padronização de níveis de senioridade
2. Tratamento de avaliações técnicas e comportamentais
3. Normalização de engajamento em capacitações
4. Cálculo de score de desempenho
5. Classificação de status dos membros

---

## 🔧 ETAPAS REALIZADAS

### **1. Padronização de `Nivel_Senioridade`**

**Problema identificado:**
- Valores inconsistentes: 'Jr', 'JR', 'P', 'pleno', 'S', 'senior', 'N/D', etc.
- Valores nulos presentes na base

**Solução aplicada:**
- Criei uma função `normalize_senioridade()` que:
  - Converte todas as entradas para minúsculas e remove espaços
  - Mapeia variações para os valores padronizados: 'Júnior', 'Pleno' ou 'Sênior'
  - Trata abreviações: 'Jr', 'P', 'S', 'Sr', 'J'
  - Identifica valores inválidos: 'N/D', 'N/A', 'ND', strings vazias
  - Utiliza heurística para detectar palavras-chave ('jun', 'pleno', 'sen')

**Preenchimento de valores nulos:**
- Calculei a moda da coluna `Nivel_Senioridade`
- **Moda identificada:** Pleno
- Preenchimento: todos os valores nulos foram substituídos por 'Pleno'

**Resultado:**
- ✅ Valores únicos finais: ['Júnior', 'Pleno', 'Sênior']
- ✅ Valores nulos: 0
- ✅ Total de registros: 253

---

### **2. Padronização de `Avaliacao_Tecnica`**

**Problema identificado:**
- Valores com vírgula decimal ('7,5') e ponto decimal ('8.5')
- Valores nulos (NaN)
- Possíveis espaços e caracteres inválidos

**Solução aplicada:**
- Criei função `parse_score_field()` que:
  - Aceita tanto vírgula quanto ponto como separador decimal
  - Remove espaços em branco
  - Converte para float ou retorna NaN se inválido
  - Valida valores numéricos entre 0 e 10

**Preenchimento de valores nulos:**
- Calculei a média aritmética da coluna
- **Média calculada:** 7.86 (sem arredondamento)
- Preenchimento: todos os valores nulos foram substituídos pela média

**Resultado:**
- ✅ Valores nulos: 0
- ✅ Média final: 7.86
- ✅ Intervalo: 5.5 a 9.9
- ✅ Todas as avaliações estão no formato numérico correto

---

### **3. Padronização de `Avaliacao_Comportamental`**

**Problema identificado:**
- Mesmos problemas da Avaliacao_Tecnica
- Valores mistos com vírgula e ponto
- Valores nulos (NaN)

**Solução aplicada:**
- Mesma função `parse_score_field()` utilizada
- Conversão uniforme para formato numérico

**Preenchimento de valores nulos:**
- Calculei a média aritmética da coluna
- **Média calculada:** 7.95 (sem arredondamento)
- Preenchimento: todos os valores nulos foram substituídos pela média

**Resultado:**
- ✅ Valores nulos: 0
- ✅ Média final: 7.95
- ✅ Intervalo: 6.0 a 9.8
- ✅ Todas as avaliações estão no formato numérico correto

---

### **4. Tratamento de `Engajamento_PIGs`**

**Problema identificado:**
- Valores em formato de porcentagem textual: '90%', '75%', '80,5%'
- Valores inválidos: 'N/A', strings vazias
- Valores nulos
- Possível mistura de formatos (porcentagem e decimal)

**Solução aplicada:**
- Criei função `parse_engajamento()` que:
  - Remove o símbolo '%'
  - Converte vírgulas para pontos
  - Identifica e trata valores inválidos ('N/A', 'na', etc.)
  - Detecta automaticamente se o valor está em escala 0-100 ou 0-1
  - Converte porcentagens (0-100) para decimal (0-1)

**Preenchimento de valores nulos:**
- Calculei a média aritmética da coluna
- **Média calculada:** 0.8156 ou 81.56%
- Preenchimento: todos os valores nulos foram substituídos pela média

**Resultado:**
- ✅ Valores nulos: 0
- ✅ Média final: 81.56%
- ✅ Intervalo: 0.50 a 1.00
- ✅ Formato decimal (0-1): correto
- ✅ Todos os valores representam frações válidas

---

### **5. Cálculo de `Score_Desempenho`**

**Fórmula aplicada:**
```
Score_Desempenho = (Avaliacao_Tecnica × 0.5) + (Avaliacao_Comportamental × 0.5)
```

**Implementação:**
- Nova coluna criada com o cálculo da média ponderada 50/50
- Utilização dos valores já tratados e preenchidos

**Validação da fórmula (amostra):**
- Linha 0: (7.5×0.5 + 8.1×0.5) = 7.80 ✅
- Linha 1: (8.2×0.5 + 7.5×0.5) = 7.85 ✅
- Linha 2: (9.1×0.5 + 9.5×0.5) = 9.30 ✅

**Resultado:**
- ✅ Coluna criada com sucesso
- ✅ Valores nulos: 0
- ✅ Média do Score: 7.91
- ✅ Fórmula aplicada corretamente em todos os 253 registros

---

### **6. Criação de `Status_Membro`**

**Critério definido:**
- **"Em Destaque"**: Score_Desempenho ≥ 7.0 **E** Engajamento_PIGs ≥ 0.8
- **"Padrão"**: Caso contrário

**Implementação:**
- Utilização de operador lógico `AND` para verificação dupla
- Aplicação do critério em todos os registros

**Resultado:**
- ✅ Coluna criada com sucesso
- ✅ Valores únicos: ['Em Destaque', 'Padrão']
- ✅ **Distribuição:**
  - **Em Destaque:** 139 membros (54.9%)
  - **Padrão:** 114 membros (45.1%)
- ✅ Critério aplicado corretamente (validado por contagem)

---

## 📊 ESTATÍSTICAS FINAIS

| Métrica | Valor |
|---------|-------|
| **Total de registros** | 253 |
| **Média Avaliação Técnica** | 7.86 |
| **Média Avaliação Comportamental** | 7.95 |
| **Média Engajamento PIGs** | 81.56% |
| **Média Score Desempenho** | 7.91 |
| **Moda Nível Senioridade** | Pleno |
| **Membros "Em Destaque"** | 139 (54.9%) |
| **Membros "Padrão"** | 114 (45.1%) |

---

## 🗂️ ARQUIVOS ENTREGUES

### 1. **Base_Membros_Desempenho_Tratada.xlsx**
- Arquivo Excel com dados numéricos
- Tipos de dados preservados (float, string)
- Ideal para análises e gráficos no Excel
- Todas as colunas tratadas e enriquecidas

### 2. **Base_Membros_Desempenho_Tratada.csv**
- Arquivo CSV com codificação UTF-8 BOM
- Valores numéricos formatados com vírgula decimal (padrão brasileiro)
  - Avaliações: formato "7,5"
  - Engajamento: formato "0,82"
  - Score: formato "7,9"
- Ideal para visualização e compartilhamento

### 3. **desafio1.py**
- Script Python completo utilizado
- Código documentado e organizado
- Funções reutilizáveis para cada etapa do tratamento
- Pode ser executado novamente para reprocessar os dados

---

## 🛠️ TECNOLOGIAS UTILIZADAS

- **Python 3.11.9**
- **Pandas** (manipulação de dados)
- **NumPy** (operações numéricas)
- **openpyxl** (exportação para Excel)

---

## ✅ VALIDAÇÕES REALIZADAS

1. ✅ Todos os valores nulos foram tratados conforme especificado
2. ✅ `Nivel_Senioridade` contém apenas valores padronizados
3. ✅ `Avaliacao_Tecnica` e `Avaliacao_Comportamental` são numéricas (0-10)
4. ✅ `Engajamento_PIGs` está em formato decimal (0-1)
5. ✅ `Score_Desempenho` calculado corretamente com a fórmula especificada
6. ✅ `Status_Membro` aplicado corretamente conforme critério
7. ✅ Nenhum valor nulo remanescente na base tratada
8. ✅ Total de 253 registros preservados (sem perda de dados)

---

## 🎯 CONCLUSÃO

O tratamento de dados foi realizado com sucesso, cumprindo todos os requisitos do desafio:

- **Padronização completa** das colunas categóricas e numéricas
- **Preenchimento inteligente** de valores nulos (moda para categórica, média para numéricas)
- **Enriquecimento** da base com novas colunas calculadas (Score e Status)
- **Qualidade garantida** através de validações automáticas

A base de dados está agora pronta para análises e tomadas de decisão pelo time de Gente e Gestão, permitindo:
- Identificar membros em destaque
- Avaliar performance geral do time
- Correlacionar engajamento com desempenho
- Segmentar por nível de senioridade

---

**Ferramenta utilizada:** Python com Pandas  
**Status:** ✅ Concluído com sucesso  
**Data de conclusão:** 30/10/2025
