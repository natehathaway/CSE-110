import statistics
import csv
lowest = 9999999
lowest2 = 9999999
highest = -1
highest2 = -1
num_list = []


pick_year = input("What year would you like to know about from 1950 to 2019? ")

with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    for line in life_expectancy:
        sweep_line = line.strip()
        parts = sweep_line.split(",")
        country = parts[0]
        code = parts[1]
        year = parts[2]
        expectancy = float(parts[3])
        if expectancy < lowest:
            lowest = expectancy
            lowest_place = country
            lowest_year = year
        if expectancy > highest:
            highest = expectancy
            highest_place = country
            highest_year = year
        if pick_year == year:
            if expectancy > highest2:
                highest2 = expectancy
                num_list.append(expectancy)
                highest_place2 = country
            if expectancy < lowest2:
                lowest2 = expectancy
                num_list.append(expectancy)
                lowest_place2 = country

Sum = sum(num_list)
length = len(num_list)
average = (Sum/length)
            
if pick_year == "2000":
    print("Hey that's my birth year!")

print(f"{lowest_place} has the lowest life expectancy at {lowest} in the year {lowest_year}")
print(f"{highest_place} has the highest life expectancy at {highest} in the year {highest_year}")
print()
print(f"The average life expectancy for {pick_year} is {average:.2f}.")
print(f"The lowest life expectancy is {lowest2} at {lowest_place2} in {pick_year}.")
print(f"The highest life expectancy is {highest2} at {highest_place2} in {pick_year}.")

print("press ENTER to exit program")






    

