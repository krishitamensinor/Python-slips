s="Hello, World"
p="!@#$%^&*(),."
r=""

for i in s:
  if i not in p:
    r=r+i
    print(r)