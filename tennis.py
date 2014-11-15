s=[0]*3
z="Player%%i %s %%i - %%i"
a=z%"wins the set"
b=z%"leads"
p=lambda x:print(x)
while 1:
  s[input()]+=1;(m,n,o)=s;v=((1,n,o),(2,o,n))[o>n]
  if 7 in s: p(a%v);break
  p("Set is tied at "+`n`,b%v)[o!=n]
