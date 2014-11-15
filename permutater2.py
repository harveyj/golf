a=raw_input()
v=[""]
for c in a:v=[z[:i]+c+z[i:]for z in v for i in range(len(z)+1)]
print'\n'.join(v)
