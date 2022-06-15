
#Compute the sum, or total, of the numbers in the list.
#Compute the average of the numbers in the list.
#Find the maximum, or largest, number in the list.

number_list = []
number = int(input("Enter a number: "))
while number != 0:
    number_list.append(number)
    number = int(input("Enter a number: "))
    
print("The sum is:", sum(number_list))
print("The average is:", sum(number_list) / len(number_list))
print("The largest number is:", max(number_list))

print("The smallest positive number is:", min([i for i in number_list if i > 0]))

sorted_list = sorted(number_list)
print("The sorted list is:")

for number in sorted_list:
    print(number)



#Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

#Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.