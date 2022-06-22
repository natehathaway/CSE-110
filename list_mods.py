

#Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.

#Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk

#Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.


shopping_list = []

new_item = input("Please enter the items of the shopping list (type: quit to finish): ")

while new_item.lower() != "quit":
    shopping_list.append(new_item)
    new_item = input("Please enter the items of the shopping list (type: quit to finish): ")

print()
print("Your shopping list is:")
for item in shopping_list:
    print(item)


print()
print("Your shopping list index is: ")
for index in range(len(shopping_list)):
    print(index, shopping_list[index])

print()
item_index = int(input("Please enter the index of the item you want to change: "))
change_item = input("Please enter the new item: ")
shopping_list[item_index] = change_item

print("Your new shopping list is:")
for item in shopping_list:
    print(item)