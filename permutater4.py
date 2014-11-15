def f(a):
  v=[]
  if a==[]: return[""]
  for c in a:v+=[a[i]+v for v in f(a.remove(c))]
  return v
print "\n".join(f(list(raw_input())))
