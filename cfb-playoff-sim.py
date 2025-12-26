import json
import decimal
user_menu = True

def read_json():
    with open('2025-teams.json') as f:
        d = json.load(f)
        # print(d)
    return d

def games_schedule(teams):
    seeds = {}

    for team in teams["teams"]:
        seeds.update({team["seed"]: team["nameabbr"]}) 

    seeds_sorted = dict(sorted(seeds.items()))

    print(f'Week 1 - Play-in Games\n2 weeks after Conference Championships')
    print(f'{seeds_sorted[20]} @ {seeds_sorted[13]}')
    print(f'{seeds_sorted[19]} @ {seeds_sorted[14]}')
    print(f'{seeds_sorted[18]} @ {seeds_sorted[15]}')
    print(f'{seeds_sorted[17]} @ {seeds_sorted[16]}\n')

    print(f'Week 2 - 1st Round\nWeek of Christmas')
    print(f'{seeds_sorted[20]}/{seeds_sorted[13]} @ {seeds_sorted[1]}')
    print(f'{seeds_sorted[19]}/{seeds_sorted[14]} @ {seeds_sorted[2]}')
    print(f'{seeds_sorted[18]}/{seeds_sorted[15]} @ {seeds_sorted[3]}')
    print(f'{seeds_sorted[17]}/{seeds_sorted[16]} @ {seeds_sorted[4]}')
    print(f'{seeds_sorted[12]} @ {seeds_sorted[5]}')
    print(f'{seeds_sorted[11]} @ {seeds_sorted[6]}')
    print(f'{seeds_sorted[10]} @ {seeds_sorted[7]}')
    print(f'{seeds_sorted[9]} @ {seeds_sorted[8]}')

    print(f'Week 3 - Round 2\nNew Years Games')
    print(f'{seeds_sorted[1]}/{seeds_sorted[13]}/{seeds_sorted[20]} vs {seeds_sorted[8]}/{seeds_sorted[9]} - Orange Bowl')
    print(f'{seeds_sorted[2]}/{seeds_sorted[14]}/{seeds_sorted[19]} vs {seeds_sorted[7]}/{seeds_sorted[10]} - Sugar Bowl')
    print(f'{seeds_sorted[3]}/{seeds_sorted[15]}/{seeds_sorted[18]} vs {seeds_sorted[6]}/{seeds_sorted[11]} - Peach Bowl')
    print(f'{seeds_sorted[4]}/{seeds_sorted[16]}/{seeds_sorted[17]} vs {seeds_sorted[5]}/{seeds_sorted[12]} - Cotton Bowl')

    print(f'Week 4 - Semi-Finals')
    print(f'{seeds_sorted[1]}/{seeds_sorted[8]}/{seeds_sorted[9]}/{seeds_sorted[13]}/{seeds_sorted[20]} vs {seeds_sorted[4]}/{seeds_sorted[5]}/{seeds_sorted[12]}/{seeds_sorted[16]}/{seeds_sorted[17]}  - Rose Bowl')
    print(f'{seeds_sorted[2]}/{seeds_sorted[7]}/{seeds_sorted[10]}/{seeds_sorted[14]}/{seeds_sorted[19]} vs {seeds_sorted[3]}/{seeds_sorted[6]}/{seeds_sorted[11]}/{seeds_sorted[15]}/{seeds_sorted[18]}  - Fiesta Bowl')

    print(f'Week 5 - National Championship')
    print(f'{seeds_sorted[1]}/{seeds_sorted[8]}/{seeds_sorted[9]}/{seeds_sorted[13]}/{seeds_sorted[20]}/{seeds_sorted[4]}/{seeds_sorted[5]}/{seeds_sorted[12]}/{seeds_sorted[16]}/{seeds_sorted[17]} vs {seeds_sorted[2]}/{seeds_sorted[7]}/{seeds_sorted[10]}/{seeds_sorted[14]}/{seeds_sorted[19]}/{seeds_sorted[3]}/{seeds_sorted[6]}/{seeds_sorted[11]}/{seeds_sorted[15]}/{seeds_sorted[18]}')

    return

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
        print(f'{x}. {seeds}: {points} ppg allowed')
        x = x + 1

    return

def def_yds(teams):
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
                total_yds.update({team["teamname"]: team["defypg"]})

            totalyds_sorted_items = sorted(total_yds.items(), key=lambda item: item[1])
            totalyds_sorted = dict(totalyds_sorted_items)

            for seeds, yards in totalyds_sorted.items():
                print(f'{x}. {seeds}: {yards} total yards allowed per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 2):
            for team in teams["teams"]:
                rush_yds.update({team["teamname"]: team["defrushydgame"]})

            rushyds_sorted_items = sorted(rush_yds.items(), key=lambda item: item[1])
            rushyds_sorted = dict(rushyds_sorted_items)

            for seeds, yards in rushyds_sorted.items():
                print(f'{x}. {seeds}: {yards} rushing yards allowed per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 3):
            for team in teams["teams"]:
                pass_yds.update({team["teamname"]: team["defpassydgame"]})

            passyds_sorted_items = sorted(pass_yds.items(), key=lambda item: item[1])
            passyds_sorted = dict(passyds_sorted_items)

            for seeds, yards in passyds_sorted.items():
                print(f'{x}. {seeds}: {yards} passing yards allowed per game')
                x = x + 1

            x = 1
            continue
        else:
            yds_menu = False

    return

def to_margin(teams):
    to = {}
    x = 1

    for team in teams["teams"]:
        to.update({team["teamname"]: team["turnovermargin"]}) 

    to_sorted_items = sorted(to.items(), key=lambda item: item[1], reverse=True)
    to_sorted = dict(to_sorted_items)

    for seeds, tos in to_sorted.items():
        print(f'{x}. {seeds}: {tos}')
        x = x + 1

    return

def prestige_calculation(teams):

    return

# def team_performance():
#     return


playoff_teams_2025 = read_json()

while user_menu == True:
    print(f'1. View Game Schedule')
    print(f'2. All-time Win Percentage')
    print(f'3. Offensive Points Per Game')
    print(f'4. Offensive Yards Per Game')
    print(f'5. Defensive Points Per Game')
    print(f'6. Defensive Yards Per Game')
    print(f'7. Turnover Margin')
    print(f'8. End Program')
    user_input = int(input(f'Please choose which stat you wish to see: '))

    if (user_input == 1):
        games_schedule(playoff_teams_2025)
        continue
    if (user_input == 2):
        win_pctg(playoff_teams_2025)
        continue
    if (user_input == 3):
        off_ppg(playoff_teams_2025)
        continue
    if (user_input == 4):
        off_yds(playoff_teams_2025)
        continue
    if (user_input == 5):
        def_ppg(playoff_teams_2025)
        continue
    if (user_input == 6):
        def_yds(playoff_teams_2025)
        continue
    if (user_input == 7):
        to_margin(playoff_teams_2025)
        continue
    else:
        user_menu = False
    
#TO-DO - PRESTIGE CALC - APPEND TO END OF JSON
#TO-DO - PERFORMANCE EQUATION
#STATS WEBSITE: https://www.teamrankings.com/ncf/stats/

