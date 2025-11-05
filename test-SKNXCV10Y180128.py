import time

ordlista=["hej", "1"]
förklaringar=["En hälsning", "siffran 1"]

while True:

    print("Vad vill du göra?\n1) Slå upp ett ord.\n2) Lägga till ett ord.\n3) Ta bort ett ord.\n4) Avsluta.")
    command=input("")

    if command=="1": # söka efter ord
        ord=input("Vilket ord vill du slå upp? ")
        if ord in ordlista: # finns ordet i ordlistan?
            ordindex=ordlista.index(ord)
            print("Ordet " + ord + " betyder: " + förklaringar[ordindex] + "\n")

        else: # om ordet inte hittades
            print("\nOrdet hittades inte i ordlistan\n")
        time.sleep(1)

    elif command=="2": # lägga till ord
        ordlista.append(input("Vilket ord vill du lägga till? "))
        förklaringar.append(input("Vad betyder ordert? "))
        time.sleep(1)

    elif command=="3": # ta bort ord
        bort=input("Vilket ord vill du ta bort? ")
        if bort in ordlista:
            bortindex=ordlista.index(bort)
            ordlista.pop(bortindex)
            förklaringar.pop(bortindex)
            print("\nOrdet " + bort + " är borttaget!\n")

        else:
            print("Ordet hittades inte i ordlistan\n")

    elif command=="4": # slut
        print("Hejdå!")
        break

    else: # fel
        print("command not found")