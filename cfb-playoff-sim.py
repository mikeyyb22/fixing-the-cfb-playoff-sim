## SORTING ERROR

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

        winpctg.update({team["teamname"]: rounded_pctg})
    
    pctg_sorted_items = sorted(winpctg.items(), key=lambda item: item[1], reverse=True)
    pctg_sorted = dict(pctg_sorted_items)

    for seeds, wins in pctg_sorted.items():
                print(f'{x}. {seeds}: {wins}% win rate')
                x = x + 1

    return
    
def win_pctg(teams):
    totalwins = {}
    winpctg_menu = True
    x = 1

    for team in teams["teams"]:
        totalwins.update({team["teamname"]: team["alltimewins"]})

    totalwins_sorted_items = sorted(totalwins.items(), key=lambda item: item[1], reverse=True)
    totalwins_sorted = dict(totalwins_sorted_items)

    while winpctg_menu == True:
        print(f'1. Total Wins')
        print(f'2. Win Percentage')
        print(f'3. Back')
        pctg_input = int(input(f'Please choose from the above options: '))

        if (pctg_input == 1):
            for seeds, wins in totalwins_sorted.items():
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
        ppg.update({team["teamname"]: team["offppg"]}) 

    ppg_sorted_items = sorted(ppg.items(), key=lambda item: item[1], reverse=True)
    ppg_sorted = dict(ppg_sorted_items)

    for seeds, points in ppg_sorted.items():
        print(f'{x}. {seeds}: {points} ppg')
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
                total_yds.update({team["teamname"]: team["offypg"]})

            totalyds_sorted_items = sorted(total_yds.items(), key=lambda item: item[1], reverse=True)
            totalyds_sorted = dict(totalyds_sorted_items)

            for seeds, yards in totalyds_sorted.items():
                print(f'{x}. {seeds}: {yards} total yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 2):
            for team in teams["teams"]:
                rush_yds.update({team["teamname"]: team["rushydgame"]})

            rushyds_sorted_items = sorted(rush_yds.items(), key=lambda item: item[1], reverse=True)
            rushyds_sorted = dict(rushyds_sorted_items)

            for seeds, yards in rushyds_sorted.items():
                print(f'{x}. {seeds}: {yards} rushing yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 3):
            for team in teams["teams"]:
                pass_yds.update({team["teamname"]: team["passydgame"]})

            passyds_sorted_items = sorted(pass_yds.items(), key=lambda item: item[1], reverse=True)
            passyds_sorted = dict(passyds_sorted_items)

            for seeds, yards in passyds_sorted.items():
                print(f'{x}. {seeds}: {yards} passing yards per game')
                x = x + 1

            x = 1
            continue
        else:
            yds_menu = False

    return

def def_ppg(teams):
    ppg = {}
    x = 1

    for team in teams["teams"]:
        ppg.update({team["teamname"]: team["defppg"]}) 

    ppg_sorted_items = sorted(ppg.items(), key=lambda item: item[1])
    ppg_sorted = dict(ppg_sorted_items)

    for seeds, points in ppg_sorted.items():
        print(f'{x}. {seeds}: {points} ppg')
        x = x + 1

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
        continue
    if (user_input == 4):
        def_ppg(playoff_teams_2025)
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

