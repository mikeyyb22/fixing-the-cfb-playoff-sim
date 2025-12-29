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
    print(f'In coin_flip() function...')
    flip = random.choice([1, 2])
    if flip == 1:
        print(f'Coinflip is heads')
        print(f'Exiting coin_flip() function...')
        return "heads"
    if flip == 2:
        print(f'Coinflip is tails')
        print(f'Exiting coin_flip() function...')
        return "tails"

def rng():
    print(f'In rng() function...')
    randnum = random.uniform(.75, 1.25)
    print(f'Random number generated in rng() is {randnum}')
    
    print(f'Exiting rng() function...')
    return randnum

def game_rng():
    print(f'In game_rng() function...')
    randnum = random.uniform(0, 1.0)
    print(f'Random number generated in game_rng() is {randnum}')
    print(f'Exiting game_rng() function...')

    return randnum

def avg_rng(avg):
    print(f'In avg_rng function...')
    print(f'Value passed through function is {type(avg)}')
    avg_randnum = random.choice(avg)
    randnum_variance = random.choice(avg_variance)
    
    avg_randnum = avg_randnum + randnum_variance
    print(f'Random number generated from {type(avg)} and variance is {avg_randnum}')

    print(f'Exiting avg_rng function...')
    return avg_randnum

def games_schedule(teams):  #Show schedule
    print(f'In games_schedule function...')
    
    # Create new dictionary with seeds and team abbreviation, then sort by seed
    seeds = {}
    for team in teams["teams"]:
        seeds.update({team["seed"]: team["nameabbr"]})
    seeds_sorted = dict(sorted(seeds.items()))

    # Print schedule
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

    print(f'Exiting games_schedule function...')

    return

def bracket_(teams):        #Start games simulation
    print(f'In bracket_ function...')
    
    # Create dictionary for each matchup
    wk1_gm1 = {}            #20 @ 13
    w1g1 = "wk1_gm1"
            # wk1_gm2 = {}            #19 @ 14
            # w1g2 = "wk1_gm2"
            # wk1_gm3 = {}            #18 @ 15
            # w1g3 = "wk1_gm3"
            # wk1_gm4 = {}            #17 @ 16
            # w1g4 = "wk1_gm4"

    # Assign teams in matchup to wk{x}_gm{x} dictionary
    seed_20 = teams["teams"][19]
            # seed_19 = teams["teams"][18]
            # seed_18 = teams["teams"][17]
            # seed_17 = teams["teams"][16]
            # seed_16 = teams["teams"][15]
            # seed_15 = teams["teams"][14]
            # seed_14 = teams["teams"][13]
    seed_13 = teams["teams"][12]
    wk1_gm1["hometeam"] = seed_13
    wk1_gm1["awayteam"] = seed_20

    game_sim(wk1_gm1, w1g1)

    print(f'Exiting bracket_ function...')
    return

def game_log(log, week):
    # put game log from drive_ into here
    log = log + week

    return log

def kickoff_return():
    print(f'In kickoff_return function...')
    randnum = game_rng()
    print(f'Randnum for kickoff return is {randnum}')
    # Touchback
    if randnum <= 0.5:
        start_drive = 25
        print(f'Touchback - drive starts at {start_drive} yd line')
    # Returned kick
    if 0.98 > randnum >= 0.5:
        print(f'Kick will be returned. Generating rand_return to get return length...')
        rand_return = rng()
        return_length = 30 * rand_return        # Avg return length
        start_drive = return_length
        print(f'Kick was returned for {start_drive} yds')
    # KOR TD
    if randnum >= 0.98:
        print(f'Kick was returned for a touchdown')
        start_drive = 100
    
    print(f'Exiting kickoff_return function...')
    return start_drive

