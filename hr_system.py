

with open("hr_system.txt") as hr_system:
    for line in hr_system:
        data = line.strip()
        data_list = data.split(" ")
        print(f"Name: {data_list[0]}, Title: {data_list[2]} ")

