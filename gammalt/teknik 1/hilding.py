hilding = input("är hilding snygg? (Y/n) ")
if hilding == "Y" or hilding == "y" or hilding == "ja" or hilding == "Ja":
    print("du har rätt!")
else:
    print("käften!")

hilding_ålder = int(input("hur gammal är du? " ))
hilding_å = hilding_ålder-10
if hilding_å < 0:
    hilding_å = 0

if hilding_ålder == 0:
    print("vad ung du är!")
elif hilding_ålder < 18:
    print("du är omynding >:(")
elif hilding_ålder > 65:
    print("vad gammal du är!")
else:
    print("kul att du är vuxen!")

print("" \
"")

print("hilding är " + str(hilding_å) + " år gammal!")