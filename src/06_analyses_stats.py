# %%
import pandas as pd
import os

# %%
# Carregar dados processados
df_laps = pd.read_csv('../reports/tables/df_laps.csv')
df_pits = pd.read_csv('../reports/tables/df_pits.csv')


# %%
# 1. Número total de voltas por piloto
total_laps_driver = df_laps.groupby('Driver').size().reset_index(name='TotalLaps')
total_laps_driver.to_csv('../reports/tables/total_laps_driver.csv', index=False)

# %%
# 2. Número total de pitstops por piloto
total_pits_driver = df_pits.groupby('Driver').size().reset_index(name='TotalPitStops')
total_pits_driver.to_csv('../reports/tables/total_pits_driver.csv', index=False)

# %%
# 3. Tempo médio de pitstop por piloto
if 'PitDuration' in df_pits.columns:
    avg_pit_driver = df_pits.groupby('Driver')['PitDuration'].mean().reset_index()
    avg_pit_driver.rename(columns={'PitDuration': 'AvgPitDurationSec'}, inplace=True)
    avg_pit_driver.to_csv('../reports/tables/avg_pit_driver.csv', index=False)
else:
    print("⚠️ Coluna 'PitDuration' não encontrada em df_pits. Pulei a média de pitstop.")

# %%
# 4. Quantidade de pneus utilizados por composto
tyre_usage = df_laps.groupby(['Compound']).size().reset_index(name='UsageCount')
tyre_usage.to_csv('../reports/tables/tyre_usage.csv', index=False)

# %%
print("✅ Tabelas de estatísticas gerais salvas em '../reports/tables/'")