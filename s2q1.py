p=float(input("Enter P : "))
r=float(input("Enter R : "))
t=float(input("Enter T : "))

si=(p*r*t)/100
ci=p*(1+r/100)**t-p

print("Simple interest : ",si)
print("Compound interest : ",ci)