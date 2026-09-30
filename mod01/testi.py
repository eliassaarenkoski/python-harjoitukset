arvo = int(input("anna luku 1-5 : "))
while arvo !=1 or arvo !=2 or arvo !=3:
    if arvo >=4:
        print("jatektaan")
        arvo = int(input("anna luku 1-5 : "))
    else:
        print("n")
        break

luvut = [2, 7, 10, 15, 1, 2]
luvut1= len(luvut)
luvut2 = []
luvut2.append(luvut1)

for luku in luvut2:
    if luku == 4:
        print("Pieni lista")
    elif luku >=10:
        print("Keskikokoinen")
    else:
        print("jotain 4 ja 10 väliltä")
print(luvut1)