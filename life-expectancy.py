
import csv



with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    data_list=[]
    for line in life_expectancy:
        data = line.strip()
        try:
            item = data.split(",")[3]
            data_list.append(float(item))
        except:
            pass
    
    print(f"The overall max life expectancy is: {max(data_list)}")
    print(f"The overall min life expectancy is: {min(data_list)}")

    

