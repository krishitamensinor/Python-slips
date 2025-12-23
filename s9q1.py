total=0
print("Enter numbers below...")
for i in range(10):
  n=int(input("Enter number : "))
  if n%2!=0:
    total+=n
print("Sum of odd numbers : ",total)