arr = [1,2,3,4,5]
ans = list(map(lambda x: x*2, filter(lambda x: x%2 == 0, arr)))
print(ans)
