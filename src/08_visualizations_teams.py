#%%
# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
sns.set_theme(style="whitegrid")

df_laps = pd.read_csv('../reports/tables/df_laps.csv')
df_pits = pd.read_csv('../reports/tables/df_pits.csv')  # Se tiver esse arquivo
#%% 
# Pré-processamento - Converter setores para segundos se necessário
for sector in ['Sector1TimeSec', 'Sector2TimeSec', 'Sector3TimeSec']:
    if df_laps[sector].dtype == 'object':
        df_laps[sector + 'Sec'] = pd.to_timedelta(df_laps[sector]).dt.total_seconds()

#%% 
# 1. Comparar médias de volta por equipe em cada GP
team_gp_avg = df_laps.groupby(['GrandPrix', 'Team'])['LapTimeSec'].mean().reset_index()

plt.figure(figsize=(26, 10))
sns.barplot(data=team_gp_avg, x='GrandPrix', y='LapTimeSec', hue='Team')
plt.xticks(rotation=45)
plt.title('Média de Tempo de Volta por Equipe em cada GP - Temporada 2024')
plt.ylabel('Tempo Médio de Volta (segundos)')
plt.xlabel('Grande Prêmio')
plt.legend(title='Equipe', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../reports/figures/team_avg_lap_per_gp.png')
plt.show()

#%% 
# 2. Evolução do desempenho por equipe ao longo da temporada
plt.figure(figsize=(14, 7))
sns.lineplot(data=team_gp_avg, x='GrandPrix', y='LapTimeSec', hue='Team', marker='o')
plt.xticks(rotation=45)
plt.title('Evolução do Desempenho das Equipes na Temporada 2024')
plt.ylabel('Tempo Médio de Volta (segundos)')
plt.xlabel('Grande Prêmio')
plt.legend(title='Equipe', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../reports/figures/team_performance_trend.png')
plt.show()

#%% 
# 3. Número de pit stops por equipe em cada GP
pit_counts = df_pits.groupby(['GrandPrix', 'Team']).size().reset_index(name='NumPitStops')

plt.figure(figsize=(26, 10))
sns.barplot(data=pit_counts, x='GrandPrix', y='NumPitStops', hue='Team')
plt.xticks(rotation=45)
plt.title('Número de Pit Stops por Equipe em cada GP - Temporada 2024')
plt.ylabel('Número de Pit Stops')
plt.xlabel('Grande Prêmio')
plt.legend(title='Equipe', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../reports/figures/team_pitstops_per_gp.png')
plt.show()

#%% 
# 4. Performance de setores por equipe (boxplots)
plt.figure(figsize=(18, 6))

for i, sector in enumerate(['Sector1TimeSec', 'Sector2TimeSec', 'Sector3TimeSec'], 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x='Team', y=sector, data=df_laps)
    plt.xticks(rotation=45)
    plt.title(f'Tempo no {sector.replace("TimeSec","Setor")}')
    plt.ylabel('Tempo (segundos)')
    plt.xlabel('Equipe')

plt.suptitle('Performance de Setores por Equipe - Temporada 2024')
plt.tight_layout()

plt.savefig('../reports/figures/team_sector_performance.png')
plt.show()