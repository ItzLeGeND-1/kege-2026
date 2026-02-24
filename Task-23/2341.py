
def f(start, k):
    if k == 8:
        if start in range(1000, 1025): return {start}
        return set()
    return f(start + 1, k + 1) | f(start + 5, k + 1) | f(start * 3, k + 1)

print(len(f(1, 0)))

#######################################

def f(cur, cnt=0):
    if cnt == 8:
        if 1000 <= cur <= 1024:
            spots.add(cur)
        return
    f(cur + 1, cnt + 1)
    f(cur + 5, cnt + 1)
    f(cur * 3, cnt + 1)


spots = set()
f(1)
print(len(spots))