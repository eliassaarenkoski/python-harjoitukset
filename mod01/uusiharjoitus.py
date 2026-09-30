oikeatvastaukset = {
    1:"100",
    2:"200",
    3:"300",
    "tehtävä_4" : "kyllä"
}

kayttajan_vastaukset = {}
pisteet = []

def tarkistus (tehtävä):
    if oikeatvastaukset[tehtävä] == kayttajan_vastaukset[tehtävä]:
        print("vastasit onneksi oikein! ")
        pisteet.append(kayttajan_vastaukset)
    else:
        print("vastasit päin veetä")

kayttajan_vastaukset[1] = input("\nTehtävä 1:\nmikä on 50 + 50 summa : ")
tarkistus(1)

kayttajan_vastaukset[2] = input("\nTehtävä 2:\nmikä on 100 + 100 summa : ")
tarkistus(2)

kayttajan_vastaukset[3] = input("\nTehtävä 3: \nmikä on 200 + 100 summa : ")
tarkistus(3)

kayttajan_vastaukset["tehtävä_4"] = input("\nOnko python ohjelmointikieli vastaa kyllä/ei : ")
tarkistus("tehtävä_4")
print(f"\nsinun vastaukset ovat  : {kayttajan_vastaukset}")
print(f"\noikeat vastaukset ovat : {oikeatvastaukset}")
print(f"\nsait pistettä {len(pisteet)}/4")
