from pipe import select, where

arr = [1,2,3,4,5]

ans = list(arr
     | where(lambda x: x%2 == 0)
     | select(lambda x: x*2)
     )
print(ans)
