import decimal

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

        if(yds_input == "1"):
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
        if(yds_input == "2"):
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
        if(yds_input == "3"):
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
