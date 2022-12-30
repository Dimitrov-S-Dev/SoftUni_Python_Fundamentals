snowballs_count = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quantity = 0

for ball in range(snowballs_count):
    ball_weight = int(input())
    ball_time = int(input())
    ball_quality = int(input())
    ball_value = (ball_weight / ball_time) ** ball_quality
    if ball_value > max_value:
        max_value = ball_value
        max_weight = ball_weight
        max_time = ball_time
        max_quantity = ball_quality

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quantity})")
