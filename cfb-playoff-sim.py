import json
user_menu = True

def read_json():
    with open('2025-teams.json') as f:
        d = json.load(f)
        # print(d)
    return d
    
def win_pctg(teams):
    totalwins = []
    for team in teams["teams"]:
        # print(f'{team["teamname"]}: {team["alltimewins"]}')
        print('Placeholder')
    return

# def team_performance():
#     return

# def prestige_calculation():
#     return

playoff_teams = read_json()

while user_menu == True:
    print(f'1. All-time win percentage')
    print(f'2. Offensive Points Per Game')
    print(f'3. Offensive Yards Per Game')
    print(f'4. Defensive Points Per Game')
    print(f'5. Defensive Yards Per Game')
    print(f'6. Turnover margin')
    print(f'7. End program')
    user_input = int(input(f'Please choose which stat you wish to see: '))

    if (user_input == 1):
        win_pctg(playoff_teams)
    if (user_input == 2):
        break
    if (user_input == 3):
        break
    if (user_input == 4):
        break
    if (user_input == 5):
        break
    if (user_input == 6):
        break
    if (user_input == 7):
        user_menu = False
    
    user_menu = False

#TO-DO - READ JSON AND SORT TEAMS BY STATISTIC
#TO-DO - FACTOR HOME/AWAY STATS (?)
#TO-DO - PRESTIGE CALC - APPEND TO END OF JSON
#TO-DO - PERFORMANCE EQUATION
#STATS WEBSITE: https://www.teamrankings.com/ncf/stats/

