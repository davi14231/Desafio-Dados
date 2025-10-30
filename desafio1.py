import pandas as pd

dados = pd.read_csv('Base_Membros_Desempenho.csv')

for i in range(len(dados)):
    valor = str(dados.loc[i, 'Nivel_Senioridade'])
    valor_lower = valor.lower().strip()
    
    if valor_lower == 'jr' or valor_lower == 'jr.' or valor_lower == 'j' or valor_lower == 'júnior' or valor_lower == 'junior':
        dados.loc[i, 'Nivel_Senioridade'] = 'Júnior'
    elif valor_lower == 'p' or valor_lower == 'pleno' or valor_lower == 'pln':
        dados.loc[i, 'Nivel_Senioridade'] = 'Pleno'
    elif valor_lower == 's' or valor_lower == 'sr' or valor_lower == 'senior' or valor_lower == 'sênior':
        dados.loc[i, 'Nivel_Senioridade'] = 'Sênior'

moda_senioridade = dados['Nivel_Senioridade'].mode()[0]
dados['Nivel_Senioridade'].fillna(moda_senioridade, inplace=True)

for i in range(len(dados)):
    valor = str(dados.loc[i, 'Avaliacao_Tecnica'])
    if valor != 'nan':
        valor = valor.replace(',', '.')
        dados.loc[i, 'Avaliacao_Tecnica'] = float(valor)

media_tecnica = dados['Avaliacao_Tecnica'].mean()
dados['Avaliacao_Tecnica'].fillna(media_tecnica, inplace=True)

for i in range(len(dados)):
    valor = str(dados.loc[i, 'Avaliacao_Comportamental'])
    if valor != 'nan':
        valor = valor.replace(',', '.')
        dados.loc[i, 'Avaliacao_Comportamental'] = float(valor)

media_comportamental = dados['Avaliacao_Comportamental'].mean()
dados['Avaliacao_Comportamental'].fillna(media_comportamental, inplace=True)

for i in range(len(dados)):
    valor = str(dados.loc[i, 'Engajamento_PIGs'])
    if valor != 'nan' and valor != 'N/A':
        valor = valor.replace('%', '').replace(',', '.')
        numero = float(valor)
        if numero > 1:
            numero = numero / 100
        dados.loc[i, 'Engajamento_PIGs'] = numero

media_engajamento = dados['Engajamento_PIGs'].mean()
dados['Engajamento_PIGs'].fillna(media_engajamento, inplace=True)

dados['Score_Desempenho'] = (dados['Avaliacao_Tecnica'] * 0.5) + (dados['Avaliacao_Comportamental'] * 0.5)

dados['Status_Membro'] = 'Padrão'

for i in range(len(dados)):
    if dados.loc[i, 'Score_Desempenho'] >= 7.0 and dados.loc[i, 'Engajamento_PIGs'] >= 0.8:
        dados.loc[i, 'Status_Membro'] = 'Em Destaque'

dados.to_excel('Base_Membros_Desempenho_Tratada.xlsx', index=False)

dados_csv = dados.copy()

for i in range(len(dados_csv)):
    dados_csv.loc[i, 'Avaliacao_Tecnica'] = str(round(dados_csv.loc[i, 'Avaliacao_Tecnica'], 1)).replace('.', ',')
    dados_csv.loc[i, 'Avaliacao_Comportamental'] = str(round(dados_csv.loc[i, 'Avaliacao_Comportamental'], 1)).replace('.', ',')
    dados_csv.loc[i, 'Score_Desempenho'] = str(round(dados_csv.loc[i, 'Score_Desempenho'], 1)).replace('.', ',')
    dados_csv.loc[i, 'Engajamento_PIGs'] = str(round(dados_csv.loc[i, 'Engajamento_PIGs'], 2)).replace('.', ',')

dados_csv.to_csv('Base_Membros_Desempenho_Tratada.csv', index=False, encoding='utf-8-sig')

print('Pronto! Arquivos salvos.')
print('Média Avaliacao Tecnica:', round(media_tecnica, 2))
print('Média Avaliacao Comportamental:', round(media_comportamental, 2))
print('Média Engajamento:', round(media_engajamento, 2))
print('Moda Senioridade:', moda_senioridade)

