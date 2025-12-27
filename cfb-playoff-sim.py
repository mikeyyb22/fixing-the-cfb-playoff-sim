import json
import decimal
import random
import math

avg_drive = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
avg_scoring_drive = [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
avg_variance = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5]

user_menu = True

def read_json():
    with open('2025-teams.json') as f:
        d = json.load(f)
        # print(d)
    return d

def coin_flip():
    flip = random.choice([1, 2])
    if flip == 1:
        return "heads"
    if flip == 2:
        return "tails"

def rng():
    randnum = random.uniform(.75, 1.25)

    return randnum

def avg_rng(avg):
    avg_randnum = random.choice(avg)
    randnum_variance = random.choice(avg_variance)
    
    avg_randnum = avg_randnum + randnum_variance

    return avg_randnum

def games_schedule(teams):  #Show schedule
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

def bracket_(teams):        #Start games simulation
    wk1_gm1 = {}            #20 @ 13
    w1g1 = "wk1_gm1"
    wk1_gm2 = {}            #19 @ 14
    w1g2 = "wk1_gm2"
    wk1_gm3 = {}            #18 @ 15
    w1g3 = "wk1_gm3"
    wk1_gm4 = {}            #17 @ 16
    w1g4 = "wk1_gm4"

    seed_20 = teams["teams"][19]
    seed_19 = teams["teams"][18]
    seed_18 = teams["teams"][17]
    seed_17 = teams["teams"][16]
    seed_16 = teams["teams"][15]
    seed_15 = teams["teams"][14]
    seed_14 = teams["teams"][13]
    seed_13 = teams["teams"][12]

    wk1_gm1["hometeam"] = seed_13
    wk1_gm1["awayteam"] = seed_20

    game_sim(wk1_gm1, w1g1)

def game_log(log, week):
    # put game log from drive_ into here
    log = log + week

    return log

def kickoff_return():
    randnum = rng()
    randnum = randnum * 0.5
    # Touchback
    if randnum <= 0.5:
        start_drive = 25
    # Return
    if 0.98 > randnum >= 0.5:
        rand_return = rng()
        return_length = 20 * rand_return
        start_drive = return_length
    if randnum >= 0.98:
        start_drive = 100
    
    return start_drive

def pat_2pt(gamestate, score, gametime):
    home_score = score[0]
    away_score = score[1]

    if 
    

def drive_(team, gamestate, score, gametime):
    start_drive = 1
    # Kickoff / Punt return
    if gamestate == "kickoff":
        start_drive = kickoff_return()
        if start_drive == 100:
            gamestate = pat_2pt(gamestate, score, gametime)
        
    return gamestate

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
        pctg_input = input(f'Please choose from the above options: ')

        if (pctg_input == "1"):
            for seeds, wins in totalwins_sorted.items():
                print(f'{x}. {seeds}: {wins} wins')
                x = x + 1
            continue
        if (pctg_input == "2"):
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
    prestige = {}
    prestigerating = 0.0
    winpct = 0.0
    x = 1

    for team in teams["teams"]:
        winpct = team["alltimewins"] / team["alltimegames"]
        prestigerating = (team["wins"] - team["losses"] + team["natchamp"] + team["confchamp"] + team["heisman"]) * winpct * team["confstrength"]
        if team["nameabbr"] == "ND":
            prestigerating = prestigerating + 50
        pctg = str(round(prestigerating, 3))
        round_help = decimal.Decimal("0.1")
        pctg = decimal.Decimal(pctg)
        rounded_prestige = float(pctg.quantize(round_help, rounding=decimal.ROUND_HALF_UP))
        team["prestige"] = rounded_prestige

    for team in teams["teams"]:
        prestige.update({team["teamname"]: team["prestige"]}) 

    # prestige_sorted_items = sorted(prestige.items(), key=lambda item: item[1], reverse=True)
    # prestige_sorted = dict(prestige_sorted_items)

    # for seeds, prestige in prestige_sorted.items():
    #     print(f'{x}. {seeds}: {prestige} Prestige Rating')
    #     x = x + 1

    return teams

