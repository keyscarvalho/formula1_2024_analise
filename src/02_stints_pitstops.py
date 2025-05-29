#%%
import pandas as pd
import fastf1
import numpy as np
import os

#%%
gp_names = ['Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix', 
            'Japanese Grand Prix', 'Chinese Grand Prix', 'Miami Grand Prix', 
            'Emilia Romagna Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix',
            'Spanish Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 
            'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix', 
            'Italian Grand Prix', 'Azerbaijan Grand Prix', 'Singapore Grand Prix', 
            'United States Grand Prix', 'Mexican Grand Prix', 'Brazilian Grand Prix', 
            'Las Vegas Grand Prix', 'Qatar Grand Prix', 'Abu Dhabi Grand Prix']

#%%
# Exemplo para stints: identificar troca de pneus por piloto
for gp in gp_names:
    laps = pd.read_csv(f'../reports/tables/{gp}_laps.csv')
    laps['TyreCompoundChange'] = laps.groupby('Driver')['Compound'].shift() != laps['Compound']
    stints = laps[laps['TyreCompoundChange'] | laps['LapNumber'] == 1]
    stints.to_csv(f'../reports/tables/{gp}_stints.csv', index=False)
    
    pit_stops = pd.read_csv(f'../reports/tables/{gp}_pit_stops.csv')
    pit_stops.to_csv(f'../reports/tables/{gp}_pit_stops_clean.csv', index=False)
# %%
all_pitstops = []

for gp in gp_names:
    try:
        session = fastf1.get_session(2024, gp, 'R')
        session.load()

        pit_data = session.laps[session.laps['PitInTime'].notnull()].copy()

        pit_data['GrandPrix'] = gp  # Adiciona GP

        cols_to_keep = ['Driver', 'Team', 'LapNumber', 'PitInTime', 'PitOutTime', 
                        'Compound', 'TyreLife', 'Stint', 'GrandPrix']

        pit_data = pit_data[cols_to_keep]

        all_pitstops.append(pit_data)
        print(f"✅ Pit stops coletados para {gp}")

    except Exception as e:
        print(f"❌ Erro ao processar {gp}: {e}")

# Concatenar todos os pit stops
df_pits = pd.concat(all_pitstops, ignore_index=True)

# Criar pasta
os.makedirs('../reports/tables/', exist_ok=True)

# Salvar CSV
df_pits.to_csv('../reports/tables/df_pits.csv', index=False)

print("✅ df_pits.csv gerado com sucesso!")
# %%
# Supondo que você já tenha 'all_pitstops' como lista de DataFrames por corrida
df_pits = pd.concat(all_pitstops)

# Adiciona a coluna GrandPrix se ainda não tiver
if 'GrandPrix' not in df_pits.columns:
    df_pits['GrandPrix'] = df_pits['EventName']  # ou ajuste conforme seu campo

# Mantém apenas colunas úteis
cols_to_keep = ['Driver', 'Team', 'LapNumber', 'PitInTime', 'PitOutTime', 
                'Compound', 'TyreLife', 'Stint', 'GrandPrix']

df_pits = df_pits[cols_to_keep]

# Salva o CSV
df_pits.to_csv('../reports/tables/df_pits.csv', index=False)

print("✅ df_pits.csv salvo com sucesso!")