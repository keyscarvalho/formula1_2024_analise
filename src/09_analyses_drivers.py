# %%
import pandas as pd
import os

# %%
# Carregar dados processados
df_laps = pd.read_csv('../reports/tables/df_laps.csv')

# %%
# 1. Média de tempo de volta por piloto
driver_avg_lap = df_laps.groupby('Driver')['LapTimeSec'].mean().reset_index()
driver_avg_lap = driver_avg_lap.sort_values('LapTimeSec')

# Salvar tabela
driver_avg_lap.to_csv('../reports/tables/driver_avg_lap.csv', index=False)

# %%
# 2. Evolução do desempenho por piloto ao longo da temporada
driver_gp_avg = df_laps.groupby(['GrandPrix', 'Driver'])['LapTimeSec'].mean().reset_index()

# Salvar tabela
driver_gp_avg.to_csv('../reports/tables/driver_gp_avg.csv', index=False)

# %%
# 3. Consistência dos pilotos (Desvio padrão dos tempos de volta)
driver_consistency = df_laps.groupby('Driver')['LapTimeSec'].std().reset_index()
driver_consistency = driver_consistency.rename(columns={'LapTimeSec': 'LapTimeStd'})

# Salvar tabela
driver_consistency.to_csv('../reports/tables/driver_consistency.csv', index=False)

# %%
# 4. Comparação de setores por piloto (médias)
sector_cols = ['Sector1TimeSec', 'Sector2TimeSec', 'Sector3TimeSec']

driver_sector_avg = df_laps.groupby('Driver')[sector_cols].mean().reset_index()

# Salvar tabela
driver_sector_avg.to_csv('../reports/tables/driver_sector_avg.csv', index=False)

print("✅ Análises de pilotos geradas e salvas com sucesso!")