team_a = [f'A-{x}' for x in range(1, 12)]
team_b = [f'B-{x}' for x in range(1, 12)]
cards = input().split()
is_terminated = False

for card in cards:
    if 'A' in card:
        if card in team_a:
            team_a.remove(card)
    else:
        if card in team_b:
            team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if is_terminated:
    print('Game was terminated')