def pat_2pt(gamestate, score, gametime, possession):
    print(f'In pat_2pt function...')
    home_score = score[0]
    away_score = score[1]
    
    # Situation where home team would go for 2 at end of game
    if possession == "home" and gametime == "2minleft":
        if (away_score - home_score) > 7:
            #try for 2 points
            print(f'Scoring team will go for 2...')
            randnum = game_rng()
            if randnum <= 0.45:             # 2pt good
                gamestate = "touchdown+2pt"
                print(f'2 point conversion was good, gamestate is now {gamestate}')
                print(f'Exiting pat_2pt function...')
                return gamestate
            else:                           # 2pt no good
                gamestate = "touchdown+no2pt"
                print(f'2 point conversion no good, gamestate is now {gamestate}')
                print(f'Exiting pat_2pt function...')
                return gamestate
    # Situation where away team would go for 2 at end of game
    elif possession == "away" and gametime == "2minleft":
        if (home_score - away_score) > 7:
            #try for 2 points
            print(f'Scoring team will go for 2...')
            randnum = game_rng()
            if randnum <= 0.45:             # 2pt good
                gamestate = "touchdown+2pt"
                print(f'2 point conversion was good, gamestate is now {gamestate}')
                print(f'Exiting pat_2pt function...')
                return gamestate
            else:                           # 2pt no good
                gamestate = "touchdown+no2pt"
                print(f'2 point conversion no good, gamestate is now {gamestate}')
                print(f'Exiting pat_2pt function...')
                return gamestate
    # Extra point
    else:
        print(f'Scoring team will kick extra point')
        randnum = game_rng()
        if randnum <= 0.9:                  # PAT good
            gamestate = "touchdown+pat"
            print(f'Extra point is good, gamestate is now {gamestate}')
            print(f'Exiting pat_2pt function...')
            return gamestate
        if 0.98 > randnum > 0.9:            # PAT missed
            gamestate = "touchdown+nopat"
            print(f'Extra point is no good, gamestate is now {gamestate}')
            print(f'Exiting pat_2pt function...')
            return gamestate
        else:                               # PAT --> 2pt
            gamestate = "touchdown+2pt"
            print(f'PAT botched, but converted, gamestate is now {gamestate}')
            print(f'Exiting pat_2pt function...')
            return gamestate

def drive_result(team, start_drive, gamestate, possession):
    print(f'In drive_result function...')

    print(f'Exiting drive_result function...')
    return

def drive_start(team, gamestate, score, gametime, possession):
    print(f'In drive_start function...')

    start_drive = 1                 # Default value for yardline of drive start
    # Kickoff / Punt return
    if gamestate == "kickoff":
        start_drive = kickoff_return()
        if start_drive == 100:      # Drive does not continue if KR TD
            gamestate = pat_2pt(gamestate, score, gametime, possession)
        else:
            gamestate = drive_result(team, start_drive, gamestate, possession)
        


    if possession == "home":
        if gamestate == "fieldgoalmiss":
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "fieldgoalmake":
            score[0] = score[0] + 3
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+pat":
            score[0] = score[0] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+nopat":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+2pt":
            score[0] = score[0] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+no2pt":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "safety":
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            score[1] = score[1] + 2
        else:
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
    elif possession == "away":
        if gamestate == "fieldgoalmiss":
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "fieldgoalmake":
            score[1] = score[1] + 3
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+pat":
            score[1] = score[1] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+nopat":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+2pt":
            score[1] = score[1] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "touchdown+no2pt":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        if gamestate == "safety":
            score[0] = score[0] + 2
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
        else:
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate
    
def win_pctg_calc(teams):
    print(f'In win_pctg_calc function...')
    x = 1

    # Create new dictionary that includes win percentage
    winpctg = {}
    wins = 0
    games = 0
    pctg = 0.0
    for team in teams["teams"]:
        # Calculate win percentage
        wins = int(team["alltimewins"])
        games = int(team["alltimegames"])
        # Round to nearest tenth 
        pctg = str(round((wins / games), 3) * 100)
        round_help = decimal.Decimal("0.1")
        pctg = decimal.Decimal(pctg)
        rounded_pctg = pctg.quantize(round_help, rounding=decimal.ROUND_HALF_UP)
        # Update new dictionary with rounded values
        winpctg.update({team["teamname"]: rounded_pctg})
    
    # Sort new dictionary
    pctg_sorted_items = sorted(winpctg.items(), key=lambda item: item[1], reverse=True)
    pctg_sorted = dict(pctg_sorted_items)

    # Print list
    for seeds, wins in pctg_sorted.items():
                print(f'{x}. {seeds}: {wins}% win rate')
                x = x + 1

    print(f'Exiting win_pctg_calc function...')
    return
    
