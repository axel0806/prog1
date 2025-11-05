x=int(input("hur gammal är du?\ndin ålder = "))

if x<18:
    if x>14:
        print("du är omyndig")
    else:
        print("ungjävel")
elif x>64:
    print("du är pensionär")
else:
    print("du är vuxen")