from rng import *


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

def def_pat_2pt(gamestate, score, gametime, possession):
    print(f'In def_pat_2pt function...')
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

def punt(gamestate, yard_line):
    print(f'In punt function...')
    punt_luck = rng()

    punt_yds = 45 * punt_luck
    print(f'Punted for {punt_yds} yards.')

    if punt_luck <= 0.76:
        print(f'Punt returned for a touchdown.')
        gamestate = "deftd"
        yard_line = 1
        return gamestate, yard_line
    else:
        yard_line = yard_line + punt_yds
        gamestate = "drivestart"
        if yard_line > 100:
            # Touchback
            print(f'Punted {punt_yds} for a touchback.')
            yard_line = 80
            return gamestate, yard_line
        else:
            return gamestate, yard_line

    print(f'Exiting punt function...')
    return 

def fieldgoal(luck):
    gamestate = ""
    if luck < 0.78:
        print(f'Field goal was blocked.')
        if luck < 0.77:
            print(f'Field goal blocked and returned for touchdown.')
            gamestate = "deftd"
            return gamestate
        else:
            gamestate = "fieldgoalmiss"
            return gamestate
    if 0.85 > luck >= 0.78:
        print(f'Field goal was missed.')
        gamestate = "fieldgoalmiss"
        return gamestate
    else:
        print(f'Field goal made.')
        gamestate = "fieldgoalmake"
        return gamestate