def win_pctg(teams):
    print(f'In win_pctg function...')
    winpctg_menu = True
    x = 1
    
    # Create new dictionary with teams and all-time wins, then sort
    totalwins = {}
    for team in teams["teams"]:
        totalwins.update({team["teamname"]: team["alltimewins"]})
    totalwins_sorted_items = sorted(totalwins.items(), key=lambda item: item[1], reverse=True)
    totalwins_sorted = dict(totalwins_sorted_items)

    # Win percentage menu
    while winpctg_menu == True:
        print(f'1. Total Wins')             # Sort by total wins
        print(f'2. Win Percentage')         # Sort by win percentage
        print(f'3. Back')                   # Exit to main menu
        pctg_input = input(f'Please choose from the above options: ')

        if (pctg_input == "1"):
            # Sort by total wins
            # Print list
            for seeds, wins in totalwins_sorted.items():
                print(f'{x}. {seeds}: {wins} wins')
                x = x + 1
            continue
        if (pctg_input == "2"):
            # Sort by win percentage
            win_pctg_calc(teams)
            continue
        else:
            # Exit to main menu
            winpctg_menu = False
        
    print(f'Exiting win_pctg function...')
    return

def off_ppg(teams):
    print(f'In off_ppg function...')
    x = 1

    # Create new dictionary with teams and ppg, then sort
    ppg = {}
    for team in teams["teams"]:
        ppg.update({team["teamname"]: team["offppg"]}) 
    ppg_sorted_items = sorted(ppg.items(), key=lambda item: item[1], reverse=True)
    ppg_sorted = dict(ppg_sorted_items)

    # Print list
    for seeds, points in ppg_sorted.items():
        print(f'{x}. {seeds}: {points} ppg')
        x = x + 1

    print(f'Exiting off_ppg function...')
    return

