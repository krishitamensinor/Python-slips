def arm(n):
  s=0
  t=n
  while t>0:
    d=t%10
    s=s+d*d*d
    t//=10

  if s==n:
    print("Armstrong")
  else:
    print("Not Armstrong")

arm(153)