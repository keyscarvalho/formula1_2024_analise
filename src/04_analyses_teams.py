#%%
import pandas as pd

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
# Diretório das tabelas
TABLES_DIR = '../reports/tables'

#%%
# ➡️ 1. Cálculo de pontos por equipe

all_results = []

for gp in gp_names:
    df = pd.read_csv(f'{TABLES_DIR}/{gp}_results.csv')
    df['GrandPrix'] = gp
    all_results.append(df[['TeamName', 'Points', 'GrandPrix']])

df_results = pd.concat(all_results)

team_points = df_results.groupby('TeamName')['Points'].sum().reset_index()
team_points = team_points.sort_values(by='Points', ascending=False)

team_points.to_csv(f'{TABLES_DIR}/team_points.csv', index=False)
print("✅ Pontos por equipe salvos.")

#%%
# ➡️ 2. Cálculo da posição média por equipe

all_positions = []

for gp in gp_names:
    df = pd.read_csv(f'{TABLES_DIR}/{gp}_results.csv')
    df['GrandPrix'] = gp
    all_positions.append(df[['TeamName', 'Position', 'GrandPrix']])

df_positions = pd.concat(all_positions)

#%%
# Removendo posições nulas ou não classificadas
df_positions = df_positions[df_positions['Position'].notnull()]
df_positions['Position'] = pd.to_numeric(df_positions['Position'], errors='coerce')

team_avg_position = df_positions.groupby('TeamName')['Position'].mean().reset_index()
team_avg_position = team_avg_position.sort_values(by='Position')

team_avg_position.rename(columns={'Position': 'AvgPosition'}, inplace=True)
team_avg_position.to_csv(f'{TABLES_DIR}/team_avg_position.csv', index=False)
print("✅ Posição média por equipe salva.")

#%%
# ➡️ 3. Tempos médios de volta por piloto e equipe

all_laps = []

for gp in gp_names:
    df = pd.read_csv(f'{TABLES_DIR}/{gp}_laps.csv')
    df['LapTimeSec'] = pd.to_timedelta(df['LapTime']).dt.total_seconds()
    df['GrandPrix'] = gp
    all_laps.append(df[['Driver', 'Team', 'LapTimeSec', 'GrandPrix']])

df_laps = pd.concat(all_laps)
df_laps.to_csv('../reports/tables/df_laps.csv', index=False)

team_driver_avg_lap = df_laps.groupby(['Team', 'Driver'])['LapTimeSec'].mean().reset_index()
team_driver_avg_lap.to_csv(f'{TABLES_DIR}/team_driver_avg_lap.csv', index=False)
print("✅ Tempos médios de volta por piloto e equipe salvos.")

#%%
# ➡️ 4. Tempo médio de pitstop por equipe (se os dados estiverem disponíveis)

import os

pitstop_files = [f for f in os.listdir(TABLES_DIR) if f.endswith('_pitstops.csv')]

#%%
all_pitstops = []

for file in pitstop_files:
    df = pd.read_csv(os.path.join(TABLES_DIR, file))
    df['GrandPrix'] = file.replace('_pitstops.csv', '')
    all_pitstops.append(df[['Team', 'PitStopTime', 'GrandPrix']])

if all_pitstops:
    df_pitstops = pd.concat(all_pitstops)
    df_pitstops['PitStopTime'] = pd.to_numeric(df_pitstops['PitStopTime'], errors='coerce')
    
    team_avg_pit = df_pitstops.groupby('Team')['PitStopTime'].mean().reset_index()
    team_avg_pit.rename(columns={'PitStopTime': 'AvgPitStop'}, inplace=True)
    team_avg_pit = team_avg_pit.sort_values(by='AvgPitStop')

    team_avg_pit.to_csv(f'{TABLES_DIR}/team_avg_pitstop.csv', index=False)
    print("✅ Tempo médio de pitstop por equipe salvo.")
else:
    print("⚠️ Nenhum arquivo de pitstop encontrado, análise de pitstop não realizada.")