def off_yds(teams):
    print(f'In off_yds function...')
    total_yds = {}
    rush_yds = {}
    pass_yds = {}
    yds_menu = True
    x = 1

    # Menu for yards by team
    while yds_menu == True:
        print(f'1. Total Yards')    # Sorts by total ypg
        print(f'2. Rush Yards')     # Sorts by rush ypg
        print(f'3. Pass Yards')     # Sorts by pass ypg
        print(f'4. Back')           # Exit to main menu
        yds_input = input(f'Please choose from the above options: ')

        if(yds_input == "1"):
            # Sorts by total ypg
            # Update and sort total yards dictionary
            for team in teams["teams"]:
                total_yds.update({team["teamname"]: team["offypg"]})
            totalyds_sorted_items = sorted(total_yds.items(), key=lambda item: item[1], reverse=True)
            totalyds_sorted = dict(totalyds_sorted_items)

            # Print list
            for seeds, yards in totalyds_sorted.items():
                print(f'{x}. {seeds}: {yards} total yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == "2"):
            # Sorts by rush ypg
            # Update and sort rush yards dictionary
            for team in teams["teams"]:
                rush_yds.update({team["teamname"]: team["rushydgame"]})
            rushyds_sorted_items = sorted(rush_yds.items(), key=lambda item: item[1], reverse=True)
            rushyds_sorted = dict(rushyds_sorted_items)

            # Print list
            for seeds, yards in rushyds_sorted.items():
                print(f'{x}. {seeds}: {yards} rushing yards per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == "3"):
            # Sorts by pass ypg
            # Update and sort pass ypg dictionary
            for team in teams["teams"]:
                pass_yds.update({team["teamname"]: team["passydgame"]})
            passyds_sorted_items = sorted(pass_yds.items(), key=lambda item: item[1], reverse=True)
            passyds_sorted = dict(passyds_sorted_items)

            # Print list
            for seeds, yards in passyds_sorted.items():
                print(f'{x}. {seeds}: {yards} passing yards per game')
                x = x + 1

            x = 1
            continue
        else:
            # Exit to main menu
            yds_menu = False

    print(f'Exiting off_yds function...')
    return

def def_ppg(teams):
    print(f'In def_ppg function...')
    x = 1

    # Create, update, and sort new dictionary for def ppg
    ppg = {}
    for team in teams["teams"]:
        ppg.update({team["teamname"]: team["defppg"]}) 
    ppg_sorted_items = sorted(ppg.items(), key=lambda item: item[1])
    ppg_sorted = dict(ppg_sorted_items)

    # Print list
    for seeds, points in ppg_sorted.items():
        print(f'{x}. {seeds}: {points} ppg allowed')
        x = x + 1

    print(f'Exiting def_ppg function...')
    return

def def_yds(teams):
    print(f'In def_yds function...')
    total_yds = {}
    rush_yds = {}
    pass_yds = {}
    yds_menu = True
    x = 1

    # Defensive ypg menu
    while yds_menu == True:
        print(f'1. Total Yards')    # Sorts by total yds allowed
        print(f'2. Rush Yards')     # Sorts by rush yds allowed
        print(f'3. Pass Yards')     # Sorts by pass yds allowed
        print(f'4. Back')           # Exit to main menu
        yds_input = input(f'Please choose from the above options: ')

        if(yds_input == 1):
            # Sorts by total yds allowed
            # Update and sort total_yds dictionary
            for team in teams["teams"]:
                total_yds.update({team["teamname"]: team["defypg"]})
            totalyds_sorted_items = sorted(total_yds.items(), key=lambda item: item[1])
            totalyds_sorted = dict(totalyds_sorted_items)

            # Print list
            for seeds, yards in totalyds_sorted.items():
                print(f'{x}. {seeds}: {yards} total yards allowed per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 2):
            # Sorts by rush yds allowed
            # Update and sort rush_yds dictionary
            for team in teams["teams"]:
                rush_yds.update({team["teamname"]: team["defrushydgame"]})
            rushyds_sorted_items = sorted(rush_yds.items(), key=lambda item: item[1])
            rushyds_sorted = dict(rushyds_sorted_items)

            # Print list
            for seeds, yards in rushyds_sorted.items():
                print(f'{x}. {seeds}: {yards} rushing yards allowed per game')
                x = x + 1

            x = 1
            continue
        if(yds_input == 3):
            # Sorts by pass yds allowed
            # Update and sort pass_yds dictionary
            for team in teams["teams"]:
                pass_yds.update({team["teamname"]: team["defpassydgame"]})
            passyds_sorted_items = sorted(pass_yds.items(), key=lambda item: item[1])
            passyds_sorted = dict(passyds_sorted_items)

            # Print list
            for seeds, yards in passyds_sorted.items():
                print(f'{x}. {seeds}: {yards} passing yards allowed per game')
                x = x + 1

            x = 1
            continue
        else:
            # Exit to main menu
            yds_menu = False

    print(f'Exiting def_yds function...')
    return

def to_margin(teams):
    print(f'In to_margin function...')
    x = 1

    # Create and sort new dictionary
    to = {}
    for team in teams["teams"]:
        to.update({team["teamname"]: team["turnovermargin"]}) 
    to_sorted_items = sorted(to.items(), key=lambda item: item[1], reverse=True)
    to_sorted = dict(to_sorted_items)

    # Print list
    for seeds, tos in to_sorted.items():
        print(f'{x}. {seeds}: {tos}')
        x = x + 1

    print(f'Exiting to_margin function...')
    return

def prestige_calculation(teams):
    print(f'In prestige_calculation function...')
    prestigerating = 0.0
    winpct = 0.0

    # Create, and update prestige dictionary
    prestige = {}
    for team in teams["teams"]:
        # Calculate win percentage
        winpct = team["alltimewins"] / team["alltimegames"]
        # Formula for rating
        prestigerating = (team["wins"] - team["losses"] + team["natchamp"] + team["confchamp"] + team["heisman"]) * winpct * team["confstrength"]
        # Formula is heavily dependent on conference championships
        # Add rating to Notre Dame to make up for them being independent
        if team["nameabbr"] == "ND":
            prestigerating = prestigerating + 50
        # Round to 1 decimal
        pctg = str(round(prestigerating, 3))
        round_help = decimal.Decimal("0.1")
        pctg = decimal.Decimal(pctg)
        rounded_prestige = float(pctg.quantize(round_help, rounding=decimal.ROUND_HALF_UP))
        team["prestige"] = rounded_prestige

    # Update original dictionary
    for team in teams["teams"]:
        prestige.update({team["teamname"]: team["prestige"]}) 

    print(f'Exiting prestige_calculation function...')
    return teams

def prestige_(teams):
    print(f'In prestige_ function...')
    x = 1

    # Create, update, and sort prestige dictionary
    prestige = {}
    for team in teams["teams"]:
        prestige.update({team["teamname"]: team["prestige"]})
    prestige_sorted_items = sorted(prestige.items(), key=lambda item: item[1], reverse=True)
    prestige_sorted = dict(prestige_sorted_items)

    # Print list
    for seeds, prestige in prestige_sorted.items():
        print(f'{x}. {seeds}: {prestige} Prestige Rating')
        x = x + 1
    
    print(f'Exiting prestige function...')
    return

def game_sim(teams, week):
    game_score = [0, 0] # Home team always first value
    home_team = {}
    away_team = {}
    gamestate = ""
    gametime = ""
    possession = ""

    # Create 2 dictionaries - 1 for home, 1 for away
    home_team["team"] = teams["hometeam"]
    away_team["team"] = teams["awayteam"]
    # Define luck for each team, and coinflip to see who gets ball first
    home_team_luck = rng()
    away_team_luck = rng()
    coinflip = coin_flip()

    # Home team starts with ball
    if coinflip == "heads":
        # Define how many drives each team will have, with home team receiving ball first
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        home_drive_count = math.floor((away_team["team"]["defypg"] / drive_length) * home_team_luck)
        # Eliminate outliers
        if home_drive_count > 15:
            home_drive_count = 15
        if home_drive_count < 10:
            home_drive_count = 10
        # Define away team drive count (one less, equal, or one more than home)
        away_drive_count = home_drive_count + drive_variance

        # Create game log
        globals()[f'{week}_game_log'] = ""
        globals()[f'{week}_game_log'] = globals()[f'{week}_game_log'] + week

        # Start game (drives)
        gamestate = "kickoff"
        gametime = "1sthalf"
        # Home & away team have same amount of drives
        if home_drive_count == away_drive_count:
            for x in range(home_drive_count):
                # Is game in 2nd half? 
                if home_drive_count - 2 > x > home_drive_count / 2:
                    gametime = "2ndhalf"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:
                    gametime = "2minleft"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
        # Home team has 1 more drive than away team
        if home_drive_count > away_drive_count:
            for x in range(home_drive_count):
                # Is game in 2nd half?
                if home_drive_count - 2 > x > home_drive_count / 2:     
                    gametime = "2ndhalf"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, possession)
                    if x != home_drive_count - 1:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:     
                    gametime = "2minleft"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, possession)
                    if x != home_drive_count - 1:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, possession)
                    if x != home_drive_count - 1:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
        # Away team has 1 more drive than home team
        if home_drive_count < away_drive_count:
            for x in range(away_drive_count):
                # Is game in 2nd half?
                if home_drive_count - 2 > x > home_drive_count / 2:   
                    gametime = "2ndhalf"  
                    if x < (away_drive_count - 1) / 2:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                    else:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        if x!= away_drive_count - 1:
                            possession = "home"
                            drive_start(home_team, gamestate, game_score, possession)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:   
                    gametime = "2minleft"  
                    if x < (away_drive_count - 1) / 2:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                    else:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        if x!= away_drive_count - 1:
                            possession = "home"
                            drive_start(home_team, gamestate, game_score, possession)
                # Else, game is still in first half
                else:   
                    gametime = "1sthalf"  
                    if x < (away_drive_count - 1) / 2:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                    else:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        if x!= away_drive_count - 1:
                            possession = "home"
                            drive_start(home_team, gamestate, game_score, possession)
                

    # Away team starts with ball
    if coinflip == "tails":
        # Define how many drives each team will have, with away team receiving ball first
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        away_drive_count = math.floor((home_team["team"]["defypg"] / drive_length) * away_team_luck)
        # Eliminate outliers
        if away_drive_count > 15:
            away_drive_count = 15
        if away_drive_count < 10:
            away_drive_count = 10
        # Define home team drive count (one less, equal, or one more than away)
        home_drive_count = away_drive_count + drive_variance
        
        # Create game log
        globals()[f'{week}_game_log'] = ""
        globals()[f'{week}_game_log'] = globals()[f'{week}_game_log'] + week

        # Start game (drives)
        gamestate = "kickoff"        
        gametime = "1sthalf"
        # Home & away team have same amount of drives
        if away_drive_count == home_drive_count:
            for x in range(away_drive_count):
                # Is game in 2nd half?
                if away_drive_count - 2 > x > away_drive_count / 2:
                    gametime = "2ndhalf"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:
                    gametime = "2minleft"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, gametime, possession)
                    possession = "home"
                    drive_start(home_team, gamestate, game_score, gametime, possession)
        # Away team has 1 more drive than home team
        if away_drive_count > home_drive_count:
            for x in range(away_drive_count):
                # Is game in 2nd half?
                if away_drive_count - 2 > x > away_drive_count / 2:     
                    gametime = "2ndhalf"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, possession)
                    if x != away_drive_count - 1:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:     
                    gametime = "2minleft"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, possession)
                    if x != away_drive_count - 1:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    possession = "away"
                    drive_start(away_team, gamestate, game_score, possession)
                    if x != away_drive_count - 1:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
        # Home team has 1 more drive than away team
        if away_drive_count < home_drive_count:
            for x in range(home_drive_count):
                # Is game in 2nd half?
                if away_drive_count - 2 > x > away_drive_count / 2:   
                    gametime = "2ndhalf"  
                    if x < (home_drive_count - 1) / 2:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                    else:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        if x!= home_drive_count - 1:
                            possession = "away"
                            drive_start(away_team, gamestate, game_score, possession)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:   
                    gametime = "2minleft"  
                    if x < (home_drive_count - 1) / 2:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                    else:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        if x!= home_drive_count - 1:
                            possession = "away"
                            drive_start(away_team, gamestate, game_score, possession)
                # Else, game is still in first half
                else:   
                    gametime = "1sthalf"  
                    if x < (home_drive_count - 1) / 2:
                        possession = "away"
                        drive_start(away_team, gamestate, game_score, possession)
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                    else:
                        possession = "home"
                        drive_start(home_team, gamestate, game_score, possession)
                        if x!= home_drive_count - 1:
                            possession = "away"
                            drive_start(away_team, gamestate, game_score, possession)
                
    print(f'Exiting game_sim function...')
    return




