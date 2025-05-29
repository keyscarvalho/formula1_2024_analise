# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#%%
sns.set_theme(style="whitegrid")

# Carregar as tabelas geradas
driver_avg_lap = pd.read_csv('../reports/tables/driver_avg_lap.csv')
driver_gp_avg = pd.read_csv('../reports/tables/driver_gp_avg.csv')
driver_consistency = pd.read_csv('../reports/tables/driver_consistency.csv')
driver_sector_avg = pd.read_csv('../reports/tables/driver_sector_avg.csv')

# Criar diretório de figuras se não existir
os.makedirs('../reports/figures/drivers', exist_ok=True)

# %%
# 1. Gráfico de barras — média de tempo de volta por piloto
plt.figure(figsize=(12, 6))
sns.barplot(data=driver_avg_lap, x='LapTimeSec', y='Driver', palette='viridis')
plt.xlabel('Média de Tempo de Volta (s)')
plt.ylabel('Piloto')
plt.title('Média de Tempo de Volta por Piloto - Temporada 2024')
plt.tight_layout()
plt.savefig('../reports/figures/drivers/driver_avg_lap.png')
plt.close()

# %%
# 2. Linha — evolução do desempenho por piloto ao longo dos GPs
plt.figure(figsize=(14, 6))
sns.lineplot(data=driver_gp_avg, x='GrandPrix', y='LapTimeSec', hue='Driver', marker="o")
plt.xticks(rotation=45)
plt.xlabel('GP')
plt.ylabel('Média de Tempo de Volta (s)')
plt.title('Evolução do Desempenho dos Pilotos - Temporada 2024')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../reports/figures/drivers/driver_gp_evolution.png')
plt.close()

# %%
# 3. Barras horizontais — consistência (desvio padrão)
plt.figure(figsize=(12, 6))
sns.barplot(data=driver_consistency, x='LapTimeStd', y='Driver', palette='coolwarm')
plt.xlabel('Desvio Padrão dos Tempos de Volta (s)')
plt.ylabel('Piloto')
plt.title('Consistência dos Pilotos - Temporada 2024')
plt.tight_layout()
plt.savefig('../reports/figures/drivers/driver_consistency.png')
plt.close()

# %%
# 4. Barras agrupadas — comparação de setores por piloto
driver_sector_avg_melted = driver_sector_avg.melt(id_vars='Driver',
                                                  value_vars=['Sector1TimeSec', 'Sector2TimeSec', 'Sector3TimeSec'],
                                                  var_name='Setor',
                                                  value_name='Tempo Médio (s)')

plt.figure(figsize=(12, 6))
sns.barplot(data=driver_sector_avg_melted, x='Tempo Médio (s)', y='Driver', hue='Setor')
plt.xlabel('Tempo Médio (s)')
plt.ylabel('Piloto')
plt.title('Comparação dos Tempos Médios por Setor - Pilotos 2024')
plt.legend(title='Setor')
plt.tight_layout()
plt.savefig('../reports/figures/drivers/driver_sector_comparison.png')
plt.close()

print("✅ Visualizações de pilotos salvas em '../reports/figures/drivers'")
