
#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)


def wind_chill(temperature, wind):
    return 35.74 + (0.6215 * temperature) - (35.75 * (wind ** 0.16)) + (0.4275 * temperature) * (wind ** 0.16)

temp = float(input("What is the temperature? "))
temp_type = input("Fahrenheit or Celsius (F/C)?")
wind = 5

if temp_type == "C":
    new_temp = (temp * 9 / 5) + 32
else:
    new_temp = temp

while wind <= 60:
    total_temp = wind_chill(new_temp, wind)
    print(f"At temperature {new_temp}F, and wind speed {wind} mph, the windchill is: {total_temp:.2f}F")
    wind += 5




