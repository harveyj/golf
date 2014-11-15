import re
d="shinichiro"
e=" of hamaji"
a=d+"es"+e
b="on the wall"
c="Take one down and pass it around"
s=""
l="%i %s %s, %i %s.\n"
for i in range(99,1,-1):s+=(l+"%s, %i %s %s.\n\n")%(i,a,b,i,a,c,i-1,a,b)
s+=l%(1,a,b,1,a)+"Go to the store and buy some more, 99 %s %s."%(a,b)
print re.sub("\\b1 "+a,"1 "+d+e,s)
