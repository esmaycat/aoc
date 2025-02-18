import re
l=int.__mul__
d=re.findall(r"(?:do|'t)\(\)|l\(\d+,\d+\)",open(0).read())
s=1
print(sum((s:='d'<i)and 0 if'e'>i else eval(i)*s for i in d))