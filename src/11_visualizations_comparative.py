# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# %%
# Carregar tabelas comparativas
avg_lap_pilot = pd.read_csv('../reports/tables/comp_avg_lap_pilot.csv')
avg_lap_team = pd.read_csv('../reports/tables/comp_avg_lap_team.csv')
pit_count_pilot = pd.read_csv('../reports/tables/comp_pit_count_pilot.csv')
pit_count_team = pd.read_csv('../reports/tables/comp_pit_count_team.csv')
tyre_pilot = pd.read_csv('../reports/tables/comp_tyre_usage_pilot.csv')
tyre_team = pd.read_csv('../reports/tables/comp_tyre_usage_team.csv')
# %%
# 1. Tempo médio de volta - Pilotos
plt.figure(figsize=(12,6))
sns.barplot(data=avg_lap_pilot.sort_values('AvgLapTimeSec'), x='AvgLapTimeSec', y='Driver', palette='viridis')
plt.title('Tempo Médio de Volta por Piloto')
plt.xlabel('Tempo Médio (s)')
plt.ylabel('Piloto')
plt.tight_layout()
plt.savefig('../reports/figures/comp_avg_lap_pilot.png')
plt.close()

# %%
# 2. Tempo médio de volta - Equipes
plt.figure(figsize=(10,6))
sns.barplot(data=avg_lap_team.sort_values('AvgLapTimeSec'), x='AvgLapTimeSec', y='Team', palette='magma')
plt.title('Tempo Médio de Volta por Equipe')
plt.xlabel('Tempo Médio (s)')
plt.ylabel('Equipe')
plt.tight_layout()
plt.savefig('../reports/figures/comp_avg_lap_team.png')
plt.close()

# %%
# 3. Pitstops - Pilotos
plt.figure(figsize=(12,6))
sns.barplot(data=pit_count_pilot.sort_values('TotalPitStops', ascending=False), x='TotalPitStops', y='Driver', palette='cubehelix')
plt.title('Total de Pitstops por Piloto')
plt.xlabel('Pitstops')
plt.ylabel('Piloto')
plt.tight_layout()
plt.savefig('../reports/figures/comp_pit_count_pilot.png')
plt.close()

# %%
# 4. Pitstops - Equipes
plt.figure(figsize=(10,6))
sns.barplot(data=pit_count_team.sort_values('TotalPitStops', ascending=False), x='TotalPitStops', y='Team', palette='coolwarm')
plt.title('Total de Pitstops por Equipe')
plt.xlabel('Pitstops')
plt.ylabel('Equipe')
plt.tight_layout()
plt.savefig('../reports/figures/comp_pit_count_team.png')
plt.close()

# %%
# 5. Uso de Compostos - Pilotos
plt.figure(figsize=(12,6))
sns.countplot(data=tyre_pilot, y='Driver', hue='Compound', palette='Set2')
plt.title('Uso de Compostos por Piloto')
plt.xlabel('Número de Voltas')
plt.ylabel('Piloto')
plt.legend(title='Composto')
plt.tight_layout()
plt.savefig('../reports/figures/comp_tyre_usage_pilot.png')
plt.close()

# %%
# 6. Uso de Compostos - Equipes
plt.figure(figsize=(10,6))
sns.countplot(data=tyre_team, y='Team', hue='Compound', palette='Set1')
plt.title('Uso de Compostos por Equipe')
plt.xlabel('Número de Voltas')
plt.ylabel('Equipe')
plt.legend(title='Composto')
plt.tight_layout()
plt.savefig('../reports/figures/comp_tyre_usage_team.png')
plt.close()

print("✅ Visualizações comparativas salvas em '../reports/figures/'")