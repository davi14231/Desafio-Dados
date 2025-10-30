import pandas as pd
import numpy as np

CSV_INPUT = 'Base_Membros_Desempenho.csv'
CSV_OUTPUT = 'Base_Membros_Desempenho_Tratada.csv'  # arquivo final com vírgula decimal (para entrega)
XLSX_OUTPUT = 'Base_Membros_Desempenho_Tratada.xlsx'  # arquivo Excel com tipos numéricos


def normalize_senioridade(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().lower()
    if s in ('jr', 'jr.', 'j', 'júnior', 'junior'):
        return 'Júnior'
    if s in ('p', 'pleno', 'pln'):
        return 'Pleno'
    if s in ('s', 'sr', 'senior', 'sênior', 'senior.'):
        return 'Sênior'
    if s in ('n/d', 'nd', 'n/a', 'na', '', 'none', 'nan'):
        return np.nan
    # fallback: try to detect keywords
    if 'jun' in s:
        return 'Júnior'
    if 'pleno' in s:
        return 'Pleno'
    if 'sen' in s:
        return 'Sênior'
    return val


def parse_score_field(x):
    # Accept '7,5' or '7.5' or numeric; return float or NaN
    if pd.isna(x):
        return np.nan
    s = str(x).strip().replace(' ', '')
    if s == '':
        return np.nan
    s = s.replace(',', '.')
    try:
        return float(s)
    except Exception:
        return np.nan


def parse_engajamento(x):
    # Accept '90%', '90,0%', 'N/A', '90', numeric
    if pd.isna(x):
        return np.nan
    s = str(x).strip().replace(' ', '')
    if s == '':
        return np.nan
    if s.lower() in ('n/a', 'na', 'nan', 'none'):
        return np.nan
    # remove percent sign and normalize comma
    s = s.replace('%', '').replace(',', '.')
    try:
        val = float(s)
    except Exception:
        return np.nan
    # if value looks like a percent (0-100), convert to fraction
    if val > 1:
        return val / 100.0
    return val


def main():
    # 1. Ler arquivo
    base = pd.read_csv(CSV_INPUT)

    # 2. Nivel_Senioridade: normalizar e preencher com moda
    if 'Nivel_Senioridade' in base.columns:
        base['Nivel_Senioridade'] = base['Nivel_Senioridade'].apply(normalize_senioridade)
        moda = base['Nivel_Senioridade'].mode()
        if not moda.empty:
            moda_val = moda.iloc[0]
            base['Nivel_Senioridade'] = base['Nivel_Senioridade'].fillna(moda_val)

    # 3. Avaliacoes: garantir floats (0-10), aceitar vírgula ou ponto
    for col in ['Avaliacao_Tecnica', 'Avaliacao_Comportamental']:
        if col in base.columns:
            base[col] = base[col].apply(parse_score_field)
            mean_val = base[col].mean()
            if np.isnan(mean_val):
                mean_val = 0.0
            else:
                mean_val = round(mean_val, 1)  # Arredondar para 1 casa decimal
            base[col] = base[col].fillna(mean_val)

    # 4. Engajamento_PIGs: converter para decimal (0-1)
    if 'Engajamento_PIGs' in base.columns:
        base['Engajamento_PIGs'] = base['Engajamento_PIGs'].apply(parse_engajamento)
        mean_eng = base['Engajamento_PIGs'].mean()
        if np.isnan(mean_eng):
            mean_eng = 0.0
        else:
            mean_eng = round(mean_eng, 2)  # Arredondar para 2 casas decimais
        base['Engajamento_PIGs'] = base['Engajamento_PIGs'].fillna(mean_eng)

    # 5. Score_Desempenho
    if all(c in base.columns for c in ('Avaliacao_Tecnica', 'Avaliacao_Comportamental')):
        base['Score_Desempenho'] = (base['Avaliacao_Tecnica'] * 0.5) + (base['Avaliacao_Comportamental'] * 0.5)
    else:
        base['Score_Desempenho'] = np.nan

    # 6. Status_Membro
    if 'Engajamento_PIGs' in base.columns:
        base['Status_Membro'] = np.where((base['Score_Desempenho'] >= 7.0) & (base['Engajamento_PIGs'] >= 0.8), 'Em Destaque', 'Padrão')
    else:
        base['Status_Membro'] = np.where(base['Score_Desempenho'] >= 7.0, 'Em Destaque', 'Padrão')

    # 7. Salvar arquivos: Excel (numérico) e CSV com vírgula decimal (visual/entrega)
    base.to_excel(XLSX_OUTPUT, index=False)

    # preparar CSV com vírgulas decimais para colunas numéricas chave
    df_csv = base.copy()
    # formatar colunas numéricas com 1 casa decimal (ex: 7,5)
    for col in ['Avaliacao_Tecnica', 'Avaliacao_Comportamental', 'Score_Desempenho']:
        if col in df_csv.columns:
            df_csv[col] = df_csv[col].map(lambda x: ('{:.1f}'.format(x)).replace('.', ',') if pd.notna(x) else '')
    # formatar Engajamento_PIGs com duas casas decimais (ex: 0,90)
    if 'Engajamento_PIGs' in df_csv.columns:
        df_csv['Engajamento_PIGs'] = df_csv['Engajamento_PIGs'].map(lambda x: ('{:.2f}'.format(x)).replace('.', ',') if pd.notna(x) else '')

    df_csv.to_csv(CSV_OUTPUT, index=False, encoding='utf-8-sig')

    # imprimir resumo rápido
    resumo = {
        'media_tecnica': float(base['Avaliacao_Tecnica'].mean()) if 'Avaliacao_Tecnica' in base.columns else None,
        'media_comportamental': float(base['Avaliacao_Comportamental'].mean()) if 'Avaliacao_Comportamental' in base.columns else None,
        'media_engajamento': float(base['Engajamento_PIGs'].mean()) if 'Engajamento_PIGs' in base.columns else None,
        'moda_senioridade': (base['Nivel_Senioridade'].mode().iloc[0]) if 'Nivel_Senioridade' in base.columns and not base['Nivel_Senioridade'].mode().empty else None,
    }

    print('Tratamento concluído! Arquivos salvos:')
    print(' -', XLSX_OUTPUT)
    print(' -', CSV_OUTPUT)
    print('\nResumo de preenchimentos e estatísticas:')
    for k, v in resumo.items():
        print(f' {k}: {v}')


if __name__ == '__main__':
    main()
