print("Detta program beräknar potenser\n")
b=int(input("Skriv potensens bas\nBas = "))
x=int(input("Skriv in potensens exponent\nExp = "))
p=1

if x>0: #positiva potesner
    for i in range(x):
        p=p*b
elif x<0: #negativa potenser
    for i in range(abs(x)):
        p=p/b
print(b, "upphöjt med ", x, " = ", p)