def drive_result(teams, score, start_drive, gamestate, gametime, possession, luck):
    print(f'In drive_result function...')
    down_count = 1                  # Counts downs, so there's no 5th down
    yard_line = start_drive
    play_yards = 0
    yards_to_go = 10

    while down_count <= 4:
        print(f'Current down: {down_count}')
        if possession == "home":
            if down_count == 4:
                if gametime == "2minleft" and 14 >= score[1] - score[0] > 0:
                    print(f'{teams["hometeam"]["nameabbr"]} will go for it on 4th down.')
                    play_success = game_rng()
                    if play_success >= 0.9: 
                        play_yards = ((teams["hometeam"]["offypg"] / 60) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                            yard_line = 1
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            down_count = down_count + 1                            
                            continue
                    elif 0.2 <= play_success < 0.9:
                        play_yards = ((teams["hometeam"]["offypg"] / 70) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                            yard_line = 1
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            down_count = down_count + 1
                            continue
                    elif play_success < 0.2:
                        play_yards = ((teams["hometeam"]["offypg"] / 85) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                            yard_line = 1
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            gamestate = "downs"
                            print(f'{teams["hometeam"]["nameabbr"]} did not get first down. Turnover on downs.')
                            return gamestate, yard_line
                elif yard_line >= 60:
                    print(f'{teams["hometeam"]["nameabbr"]} will try for a {100 - yard_line} yard field goal.')
                    gamestate = fieldgoal(luck)
                    return gamestate, yard_line
                else:
                    print(f'{teams["hometeam"]["nameabbr"]} will punt.')
                    gamestate = "punt"
                    return gamestate, yard_line
            else:
                play_success = game_rng()
                if play_success >= 0.9: 
                    play_yards = ((teams["hometeam"]["offypg"] / 60) * luck)
                    yard_line = yard_line + play_yards
                    yards_to_go = yards_to_go - play_yards
                    print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                    if yard_line >= 100:
                        gamestate = "touchdown"
                        print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                        yard_line = 1
                        return gamestate, yard_line
                    elif yards_to_go < 0:
                        down_count = 1
                        yards_to_go = 10
                        continue
                    else:
                        down_count = down_count + 1                            
                        continue
                elif 0.2 <= play_success < 0.9:
                    play_yards = ((teams["hometeam"]["offypg"] / 70) * luck)
                    yard_line = yard_line + play_yards
                    yards_to_go = yards_to_go - play_yards
                    print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                    if yard_line >= 100:
                        gamestate = "touchdown"
                        print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                        yard_line = 1
                        return gamestate, yard_line
                    elif yards_to_go < 0:
                        down_count = 1
                        yards_to_go = 10
                        continue
                    else:
                        down_count = down_count + 1
                        continue
                elif play_success < 0.2:
                    play_yards = ((teams["hometeam"]["offypg"] / 85) * luck)
                    yard_line = yard_line + play_yards
                    yards_to_go = yards_to_go - play_yards
                    print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                    if yard_line >= 100:
                        gamestate = "touchdown"
                        print(f'{teams["hometeam"]["nameabbr"]} scored a touchdown')
                        yard_line = 1
                        return gamestate, yard_line
                    elif yards_to_go < 0:
                        down_count = 1
                        yards_to_go = 10
                        continue
                    else:
                        down_count = down_count + 1
                        continue

        if possession == "away":
                if down_count == 4:
                    if gametime == "2minleft" and 14 >= score[1] - score[0] > 0:
                        print(f'{teams["awayteam"]["nameabbr"]} will go for it on 4th down.')
                        play_success = game_rng()
                        if play_success >= 0.9: 
                            play_yards = ((teams["awayteam"]["offypg"] / 60) * luck)
                            yard_line = yard_line + play_yards
                            yards_to_go = yards_to_go - play_yards
                            print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                            if yard_line >= 100:
                                gamestate = "touchdown"
                                print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                                yard_line = 1
                                return gamestate, yard_line
                            elif yards_to_go < 0:
                                down_count = 1
                                yards_to_go = 10
                                continue
                            else:
                                down_count = down_count + 1                            
                                continue
                        elif 0.2 <= play_success < 0.9:
                            play_yards = ((teams["awayteam"]["offypg"] / 70) * luck)
                            yard_line = yard_line + play_yards
                            yards_to_go = yards_to_go - play_yards
                            print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                            if yard_line >= 100:
                                gamestate = "touchdown"
                                print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                                yard_line = 1
                                return gamestate, yard_line
                            elif yards_to_go < 0:
                                down_count = 1
                                yards_to_go = 10
                                continue
                            else:
                                down_count = down_count + 1
                                continue
                        elif play_success < 0.2:
                            play_yards = ((teams["awayteam"]["offypg"] / 85) * luck)
                            yard_line = yard_line + play_yards
                            yards_to_go = yards_to_go - play_yards
                            print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                            if yard_line >= 100:
                                gamestate = "touchdown"
                                print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                                yard_line = 1
                                return gamestate, yard_line
                            elif yards_to_go < 0:
                                down_count = 1
                                yards_to_go = 10
                                continue
                            else:
                                gamestate = "downs"
                                print(f'{teams["awayteam"]["nameabbr"]} did not get first down. Turnover on downs.')
                                return gamestate, yard_line
                    elif yard_line >= 60:
                        print(f'{teams["awayteam"]["nameabbr"]} will try for a {100 - yard_line} yard field goal.')
                        gamestate = fieldgoal(luck)
                        return gamestate, yard_line
                    else:
                        print(f'{teams["awayteam"]["nameabbr"]} will punt.')
                        gamestate = "punt"
                        return gamestate, yard_line
                else:
                    play_success = game_rng()
                    if play_success >= 0.9: 
                        play_yards = ((teams["awayteam"]["offypg"] / 60) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                            yard_line = 1
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            down_count = down_count + 1                            
                            continue
                    elif 0.2 <= play_success < 0.9:
                        play_yards = ((teams["awayteam"]["offypg"] / 70) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            yard_line = 1
                            print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            down_count = down_count + 1
                            continue
                    elif play_success < 0.2:
                        play_yards = ((teams["awayteam"]["offypg"] / 85) * luck)
                        yard_line = yard_line + play_yards
                        yards_to_go = yards_to_go - play_yards
                        print(f'The last play went for {play_yards}. The ball is now on the {yard_line}.')
                        if yard_line >= 100:
                            gamestate = "touchdown"
                            print(f'{teams["awayteam"]["nameabbr"]} scored a touchdown')
                            yard_line = 1
                            return gamestate, yard_line
                        elif yards_to_go < 0:
                            down_count = 1
                            yards_to_go = 10
                            continue
                        else:
                            down_count = down_count + 1
                            continue

def drive_start(teams, gamestate, score, gametime, start_drive, possession, luck):
    print(f'In drive_start function...')

    # Kickoff / Punt return
    if gamestate == "kickoff":
        start_drive = kickoff_return()
        if start_drive == 100:      # Drive does not continue if KR TD
            gamestate = pat_2pt(gamestate, score, gametime, possession)
        else:
            gamestate, start_drive = drive_result(teams, score, start_drive, gamestate, gametime, possession, luck)
            if gamestate == "touchdown":
                gamestate = pat_2pt(gamestate, score, gametime, possession)
            elif gamestate == "punt":
                gamestate, start_drive = punt(gamestate, start_drive)
            elif gamestate == "downs":
                gamestate = "drivestart"
                return score, gamestate, start_drive
            elif gamestate == "deftd":
                gamestate = def_pat_2pt(gamestate, score, gametime, possession)
    else:
        gamestate, start_drive = drive_result(teams, score, start_drive, gamestate, gametime, possession, luck)
        if gamestate == "touchdown":
            gamestate = pat_2pt(gamestate, score, gametime, possession)
        elif gamestate == "punt":
            gamestate, start_drive = punt(gamestate, start_drive)
        elif gamestate == "downs":
            return score, gamestate, start_drive
        elif gamestate == "deftd":
            gamestate = def_pat_2pt(gamestate, score, gametime, possession)


    if possession == "home":
        if gamestate == "fieldgoalmiss":
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate, start_drive
        elif gamestate == "fieldgoalmake":
            score[0] = score[0] + 3
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "touchdown+pat":
            score[0] = score[0] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "touchdown+nopat":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "touchdown+2pt":
            score[0] = score[0] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "touchdown+no2pt":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "safety":
            score[1] = score[1] + 2
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        elif gamestate == "deftd+pat":
            score[1] = score[1] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+nopat":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+2pt":
            score[1] = score[1] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+no2pt":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        else:
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate, start_drive
        
    elif possession == "away":
        if gamestate == "fieldgoalmiss":
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate, start_drive
        if gamestate == "fieldgoalmake":
            score[1] = score[1] + 3
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        if gamestate == "touchdown+pat":
            score[1] = score[1] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        if gamestate == "touchdown+nopat":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        if gamestate == "touchdown+2pt":
            score[1] = score[1] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        if gamestate == "touchdown+no2pt":
            score[1] = score[1] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "score"
            return score, gamestate, start_drive
        if gamestate == "safety":
            score[0] = score[0] + 2
            gamestate = "score"
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate, start_drive
        elif gamestate == "deftd+pat":
            score[0] = score[0] + 7
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+nopat":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+2pt":
            score[0] = score[0] + 8
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        elif gamestate == "deftd+no2pt":
            score[0] = score[0] + 6
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            gamestate = "defscore"
            return score, gamestate, start_drive
        else:
            print(f'Exiting drive_start function with gamestate {gamestate} and score {score}...')
            return score, gamestate, start_drive
