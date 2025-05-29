# %%
import pandas as pd
import os

# %%
# Carregar dados processados
df_laps = pd.read_csv('../reports/tables/df_laps.csv')
df_pits = pd.read_csv('../reports/tables/df_pits.csv')

# Criar diretório de tabelas se não existir
os.makedirs('../reports/tables', exist_ok=True)

# %%
# 1. Média de tempo de volta por corrida
race_avg_lap = df_laps.groupby('GrandPrix')['LapTimeSec'].mean().reset_index()
race_avg_lap.rename(columns={'LapTimeSec': 'AvgLapTimeSec'}, inplace=True)
race_avg_lap.to_csv('../reports/tables/race_avg_lap.csv', index=False)

# %%
# 2. Número de pitstops por corrida
race_pit_count = df_pits.groupby('GrandPrix').size().reset_index(name='PitStops')
race_pit_count.to_csv('../reports/tables/race_pit_count.csv', index=False)

# %%
# 3. Tempo médio de pitstop por corrida
if 'PitDuration' in df_pits.columns:
    race_avg_pit = df_pits.groupby('GrandPrix')['PitDuration'].mean().reset_index()
    race_avg_pit.rename(columns={'PitDuration': 'AvgPitDurationSec'}, inplace=True)
    race_avg_pit.to_csv('../reports/tables/race_avg_pit.csv', index=False)
else:
    print("⚠️ Coluna 'PitDuration' não encontrada em df_pits. Pulei a média de pitstop.")

print("✅ Tabelas de análises de corridas salvas em '../reports/tables/'")
