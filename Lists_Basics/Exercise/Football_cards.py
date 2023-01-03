# team_a = 11
# team_b = 11
# red_cards = input().split()
# sent_off_players = []
# is_terminated = False
#
# for card in red_cards:
#     if card not in sent_off_players:
#         sent_off_players.append(card)
#         if 'A' in card:
#             team_a -= 1
#         elif 'B' in card:
#             team_b -= 1
#     if team_a < 7 or team_b < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {team_a}; Team B - {team_b}")
# if is_terminated:
#     print("Game was terminated")


team_a = ['A-' + str(s) for s in range(1, 12)]
team_b = ['B-' + str(s) for s in range(1, 12)]
red_cards = input().split()
is_terminated = False

for card in red_cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")
