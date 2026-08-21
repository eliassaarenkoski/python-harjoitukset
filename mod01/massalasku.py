leiviskät = float(input("anna leiviskät:"))
naulat = float(input("anna naulat:"))
luodit = float(input("anna luodit:"))

leiviskämassa = (20 * 32 * 13.3 * leiviskät)
naulamassa = (32 * 13.3 * naulat)
luotimassa = (13.3 * luodit)

yhteismassa = (leiviskämassa + naulamassa + luotimassa) 
kilomassa = (yhteismassa // 1000)
grammamassa = (yhteismassa % 1000)

print (f"{kilomassa:2.0f} kg ja {grammamassa:3.2f} grammaa")