playoff_teams_2025 = read_json()
# Add prestige rating
playoff_teams_2025 = prestige_calculation(playoff_teams_2025)

# Main menu for 2025 playoff teams
while user_menu == True:
    print(f'1. View Game Schedule')             # Show game schedule and possible matchups
    print(f'2. All-time Win Percentage')        # Sort by all-time win %
    print(f'3. Offensive Points Per Game')      # Sort by offensive ppg
    print(f'4. Offensive Yards Per Game')       # Sort by offensive ypg
    print(f'5. Defensive Points Per Game')      # Sort by defensive ppg
    print(f'6. Defensive Yards Per Game')       # Sort by defensive ypg
    print(f'7. Turnover Margin')                # Sort by turnover margin
    print(f'8. See prestige rating')            # Sort by prestige rating
    print(f'9. View json file')                 # View dictionary of playoff teams
    print(f'10. Start simulation')              # Simulate games in current year
    print(f'11. End Program')                   # Terminate program
    user_input = input(f'Please choose one of the options below: ')

    if (user_input == "1"):
        # Show game schedule and possible matchups
        games_schedule(playoff_teams_2025)
        continue
    if (user_input == "2"):
        # Sort by all-time win %
        win_pctg(playoff_teams_2025)
        continue
    if (user_input == "3"):
        # Sort by offensive ppg
        off_ppg(playoff_teams_2025)
        continue
    if (user_input == "4"):
        # Sort by offensive ypg
        off_yds(playoff_teams_2025)
        continue
    if (user_input == "5"):
        # Sort by defensive ppg
        def_ppg(playoff_teams_2025)
        continue
    if (user_input == "6"):
        # Sort by defensive ypg
        def_yds(playoff_teams_2025)
        continue
    if (user_input == "7"):
        # Sort by turnover margin
        to_margin(playoff_teams_2025)
        continue
    if (user_input == "8"):
        # Sort by prestige rating
        prestige_(playoff_teams_2025)
    if (user_input == "9"):
        # View dictionary of playoff teams
        print(playoff_teams_2025)
        continue
    if (user_input == "10"):
        bracket_(playoff_teams_2025)
        continue
    else:
        # Terminate program
        user_menu = False
