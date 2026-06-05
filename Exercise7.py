# Exercise Tempereture Converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * (9/5)) + 32
    print(f"Your temperature is: {round(temp)}°F")
elif unit == "F":
    temp = (5 * (temp - 32) / 9)
    print(f"Your temperature is: {round(temp)}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
