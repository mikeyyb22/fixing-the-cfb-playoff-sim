import json
import decimal
user_menu = True

def read_json():
    with open('2025-teams.json') as f:
        d = json.load(f)
        # print(d)
    return d

def win_pctg_calc(teams):
    winpctg = {}
    wins = 0
    games = 0
    pctg = 0.0
    x = 1
    for team in teams["teams"]:
        wins = int(team["alltimewins"])
        games = int(team["alltimegames"])
        pctg = str(round((wins / games), 3) * 100)
        round_help = decimal.Decimal("0.1")
        pctg = decimal.Decimal(pctg)

        rounded_pctg = pctg.quantize(round_help, rounding=decimal.ROUND_HALF_UP)

        winpctg.update({rounded_pctg: team["teamname"]})
    
    pctg_sorted = dict(sorted(winpctg.items(), reverse=True))
    for wins, teams in pctg_sorted.items():
                print(f'{x}. {teams}: {wins}% win rate')
                x = x + 1

    return
    
def win_pctg(teams):
    totalwins = {}
    winpctg_menu = True
    x = 1
    
    for team in teams["teams"]:
        totalwins.update({team["alltimewins"]: team["teamname"]})
    totalwinssorted = dict(sorted(totalwins.items(), reverse=True))

    while winpctg_menu == True:
        print(f'1. Total wins')
        print(f'2. Win percentage')
        print(f'3. Back')
        pctg_input = int(input(f'Please choose from the above options: '))

        if (pctg_input == 1):
            for wins, teams in totalwinssorted.items():
                print(f'{x}. {teams}: {wins} wins')
                x = x + 1
            continue
        if (pctg_input == 2):
            win_pctg_calc(teams)
            continue
        else:
            winpctg_menu = False
        
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
        continue
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
    else:
        user_menu = False
    

#TO-DO - READ JSON AND SORT TEAMS BY STATISTIC
#TO-DO - FACTOR HOME/AWAY STATS (?)
#TO-DO - PRESTIGE CALC - APPEND TO END OF JSON
#TO-DO - PERFORMANCE EQUATION
#STATS WEBSITE: https://www.teamrankings.com/ncf/stats/