def game_sim(teams, week):
    game_score = [0, 0] # Home team always first value
    home_team = {}
    away_team = {}
    gamestate = ""
    gametime = ""

    home_team["team"] = teams["hometeam"]
    away_team["team"] = teams["awayteam"]
    home_team_luck = rng()              # luck number for game
    away_team_luck = rng()              # luck number for game
    coinflip = coin_flip()
    
    # Home team starts with ball
    if coinflip == "heads":
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        home_drive_count = math.floor((away_team["team"]["defypg"] / drive_length) * home_team_luck)
        if home_drive_count > 15:
            home_drive_count = 15
        if home_drive_count < 10:
            home_drive_count = 10
        away_drive_count = home_drive_count + drive_variance

        # home_drive_count = 10
        # away_drive_count = 10

        # Create game log
        globals()[f'{week}_game_log'] = ""
        globals()[f'{week}_game_log'] = globals()[f'{week}_game_log'] + week
        gamestate = "kickoff"
        gametime = "1sthalf"
        # Start game (drives)
        if home_drive_count == away_drive_count:
            for x in range(home_drive_count):
                if home_drive_count - 2 > x > home_drive_count / 2:
                    gametime = "2ndhalf"
                    # print(f'x: {x}, gametime: {gametime}')
                    drive_(home_team, gamestate, game_score, gametime)
                    drive_(away_team, gamestate, game_score, gametime)
                if x > home_drive_count - 2:
                    gametime = "2minleft"
                    # print(f'x: {x}, gametime: {gametime}')
                    drive_(home_team, gamestate, game_score, gametime)
                    drive_(away_team, gamestate, game_score, gametime)
                else:
                    # print(f'x: {x}, gametime: {gametime}')
                    drive_(home_team, gamestate, game_score, gametime)
                    drive_(away_team, gamestate, game_score, gametime)
        if home_drive_count > away_drive_count:
            for x in range(home_drive_count):
                drive_(home_team, gamestate, game_score)
                if x != home_drive_count - 1:
                    drive_(away_team, gamestate, game_score)
        if home_drive_count < away_drive_count:
            for x in range(away_drive_count):
                if x < (away_drive_count - 1) / 2:
                    drive_(home_team, gamestate, game_score)
                    drive_(away_team, gamestate, game_score)
                else:
                    drive_(away_team, gamestate, game_score)
                    if x!= away_drive_count - 1:
                        drive_(home_team, gamestate, game_score)
                

    # Away team starts with ball
    if coinflip == "tails":
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        away_drive_count = math.floor((home_team["team"]["defypg"] / drive_length) * away_team_luck)
        if away_drive_count > 15:
            away_drive_count = 15
        if away_drive_count < 10:
            away_drive_count = 10
        home_drive_count = away_drive_count + drive_variance
        
        # Create game log
        globals()[f'{week}_game_log'] = ""
        globals()[f'{week}_game_log'] = globals()[f'{week}_game_log'] + week
        gamestate = "kickoff"
        # Start game (drives)
        if away_drive_count == home_drive_count:
            for x in range(away_drive_count):
                drive_(away_team, gamestate, game_score)
                drive_(home_team, gamestate, game_score)
        if away_drive_count > home_drive_count:
            for x in range(away_drive_count):
                drive_(away_team, gamestate, game_score)
                if x != away_drive_count - 1:
                    drive_(home_team, gamestate, game_score)
        if away_drive_count < home_drive_count:
            for x in range(home_drive_count):
                if x < (home_drive_count - 1) / 2:
                    drive_(away_team, gamestate, game_score)
                    drive_(home_team, gamestate, game_score)
                else:
                    drive_(home_team, gamestate, game_score)
                    if x!= home_drive_count - 1:
                        drive_(away_team, gamestate, game_score)

    return




playoff_teams_2025 = read_json()
playoff_teams_2025 = prestige_calculation(playoff_teams_2025)
bracket_(playoff_teams_2025)

# while user_menu == True:
#     print(f'1. View Game Schedule')
#     print(f'2. All-time Win Percentage')
#     print(f'3. Offensive Points Per Game')
#     print(f'4. Offensive Yards Per Game')
#     print(f'5. Defensive Points Per Game')
#     print(f'6. Defensive Yards Per Game')
#     print(f'7. Turnover Margin')
#     print(f'8. View json file')
#     print(f'9. End Program')
#     user_input = input(f'Please choose which stat you wish to see: ')

#     if (user_input == "1"):
#         games_schedule(playoff_teams_2025)
#         continue
#     if (user_input == "2"):
#         win_pctg(playoff_teams_2025)
#         continue
#     if (user_input == "3"):
#         off_ppg(playoff_teams_2025)
#         continue
#     if (user_input == "4"):
#         off_yds(playoff_teams_2025)
#         continue
#     if (user_input == "5"):
#         def_ppg(playoff_teams_2025)
#         continue
#     if (user_input == "6"):
#         def_yds(playoff_teams_2025)
#         continue
#     if (user_input == "7"):
#         to_margin(playoff_teams_2025)
#         continue
#     if (user_input == "8"):
#         print(playoff_teams_2025)
#         continue
#     else:
#         user_menu = False

#TO-DO - PERFORMANCE EQUATION
