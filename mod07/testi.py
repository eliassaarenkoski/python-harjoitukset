kerrat = int(input("anna kerta moi:lle : "))
tervehdys = int(input("anna tervehdys kerrat : "))

def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print(tervehdys + " " + str(i+1) + ". kerran")
    return

tervehdi("Moi", kerrat)
tervehdi("Hyvää päivää", tervehdys)