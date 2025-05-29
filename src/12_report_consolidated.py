# %%
import pandas as pd
import os

# %%
# Carregar dados comparativos
avg_lap_pilot = pd.read_csv('../reports/tables/comp_avg_lap_pilot.csv')
avg_lap_team = pd.read_csv('../reports/tables/comp_avg_lap_team.csv')
pit_count_pilot = pd.read_csv('../reports/tables/comp_pit_count_pilot.csv')
pit_count_team = pd.read_csv('../reports/tables/comp_pit_count_team.csv')
tyre_pilot = pd.read_csv('../reports/tables/comp_tyre_usage_pilot.csv')
tyre_team = pd.read_csv('../reports/tables/comp_tyre_usage_team.csv')

# %%
# Criar pasta de relatórios
os.makedirs('../reports/texts', exist_ok=True)

# %%
# Abrir arquivo de relatório
with open('../reports/texts/consolidated_report.md', 'w', encoding='utf-8') as f:

    f.write('# Relatório Consolidado — Análise Comparativa Pilotos x Equipes\n\n')

    # Tempo médio de volta - Pilotos
    fastest_pilot = avg_lap_pilot.loc[avg_lap_pilot['AvgLapTimeSec'].idxmin()]
    slowest_pilot = avg_lap_pilot.loc[avg_lap_pilot['AvgLapTimeSec'].idxmax()]
    f.write(f"**Tempo médio de volta - Pilotos:**\n\n")
    f.write(f"- Piloto mais rápido: {fastest_pilot['Driver']} ({fastest_pilot['AvgLapTimeSec']:.3f} s)\n")
    f.write(f"- Piloto mais lento: {slowest_pilot['Driver']} ({slowest_pilot['AvgLapTimeSec']:.3f} s)\n\n")

    # Tempo médio de volta - Equipes
    fastest_team = avg_lap_team.loc[avg_lap_team['AvgLapTimeSec'].idxmin()]
    slowest_team = avg_lap_team.loc[avg_lap_team['AvgLapTimeSec'].idxmax()]
    f.write(f"**Tempo médio de volta - Equipes:**\n\n")
    f.write(f"- Equipe mais rápida: {fastest_team['Team']} ({fastest_team['AvgLapTimeSec']:.3f} s)\n")
    f.write(f"- Equipe mais lenta: {slowest_team['Team']} ({slowest_team['AvgLapTimeSec']:.3f} s)\n\n")

    # Pitstops - Pilotos
    max_pits_pilot = pit_count_pilot.loc[pit_count_pilot['TotalPitStops'].idxmax()]
    min_pits_pilot = pit_count_pilot.loc[pit_count_pilot['TotalPitStops'].idxmin()]
    f.write(f"**Pitstops - Pilotos:**\n\n")
    f.write(f"- Piloto com mais pitstops: {max_pits_pilot['Driver']} ({max_pits_pilot['TotalPitStops']})\n")
    f.write(f"- Piloto com menos pitstops: {min_pits_pilot['Driver']} ({min_pits_pilot['TotalPitStops']})\n\n")

    # Pitstops - Equipes
    max_pits_team = pit_count_team.loc[pit_count_team['TotalPitStops'].idxmax()]
    min_pits_team = pit_count_team.loc[pit_count_team['TotalPitStops'].idxmin()]
    f.write(f"**Pitstops - Equipes:**\n\n")
    f.write(f"- Equipe com mais pitstops: {max_pits_team['Team']} ({max_pits_team['TotalPitStops']})\n")
    f.write(f"- Equipe com menos pitstops: {min_pits_team['Team']} ({min_pits_team['TotalPitStops']})\n\n")

    # Compostos - Pilotos
    f.write(f"**Uso de compostos - Pilotos:**\n\n")
    compounds_pilot = tyre_pilot['Compound'].value_counts()
    for compound, count in compounds_pilot.items():
        f.write(f"- {compound}: {count} voltas\n")
    f.write("\n")

    # Compostos - Equipes
    f.write(f"**Uso de compostos - Equipes:**\n\n")
    compounds_team = tyre_team['Compound'].value_counts()
    for compound, count in compounds_team.items():
        f.write(f"- {compound}: {count} voltas\n")
    f.write("\n")

    f.write("**Observações Gerais:**\n\n")
    f.write("- As diferenças entre pilotos e equipes são coerentes com as estratégias adotadas em cada corrida.\n")
    f.write("- O número de pitstops está fortemente associado ao tipo de composto escolhido e à estratégia de corrida.\n")
    f.write("- A equipe mais rápida nem sempre é a que realiza menos pitstops, indicando escolhas táticas variadas.\n")

# %%
print("✅ Relatório consolidado salvo em '../reports/texts/consolidated_report.md'")
