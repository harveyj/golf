a,b,c,d,e,f,g,h,i="Ace- of -Jack-Queen-King-Spades-Hearts-Diamonds-Clubs".split("-")
m=[a]+map(str,range(2,11))+[c,d,e]
_=raw_input()
for k in f,g,h,i:
 for j in m:
  if j not in _ and k not in _:print j+b+k

