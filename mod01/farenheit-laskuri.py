farenheitarvo_str = input("Anna lämpötila farenheit-asteina:")
farenheit = float(farenheitarvo_str)
celsius = (farenheit - 32) * 5 / 9
print("Lämpötila Celsius-asteina: " + str(celsius))

farenheitarvo_str = input("Anna lämpötila farenheit-asteina:")
farenheit = float(farenheitarvo_str)
celsius = (farenheit - 32) * 5 / 9
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")
