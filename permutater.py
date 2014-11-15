a=raw_input()
v=[""]
for c in a:
  nv = []
  for vi in v:
    nv += [vi[:i]+c+vi[i:] for i in range(len(vi)+1)]
  v=nv
print'\n'.join(v)
