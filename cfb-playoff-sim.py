import json
import decimal
import random
import math
from statsort import *
from drive import *
from rng import *

avg_drive = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
avg_scoring_drive = [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
avg_variance = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5]

user_menu = True

def read_json(year):
    with open(year) as f:
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

def true_strength(teams):
    print(f'In true_strength function...')
    print(f'{teams["hometeam"]["nameabbr"]}\'s strength of schedule is #{teams["hometeam"]["sos"]}.')
    print(f'{teams["awayteam"]["nameabbr"]}\'s strength of schedule is #{teams["awayteam"]["sos"]}.')

    # True strength based off SOS
    if teams["hometeam"]["sos"] <= 10:
        print(f'{teams["hometeam"]["nameabbr"]} will receive a boost to offypg and defypg of 1.15x. The old stats were offypg: {teams["hometeam"]["offypg"]} and defypg: {teams["hometeam"]["defypg"]}')
        teams["hometeam"]["offypg"] = (teams["hometeam"]["offypg"]) * 1.15
        teams["hometeam"]["defypg"] = (teams["hometeam"]["defypg"]) * 1.15
        print(f'The new stats for {teams["hometeam"]["nameabbr"]} are offypg: {teams["hometeam"]["offypg"]} and defypg: {teams["hometeam"]["defypg"]}')
    elif teams["hometeam"]["sos"] <= 25:
        print(f'{teams["hometeam"]["nameabbr"]} will receive a boost to offypg and defypg of 1.10x. The old stats were offypg: {teams["hometeam"]["offypg"]} and defypg: {teams["hometeam"]["defypg"]}')
        teams["hometeam"]["offypg"] = (teams["hometeam"]["offypg"]) * 1.10
        teams["hometeam"]["defypg"] = (teams["hometeam"]["defypg"]) * 1.10
        teams["hometeam"]["defypg"] = (teams["hometeam"]["defypg"]) * 1.15
        print(f'The new stats for {teams["hometeam"]["nameabbr"]} are offypg: {teams["hometeam"]["offypg"]} and defypg: {teams["hometeam"]["defypg"]}')

    if teams["awayteam"]["sos"] <= 10:
        print(f'{teams["awayteam"]["nameabbr"]} will receive a boost to offypg and defypg of 1.15x. The old stats were offypg: {teams["awayteam"]["offypg"]} and defypg: {teams["awayteam"]["defypg"]}')
        teams["awayteam"]["offypg"] = (teams["awayteam"]["offypg"]) * 1.15
        teams["awayteam"]["defypg"] = (teams["awayteam"]["defypg"]) * 1.15
        print(f'The new stats for {teams["awayteam"]["nameabbr"]} are offypg: {teams["awayteam"]["offypg"]} and defypg: {teams["awayteam"]["defypg"]}')
    elif teams["awayteam"]["sos"] <= 25:
        print(f'{teams["awayteam"]["nameabbr"]} will receive a boost to offypg and defypg of 1.10x. The old stats were offypg: {teams["awayteam"]["offypg"]} and defypg: {teams["awayteam"]["defypg"]}')
        teams["awayteam"]["offypg"] = (teams["awayteam"]["offypg"]) * 1.10
        teams["awayteam"]["defypg"] = (teams["awayteam"]["defypg"]) * 1.10
        print(f'The new stats for {teams["awayteam"]["nameabbr"]} are offypg: {teams["awayteam"]["offypg"]} and defypg: {teams["awayteam"]["defypg"]}')

    print(f'Exiting true_strength function...')
    return teams

