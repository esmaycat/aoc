d=open(0).read()
R,w=[*range(len(d))],d.index('\n')+1;N=w+1,w-1
print(sum(sum(d[i::p][:4]in('XMAS','SAMX')for p in(1,w)+N)+1j*({d[i-p::p][:3]for p in N}<={'SAM','MAS'})for i in R))