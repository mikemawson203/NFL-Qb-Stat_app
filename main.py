games = []

while True:
    game = {}
    game['game'] = len(games) + 1
    game['pass_att'] = int(input("Enter passing attempts for game {}: ".format(game['game'])))
    game['pass_cmp'] = int(input("Enter passing completions for game {}: ".format(game['game'])))
    game['pass_yds'] = int(input("Enter passing yards for game {}: ".format(game['game'])))
    game['pass_tds'] = int(input("Enter passing touchdowns for game {}: ".format(game['game'])))
    game['pass_ints'] = int(input("Enter interceptions for game {}: ".format(game['game'])))
    games.append(game)

    if input("Enter another game? (y/n) ") == 'n':
        break

totals = {'pass_att': 0, 'pass_cmp': 0, 'pass_yds': 0, 'pass_tds': 0, 'pass_ints': 0}

for game in games:
    totals['pass_att'] += game['pass_att']
    totals['pass_cmp'] += game['pass_cmp']
    totals['pass_yds'] += game['pass_yds']
    totals['pass_tds'] += game['pass_tds']
    totals['pass_ints'] += game['pass_ints']

totals['pass_cmp_pct'] = 100 * totals['pass_cmp'] / totals['pass_att']

print("Attempts:", totals['pass_att'])
print("Completions:", totals['pass_cmp'])
print("Completion Percentage: {:.1f}%".format(totals['pass_cmp_pct']))
print("Yards:", totals['pass_yds'])
print("Touchdowns:", totals['pass_tds'])
print("Interceptions:", totals['pass_ints'])
