times = int(input("Matches played:"))
score = 0
wins = 0
for i in range(times):
    match1 = input("input: ")

    match1 = match1.split("-")
    print(match1)
    my_team = int(match1[0])
    opponent = int(match1[1])
    if my_team> opponent:
        score += 3
        wins += 1
    elif my_team<opponent:
        score += 0
    else:
        score += 1

print(f"Total points: {score}")
print(f"Winning percentage: {(wins/times)*100}%")







    
    
