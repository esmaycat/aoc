from collections import* # type: ignore
R,U=([(*l.split(s),)for l in c.splitlines()]for c,s in zip(open(0).read().split('\n\n'),'|,'))
*a,=0,0
for u in U:
 o=Counter(r[0]for r in{r for r in R if set(u)>={*r}})
 s=sorted(u,key=lambda x:-o[x])
 a[u!=(*s,)]+=int(s[len(u)//2]) # type: ignore
print(a)