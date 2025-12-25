### FIX HOW NEW DICTIONARIES ARE SORTED
#### KEY NEEDS TO BE TEAM NAME TO PREVENT DUPLICATES
##### SEE PASS YD/GAME --> BYU AND GEORGIA HAVE SAME AVG


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
    for wins, seeds in pctg_sorted.items():
                print(f'{x}. {seeds}: {wins}% win rate')
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
        print(f'1. Total Wins')
        print(f'2. Win Percentage')
        print(f'3. Back')
        pctg_input = int(input(f'Please choose from the above options: '))

        if (pctg_input == 1):
            for wins, seeds in totalwinssorted.items():
                print(f'{x}. {seeds}: {wins} wins')
                x = x + 1
            continue
        if (pctg_input == 2):
            win_pctg_calc(teams)
            continue
        else:
            winpctg_menu = False
        
    return

def off_ppg(teams):
    ppg = {}
    x = 1

    for team in teams["teams"]:
        ppg.update({team["offppg"]: team["teamname"]})

    ppgsorted = dict(sorted(ppg.items(), reverse=True))

    for wins, seeds in ppgsorted.items():
        print(f'{x}. {seeds}: {wins} ppg')
        x = x + 1

    return

def off_yds(teams):
    total_yds = {}
    rush_yds = {}
    pass_yds = {}
    yds_menu = True
    x = 1

    while yds_menu == True:
        print(f'1. Total Yards')
        print(f'2. Rush Yards')
        print(f'3. Pass Yards')
        print(f'4. Back')
        yds_input = int(input(f'Please choose from the above options: '))

        if(yds_input == 1):
            for team in teams["teams"]:
                total_yds.update({team["offypg"]: team["teamname"]})

            totalydssorted = dict(sorted(total_yds.items(), reverse=True))

            for yards, seeds in totalydssorted.items():
                print(f'{x}. {seeds}: {yards} total yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 2):
            for team in teams["teams"]:
                rush_yds.update({team["rushydgame"]: team["teamname"]})

            rushydssorted = dict(sorted(rush_yds.items(), reverse=True))

            for yards, seeds in rushydssorted.items():
                print(f'{x}. {seeds}: {yards} rushing yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 3): #only printing 19 teams
            for team in teams["teams"]:
                pass_yds.update({team["passydgame"]: team["teamname"]})

            passydssorted = dict(sorted(pass_yds.items(), reverse=True))

            for yards, seeds in passydssorted.items():
                print(f'{x}. {seeds}: {yards} passing yards per game')
                x = x + 1

            x = 1
            continue
        else:
            yds_menu = False

    return

# def team_performance():
#     return

# def prestige_calculation():
#     return

playoff_teams_2025 = read_json()

while user_menu == True:
    print(f'1. All-time Win Percentage')
    print(f'2. Offensive Points Per Game')
    print(f'3. Offensive Yards Per Game')
    print(f'4. Defensive Points Per Game')
    print(f'5. Defensive Yards Per Game')
    print(f'6. Turnover Margin')
    print(f'7. End Program')
    user_input = int(input(f'Please choose which stat you wish to see: '))

    if (user_input == 1):
        win_pctg(playoff_teams_2025)
        continue
    if (user_input == 2):
        off_ppg(playoff_teams_2025)
        continue
    if (user_input == 3):
        off_yds(playoff_teams_2025)
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

