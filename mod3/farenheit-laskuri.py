farenheitarvo_str = float(input("Anna lämpötila farenheit-asteina:"))
farenheit = float(farenheitarvo_str)
celsius = (farenheit - 32) * 5 / 9
print("Lämpötila Celsius-asteina: " + str(celsius))

farenheitarvo_str = input("Anna lämpötila farenheit-asteina:")
farenheit = float(farenheitarvo_str)
celsius = (farenheit - 32) * 5 / 9
print(f"Lämpötila Celsius-asteina: {celsius:10.2f}")

#vielä tiivistetympi koodin pätkä tehty oppimisen jälkeen 26.8.26
fahrenheit_str = float (input("Anna lämpötila Fahrenheit-asteina: "))
celsius = (fahrenheit_str - 32) * 5 / 9
print(f"Lämpötila Celsius-asteina: {celsius:10.2f}")