s=map(int,raw_input().split())
i=c=0
while 1:
 n,o=s[i:i+2];c+=n+o
 if 10in[n,n+o]:c+=s[i+2]
 i+=(1,2)[n!=10];print c,