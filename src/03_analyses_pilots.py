#%%
import pandas as pd
import numpy as np
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
points_dict = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

all_results = []
for gp in gp_names:
    results = pd.read_csv(f'../reports/tables/{gp}_results.csv')
    results['Points'] = results['Position'].map(points_dict).fillna(0)
    results['GrandPrix'] = gp
    all_results.append(results[['Abbreviation', 'TeamName', 'Position', 'Points', 'GrandPrix', 'Status']])

df_results = pd.concat(all_results)

#%%
# Pontuação acumulada por corrida
df_results['PointsAccum'] = df_results.groupby('Abbreviation')['Points'].cumsum()

# Evolução da posição no campeonato (rank por pontos acumulados)
df_results['ChampPosition'] = df_results.groupby('GrandPrix').apply(
    lambda x: x.sort_values('PointsAccum', ascending=False).reset_index(drop=True).index + 1
).reset_index(level=0, drop=True)

# Vitórias, pódios, abandonos (DNF)
wins = df_results[df_results['Position'] == 1].groupby('Abbreviation').size().rename('Wins')
podiums = df_results[df_results['Position'] <= 3].groupby('Abbreviation').size().rename('Podiums')
dnfs = df_results[~df_results['Status'].str.contains('Finished')].groupby('Abbreviation').size().rename('DNFs')

stats_pilots = pd.concat([wins, podiums, dnfs], axis=1).fillna(0).astype(int)
stats_pilots.to_csv('../reports/tables/pilot_stats.csv')

#%%
# Qualificação vs corrida (posição qualy vs corrida)
qualy_all = []
for gp in gp_names:
    qualy = pd.read_csv(f'../reports/tables/{gp}_qualy_results.csv')
    qualy['GrandPrix'] = gp
    qualy_all.append(qualy[['Abbreviation', 'GridPosition', 'GrandPrix']])
qualy_all = pd.concat(qualy_all)

qualy_race = df_results.merge(qualy_all, on=['Abbreviation', 'GrandPrix'])
qualy_race['PosDiff'] = qualy_race['Position'] - qualy_race['GridPosition']
qualy_race.to_csv('../reports/tables/qualy_vs_race.csv')

#%%
# Diferença de tempo para companheiro (tempo corrida por volta)
all_laps = []
for gp in gp_names:
    laps = pd.read_csv(f'../reports/tables/{gp}_laps.csv')
    laps['LapTimeSec'] = pd.to_timedelta(laps['LapTime']).dt.total_seconds()
    laps['GrandPrix'] = gp
    all_laps.append(laps[['Driver', 'Team', 'LapTimeSec', 'LapNumber', 'GrandPrix']])

all_laps = pd.concat(all_laps)

#%%
# Para cada piloto e corrida, calcular diferença de tempo média para companheiro
diff_times = []
for (gp, team, lap), group in all_laps.groupby(['GrandPrix', 'Team', 'LapNumber']):
    if group['Driver'].nunique() < 2:
        continue
    times = group.set_index('Driver')['LapTimeSec']
    for driver in times.index:
        others = times.drop(driver)
        diff = (times[driver] - others).mean()
        diff_times.append({'GrandPrix': gp, 'Team': team, 'Lap': lap, 'Driver': driver, 'DiffTimeToTeammate': diff})

df_diff_times = pd.DataFrame(diff_times)
df_diff_times.to_csv('../reports/tables/diff_time_teammate.csv')