import time
# from colorama import Fore, Back, Style, init # type: ignore
# from termcolor import colored # type: ignore

# init(autoreset=True)

ordlista2={
    "hej":"en hälsning",
    "1":"siffran 1"
}

# ordlista=["hej", "1"]
# förklaringar=["En hälsning", "siffran 1"]

namn=(r"""
   ____          _ _           _              
  / __ \        | | |         | |             
 | |  | |_ __ __| | |__   ___ | | _____ _ __  
 | |  | | '__/ _` | '_ \ / _ \| |/ / _ \ '_ \ 
 | |__| | | | (_| | |_) | (_) |   <  __/ | | |
  \____/|_|  \__,_|_.__/ \___/|_|\_\___|_| |_|
                                              
                                              """)

#   ____          _ _           _              
#  / __ \        | | |         | |             
# | |  | |_ __ __| | |__   ___ | | _____ _ __  
# | |  | | '__/ _` | '_ \ / _ \| |/ / _ \ '_ \ 
# | |__| | | | (_| | |_) | (_) |   <  __/ | | |
#  \____/|_|  \__,_|_.__/ \___/|_|\_\___|_| |_|
                                              
                                              
print(namn)

while True:

    # print("Vad vill du göra?\n1) Slå upp ett ord.\n2) Lägga till ett ord.\n3) Ta bort ett ord.\n4) Ändra förklaring av ett ord.\n5) Avsluta.")
    # print(namn)
    print("1) Slå upp ett ord.")
    print("2) Lägga till ett ord.")
    print("3) Ta bort ett ord.")
    print("4) Ändra förklaring av ett ord.")
    print("5) Avsluta.")
    command=input("")

    if command=="1": # söka efter ord
        ord=input("Vilket ord vill du slå upp? ")
        if ord in ordlista2: # finns ordet i ordlistan?
            # ordindex=ordlista.index(ord)
            print("\nOrdet " + ord + " betyder: " + ordlista2[ord] + "\n")

        else: # om ordet inte hittades
            print("\nOrdet hittades inte i ordlistan\n")

    elif command=="2": # lägga till ord
        l_ord=input("Vilket ord vill du lägga till? ")
        if l_ord in ordlista2:
            print("\nOrdet finns redan i ordlistan\n")
        else:
            # ordlista2.append(l_ord)
            f_ord=input("Vad betyder ordet? ")
            ordlista2[l_ord]=f_ord
            # förklaringar.append(input("Vad betyder ordert? "))

    elif command=="3": # ta bort ord
        bort=input("Vilket ord vill du ta bort? ")
        if bort in ordlista2:
            # bortindex=ordlista.index(bort)
            ordlista2.pop(bort)
            # förklaringar.pop(bortindex)
            print("\nOrdet " + bort + " är borttaget!\n")

        else:
            print("\nOrdet hittades inte i ordlistan\n")

    elif command=="4":
        andra=input("Vilket ords betydelse vill du ändra? ")
        if andra in ordlista2:
            # andraIndex=ordlista.index(andra)
            andring=input("Vad ska ordet ha för någon förklaring? ")
            ordlista2[andra]=andring
            # förklaringar.pop(andraIndex)
            # förklaringar.insert(andraIndex, andring)

        else:
            print("\nOrdet hittades inte i ordlistan\n")

    elif command=="5": # slut
        print("\nHejdå!\n")
        break

    else: # fel
        print("\ncommand not found\n")