def game_sim(teams, week):
    game_score = [0, 0] # Home team always first value
    gamestate = ""
    gametime = ""
    possession = ""
    yard_line = 1

    # Return equalized stats based on SOS
    teams = true_strength(teams)

    # Define luck for each team, and coinflip to see who gets ball first
    home_team_luck = game_rng()
    away_team_luck = game_rng()
    # See if prestige rating will help/hinder luck
    home_prestige = prestige_luck(teams["hometeam"])
    away_prestige = prestige_luck(teams["awayteam"])
    home_team_luck = home_team_luck * home_prestige
    away_team_luck = away_team_luck * away_prestige
    coinflip = coin_flip()

    # Home team starts with ball
    if coinflip == "heads":
        # Define how many drives each team will have, with home team receiving ball first
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        home_drive_count = math.floor((teams["awayteam"]["defypg"] / drive_length) * home_team_luck)
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
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:
                    gametime = "2minleft"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
        # Home team has 1 more drive than away team
        if home_drive_count > away_drive_count:
            for x in range(home_drive_count):
                # Is game in 2nd half?
                if home_drive_count - 2 > x > home_drive_count / 2:     
                    gametime = "2ndhalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if x != home_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:     
                    gametime = "2minleft"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if x != home_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    if x != home_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
        # Away team has 1 more drive than home team
        if home_drive_count < away_drive_count:
            for x in range(away_drive_count):
                # Is game in 2nd half?
                if home_drive_count - 2 > x > home_drive_count / 2:   
                    gametime = "2ndhalf"  
                    if x < (away_drive_count - 1) / 2:
                        
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    else:
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if x!= away_drive_count - 1:
                            possession = "home"
                            print(f'Drive #{x} - possession is {possession}')
                            game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > home_drive_count - 2:   
                    gametime = "2minleft"  
                    if x < (away_drive_count - 1) / 2:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    else:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if x!= away_drive_count - 1:
                            if gamestate == "score":
                                gamestate = "kickoff"
                            possession = "home"
                            print(f'Drive #{x} - possession is {possession}')
                            drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Else, game is still in first half
                else:   
                    gametime = "1sthalf"  
                    if x < (away_drive_count - 1) / 2:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    else:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if x!= away_drive_count - 1:
                            if gamestate == "score":
                                gamestate = "kickoff"
                            possession = "home"
                            print(f'Drive #{x} - possession is {possession}')
                            game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                

    # Away team starts with ball
    if coinflip == "tails":
        # Define how many drives each team will have, with away team receiving ball first
        drive_length = avg_rng(avg_drive)
        drive_variance = random.choice([-1, 0, 1])
        away_drive_count = math.floor((teams["hometeam"]["defypg"] / drive_length) * away_team_luck)
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
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:
                    gametime = "2minleft"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "home"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
        # Away team has 1 more drive than home team
        if away_drive_count > home_drive_count:
            for x in range(away_drive_count):
                # Is game in 2nd half?
                if away_drive_count - 2 > x > away_drive_count / 2:     
                    gametime = "2ndhalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if x != away_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:     
                    gametime = "2minleft"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if x != away_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                # Else, game is still in first half
                else:
                    gametime = "1sthalf"
                    if gamestate == "score":
                        gamestate = "kickoff"
                    possession = "away"
                    print(f'Drive #{x} - possession is {possession}')
                    game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                    if x != away_drive_count - 1:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
        # Home team has 1 more drive than away team
        if away_drive_count < home_drive_count:
            for x in range(home_drive_count):
                # Is game in 2nd half?
                if away_drive_count - 2 > x > away_drive_count / 2:   
                    gametime = "2ndhalf"  
                    if x < (home_drive_count - 1) / 2:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    else:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        if x!= home_drive_count - 1:
                            if gamestate == "score":
                                gamestate = "kickoff"
                            possession = "away"
                            print(f'Drive #{x} - possession is {possession}')
                            game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Last drive? (assumes 2 mins left)
                if x > away_drive_count - 2:   
                    gametime = "2minleft"  
                    if x < (home_drive_count - 1) / 2:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    else:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        if x!= home_drive_count - 1:
                            if gamestate == "score":
                                gamestate = "kickoff"
                            possession = "away"
                            print(f'Drive #{x} - possession is {possession}')
                            game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                # Else, game is still in first half
                else:   
                    gametime = "1sthalf"  
                    if x < (home_drive_count - 1) / 2:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "away"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                    else:
                        if gamestate == "score":
                            gamestate = "kickoff"
                        possession = "home"
                        print(f'Drive #{x} - possession is {possession}')
                        game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, home_team_luck)
                        if x!= home_drive_count - 1:
                            if gamestate == "score":
                                gamestate = "kickoff"
                            possession = "away"
                            print(f'Drive #{x} - possession is {possession}')
                            game_score, gamestate, yard_line = drive_start(teams, gamestate, game_score, gametime, yard_line, possession, away_team_luck)
                
    print(f'Exiting game_sim function...')
    return


year_input = input('Choose year (2010 or 2025): ')
year_ = f'{year_input}-teams.json'

globals()[f'playoff_teams_{year_input}'] = read_json(year_)

# Add prestige rating
globals()[f'playoff_teams_{year_input}'] = prestige_calculation(globals()[f'playoff_teams_{year_input}'])

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
    user_input = input(f'Please choose one of the options above: ')

    if (user_input == "1"):
        # Show game schedule and possible matchups
        games_schedule(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "2"):
        # Sort by all-time win %
        win_pctg(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "3"):
        # Sort by offensive ppg
        off_ppg(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "4"):
        # Sort by offensive ypg
        off_yds(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "5"):
        # Sort by defensive ppg
        def_ppg(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "6"):
        # Sort by defensive ypg
        def_yds(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "7"):
        # Sort by turnover margin
        to_margin(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "8"):
        # Sort by prestige rating
        prestige_(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "9"):
        # View dictionary of playoff teams
        print(globals()[f'playoff_teams_{year_input}'])
        continue
    if (user_input == "10"):
        bracket_(globals()[f'playoff_teams_{year_input}'])
        continue
    else:
        # Terminate program
        user_menu = False