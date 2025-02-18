f=lambda l:all(0<(2*(l[0]-l[1]>0)-1)*i<4 for i in[a-b for(a,b)in zip(l,l[1:])])
print(sum(f(l)+1j*any(f(l[:i]+l[i+1:])for i in range(len(l)))for l in[[*map(int,l.split())]for l in open(0)]))