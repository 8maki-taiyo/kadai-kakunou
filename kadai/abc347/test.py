from collections import Counter

s=input()
c = list(Counter(s).values())
n = len(c)
ans = 0
for i in range(n):
  for j in range(i+1, n):
    ans += c[i]*c[j]
if max(c)>1:
  ans+=1
print(ans)