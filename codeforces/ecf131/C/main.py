t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    worker_hours_prof = [0] * n
    # assign all proficient tasks first, then subtract what you need to move to others
    for proficient_worker in a:
        worker_hours_prof[proficient_worker-1] += 1
    worker_hours_total = worker_hours_prof.copy()
    mx = max(worker_hours_total) # Only want workers with proficient hours
    mn = min(worker_hours_total)
    while mx >= mn + 2:
        worker_hours_prof[worker_hours.index(mx)] -= 1
        worker_hours_total[worker_hours.index(mx)] -= 1
        worker_hours_total[worker_hours.index(mn)] += 2
        mx = max(worker_hours)
        mn = min(worker_hours)
    print(mx)
