import decimal
import math
import random

avg_variance = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5]

def rng():
    print(f'In rng() function...')
    randnum = random.uniform(.75, 1.25)     # Generates random number between .75 and 1.25
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

def prestige_luck(team):
    print(f'In prestige_luck function...')
    prestigeboost = 0.0
    prestigehelp = game_rng()
    print(f'prestigehelp for {team["nameabbr"]} is {prestigehelp}')
    if team["prestige"] >= 50:
        if 0.90 >= prestigehelp >= 0.10:
            prestigeboost = 1.2
            print(f'{team["nameabbr"]} will receive a small boost for being prestigious')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if prestigehelp > 0.90:
            prestigeboost = 2
            print(f'{team["nameabbr"]} will receive a large boost for being prestigious [been there, done that boost]')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if 0.05 <= prestigehelp < 0.10:
            prestigeboost = 0.75
            print(f'{team["nameabbr"]} will receive a small debuff [underestimated opponent debuff]')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if prestigehelp < 0.05:
            prestigeboost = 0.5
            print(f'{team["nameabbr"]} will receive a large debuff [when it rains, it pours debuff]')
            print(f'Exiting prestige_luck function...')
            return prestigeboost

    if team["prestige"] < 50:
        if 0.90 >= prestigehelp >= 0.10:
            prestigeboost = 1
            print(f'{team["nameabbr"]} will play normally as a less prestigious team')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if prestigehelp > 0.90:
            prestigeboost = 2
            print(f'{team["nameabbr"]} will receive a large boost [underdog boost]')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if 0.05 <= prestigehelp < 0.10:
            prestigeboost = 0.75
            print(f'{team["nameabbr"]} will receive a small debuff for being less prestigious')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
        if prestigehelp < 0.05:
            prestigeboost = 0.5
            print(f'{team["nameabbr"]} will receive a large debuff [deer in headlights debuff]')
            print(f'Exiting prestige_luck function...')
            return prestigeboost
