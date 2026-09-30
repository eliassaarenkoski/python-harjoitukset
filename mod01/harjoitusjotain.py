teksti = input("Anna teksti: ")

for merkki in teksti:
    print(f"{ord(merkki):08b}")