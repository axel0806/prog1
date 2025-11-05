import time

ordlista2={
    "hej":"en hälsning",
    "1":"siffran 1"
}

# ordlista=["hej", "1"]
# förklaringar=["En hälsning", "siffran 1"]

while True:

    print("Vad vill du göra?\n1) Slå upp ett ord.\n2) Lägga till ett ord.\n3) Ta bort ett ord.\n4) Ändra förklaring av ett ord.\n5) Avsluta.")
    command=input("")

    if command=="1": # söka efter ord
        ord=input("Vilket ord vill du slå upp? ")
        if ord in ordlista2: # finns ordet i ordlistan?
            # ordindex=ordlista.index(ord)
            print("\nOrdet " + ord + " betyder: " + ordlista2[ord] + "\n")

        else: # om ordet inte hittades
            print("\nOrdet hittades inte i ordlistan\n")
        time.sleep(1)

    elif command=="2": # lägga till ord
        l_ord=input("Vilket ord vill du lägga till? ")
        if l_ord in ordlista2:
            print("\nOrdet finns redan i ordlistan\n")
        else:
            # ordlista2.append(l_ord)
            f_ord=input("Vad betyder ordet? ")
            ordlista2[l_ord]=f_ord
            # förklaringar.append(input("Vad betyder ordert? "))
            time.sleep(1)

    elif command=="3": # ta bort ord
        bort=input("Vilket ord vill du ta bort? ")
        if bort in ordlista2:
            # bortindex=ordlista.index(bort)
            ordlista2.pop(bort)
            # förklaringar.pop(bortindex)
            print("\nOrdet " + bort + " är borttaget!\n")
            time.sleep(1)

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