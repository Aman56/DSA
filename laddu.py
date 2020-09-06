# cook your dish here
for _ in range(int(input())):
    n, origin = input().split()
    activity = []
    for __ in range(int(n)):
        activity.append(input())
    laddu = 0
    for act in activity:
        if 'CONTEST_WON' in act:
            rank = int(act.split()[1])
            laddu += 300    
            if rank <= 20:
                laddu += 20-rank
        if 'TOP_CONTRIBUTOR' in act:
            laddu += 300
        if 'BUG_FOUND' in act:
            severity = int(act.split()[1])
            laddu += severity
        if 'CONTEST_HOSTED' in act:
            laddu += 50

    if origin == 'INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)
