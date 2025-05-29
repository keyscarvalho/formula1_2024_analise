#%%
import fastf1
import pandas as pd
#%%
fastf1.Cache.enable_cache('../data/cache')
#%%
gp_names = ['Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix', 
            'Japanese Grand Prix', 'Chinese Grand Prix', 'Miami Grand Prix', 
            'Emilia Romagna Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix',
            'Spanish Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 
            'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix', 
            'Italian Grand Prix', 'Azerbaijan Grand Prix', 'Singapore Grand Prix', 
            'United States Grand Prix', 'Mexican Grand Prix', 'Brazilian Grand Prix', 
            'Las Vegas Grand Prix', 'Qatar Grand Prix', 'Abu Dhabi Grand Prix']

year = 2024
#%%
for gp in gp_names:
    race = fastf1.get_session(year, gp, 'R')
    qualy = fastf1.get_session(year, gp, 'Q')
    practice = fastf1.get_session(year, gp, 'FP1')
    race.load()
    qualy.load()
    practice.load()
    
    race.laps.to_csv(f'../reports/tables/{gp}_laps.csv', index=False)
    race.results.to_csv(f'../reports/tables/{gp}_results.csv', index=False)
    laps = race.laps
    pit_stops = laps.loc[laps['PitOutTime'].notnull() | laps['PitInTime'].notnull()]
    pit_stops.to_csv(f'../reports/tables/{gp}_pit_stops.csv', index=False)
    qualy.results.to_csv(f'../reports/tables/{gp}_qualy_results.csv', index=False)
    practice.laps.to_csv(f'../reports/tables/{gp}_practice_laps.csv', index=False)
# %%
# Lista para armazenar os DataFrames
all_laps = []

for gp in gp_names:
    try:
        # Carregar sessão de corrida
        session = fastf1.get_session(2024, gp, 'R')
        session.load()

        # Obter voltas
        laps = session.laps.copy()

        # Converter LapTime para segundos
        laps['LapTimeSec'] = pd.to_timedelta(laps['LapTime']).dt.total_seconds()

        # Converter setores para segundos
        for sector in ['Sector1Time', 'Sector2Time', 'Sector3Time']:
            laps[sector + 'Sec'] = pd.to_timedelta(laps[sector]).dt.total_seconds()

        # Adicionar nome do GP
        laps['GrandPrix'] = gp

        # Selecionar colunas relevantes
        cols_to_keep = [
            'Driver', 'Driver', 'Team', 'LapNumber', 'LapTime', 'LapTimeSec',
            'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector1TimeSec',
            'Sector2Time', 'Sector2TimeSec', 'Sector3Time', 'Sector3TimeSec',
            'Compound', 'TyreLife', 'IsAccurate', 'GrandPrix'
        ]

        laps = laps[cols_to_keep]

        all_laps.append(laps)

    except Exception as e:
        print(f"Erro ao processar {gp}: {e}")

# Concatenar tudo
df_laps = pd.concat(all_laps, ignore_index=True)

# Salvar CSV
df_laps.to_csv('../reports/tables/df_laps.csv', index=False)

print("✅ df_laps.csv gerado com sucesso!")