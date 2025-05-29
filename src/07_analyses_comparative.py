# %%
import pandas as pd
import os

# %%
# Carregar dados processados
df_laps = pd.read_csv('../reports/tables/df_laps.csv')
df_pits = pd.read_csv('../reports/tables/df_pits.csv')
# %%
# 1. Comparar médias de tempo de volta: pilotos x equipes
avg_lap_pilot = df_laps.groupby('Driver')['LapTimeSec'].mean().reset_index()
avg_lap_team = df_laps.groupby('Team')['LapTimeSec'].mean().reset_index()

avg_lap_pilot.rename(columns={'LapTimeSec': 'AvgLapTimeSec'}, inplace=True)
avg_lap_team.rename(columns={'LapTimeSec': 'AvgLapTimeSec'}, inplace=True)

avg_lap_pilot.to_csv('../reports/tables/comp_avg_lap_pilot.csv', index=False)
avg_lap_team.to_csv('../reports/tables/comp_avg_lap_team.csv', index=False)

# %%
# 2. Comparar número de pitstops: pilotos x equipes
pit_count_pilot = df_pits.groupby('Driver').size().reset_index(name='TotalPitStops')
pit_count_team = df_pits.groupby('Team').size().reset_index(name='TotalPitStops')

pit_count_pilot.to_csv('../reports/tables/comp_pit_count_pilot.csv', index=False)
pit_count_team.to_csv('../reports/tables/comp_pit_count_team.csv', index=False)

# %%
# 3. Comparar uso de compostos: pilotos x equipes
tyre_pilot = df_laps.groupby(['Driver', 'Compound']).size().reset_index(name='UsageCount')
tyre_team = df_laps.groupby(['Team', 'Compound']).size().reset_index(name='UsageCount')

tyre_pilot.to_csv('../reports/tables/comp_tyre_usage_pilot.csv', index=False)
tyre_team.to_csv('../reports/tables/comp_tyre_usage_team.csv', index=False)

print("✅ Tabelas de comparativos (pilotos x equipes) salvas em '../reports/tables/'")