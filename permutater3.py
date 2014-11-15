def f(a):
  v=[]
  if a=="": return[a]
  for i,x in enumerate(a):v+=[a[i]+v for v in f(a[:i]+a[i+1:])]
  return v
print "\n".join(f(raw_input()))
