

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


youngest_age = 999

youngest_name = ""

for line in people:
    people_split = line.split()
    name = people_split[0]
    age = int(people_split[1])
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")